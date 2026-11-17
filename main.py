#!/usr/bin/env python3
"""
NIT Jamshedpur Main Gate E-Rickshaw Dispatch Optimizer
Author: Vivek Paswan (NIT Jamshedpur)
Informant & Driver: Manoj Mahato (Blue E-Rickshaw, NIT Main Gate Stand)
Date: November 17, 2026

Description:
  Evaluates empirical queue holding times, passenger walk-away churn,
  and turnover rates for e-rickshaw drivers at NIT Jamshedpur Main Gate.
  Generates an optimal dispatch policy balancing seat-fill vs churn risk.
"""

import csv
import sys
from statistics import mean

# ==============================================================================
# INTERVIEW-TUNABLE THRESHOLDS (Live editable during technical interviews)
# ==============================================================================
MAX_SEAT_CAPACITY = 5            # Maximum passenger seats in Manoj's blue e-rickshaw
CHURN_RISK_WAIT_MINS = 8         # Wait threshold where seated passengers abandon to autos
MIN_PROFITABLE_PASSENGERS = 3    # Minimum passenger count to cover trip battery & time costs
TARGET_DISPATCH_WAIT_MINS = 6    # Recommended maximum holding cutoff at gate
AVG_ONEWAY_TRANSIT_MINS = 12     # Average transit time to Adityapur Station or Bistupur
# ==============================================================================

REQUIRED_COLUMNS = {
    "trip_id",
    "arrival_time",
    "depart_time",
    "wait_mins",
    "passengers_boarded",
    "passengers_walked_away",
    "destination",
    "fare_total_inr",
    "notes",
}


def parse_and_validate_row(row_dict, line_num):
    """
    Validates a single CSV row. Returns a cleaned dict if valid, or None if malformed.
    Prints informative, non-crashing warnings to stderr on failure.
    """
    missing = REQUIRED_COLUMNS - set(row_dict.keys())
    if missing:
        sys.stderr.write(f"[WARN] Line {line_num}: Skipped - missing required column(s): {', '.join(missing)}\n")
        return None

    try:
        trip_id = int(row_dict["trip_id"].strip())
        wait_mins = float(row_dict["wait_mins"].strip())
        passengers_boarded = int(row_dict["passengers_boarded"].strip())
        passengers_walked_away = int(row_dict["passengers_walked_away"].strip())
        fare_total_inr = float(row_dict["fare_total_inr"].strip())
    except (ValueError, TypeError, AttributeError) as err:
        sys.stderr.write(f"[WARN] Line {line_num}: Skipped - numeric parsing error ({err})\n")
        return None

    # Sanity range checks
    if wait_mins < 0:
        sys.stderr.write(f"[WARN] Line {line_num} (Trip {trip_id}): Skipped - negative wait time ({wait_mins})\n")
        return None

    if passengers_boarded < 0 or passengers_boarded > MAX_SEAT_CAPACITY:
        sys.stderr.write(
            f"[WARN] Line {line_num} (Trip {trip_id}): Skipped - invalid passengers boarded "
            f"({passengers_boarded}); valid capacity is 0 to {MAX_SEAT_CAPACITY}\n"
        )
        return None

    if passengers_walked_away < 0:
        sys.stderr.write(
            f"[WARN] Line {line_num} (Trip {trip_id}): Skipped - negative passengers walked away ({passengers_walked_away})\n"
        )
        return None

    if fare_total_inr < 0:
        sys.stderr.write(f"[WARN] Line {line_num} (Trip {trip_id}): Skipped - negative fare ({fare_total_inr})\n")
        return None

    destination = row_dict["destination"].strip()
    if not destination:
        sys.stderr.write(f"[WARN] Line {line_num} (Trip {trip_id}): Skipped - empty destination\n")
        return None

    return {
        "trip_id": trip_id,
        "arrival_time": row_dict["arrival_time"].strip(),
        "depart_time": row_dict["depart_time"].strip(),
        "wait_mins": wait_mins,
        "passengers_boarded": passengers_boarded,
        "passengers_walked_away": passengers_walked_away,
        "destination": destination,
        "fare_total_inr": fare_total_inr,
        "notes": row_dict["notes"].strip(),
    }


def load_dataset(filepath):
    """
    Reads CSV file safely, skips malformed rows with warnings, and returns clean records.
    """
    valid_trips = []
    skipped_count = 0

    try:
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                sys.stderr.write(f"[ERROR] File '{filepath}' is empty or unreadable.\n")
                return [], 0

            for line_idx, row in enumerate(reader, start=2):  # line 1 is header
                parsed = parse_and_validate_row(row, line_idx)
                if parsed:
                    valid_trips.append(parsed)
                else:
                    skipped_count += 1
    except FileNotFoundError:
        sys.stderr.write(f"[ERROR] Could not find data file at '{filepath}'.\n")
        sys.exit(1)
    except Exception as err:
        sys.stderr.write(f"[ERROR] Unexpected I/O error reading '{filepath}': {err}\n")
        sys.exit(1)

    return valid_trips, skipped_count


def calculate_and_report(trips, skipped_count, filepath):
    total_valid = len(trips)
    if total_valid == 0:
        print(f"[!] No valid trips found in {filepath} to analyze.")
        return

    wait_times = [t["wait_mins"] for t in trips]
    boarded_counts = [t["passengers_boarded"] for t in trips]
    fares = [t["fare_total_inr"] for t in trips]
    walkaways = [t["passengers_walked_away"] for t in trips]

    avg_wait = mean(wait_times)
    avg_boarded = mean(boarded_counts)
    total_revenue = sum(fares)
    total_walkaways = sum(walkaways)

    # Churn breakdown by wait threshold
    trips_over = [t for t in trips if t["wait_mins"] >= CHURN_RISK_WAIT_MINS]
    trips_under = [t for t in trips if t["wait_mins"] < CHURN_RISK_WAIT_MINS]

    walkaways_over = sum(t["passengers_walked_away"] for t in trips_over)
    churn_rate_over = (walkaways_over / len(trips_over)) if trips_over else 0.0

    walkaways_under = sum(t["passengers_walked_away"] for t in trips_under)
    churn_rate_under = (walkaways_under / len(trips_under)) if trips_under else 0.0

    # Hourly earning rate: (Revenue / Total Cycle Time) * 60
    def compute_hourly_rate(trip_subset):
        if not trip_subset:
            return 0.0
        total_fare = sum(t["fare_total_inr"] for t in trip_subset)
        total_time_mins = sum(t["wait_mins"] + AVG_ONEWAY_TRANSIT_MINS for t in trip_subset)
        return (total_fare / total_time_mins) * 60.0

    rate_disciplined = compute_hourly_rate(trips_under)
    rate_stalled = compute_hourly_rate(trips_over)

    # Output formatted report
    print("=" * 72)
    print(" NIT JAMSHEDPUR MAIN GATE: E-RICKSHAW DISPATCH OPTIMIZATION TOOL")
    print(" Field Informant: Manoj Mahato (Blue E-Rickshaw, 4 Years at Stand)")
    print(" Target Route   : NIT Main Gate -> Adityapur Station / Bistupur")
    print("=" * 72)
    print(f" Dataset Source                 : {filepath}")
    print(f" Valid Trips Processed          : {total_valid}")
    if skipped_count > 0:
        print(f" Malformed / Skipped Rows       : {skipped_count} (see warnings above)")
    print(f" Average Stand Wait Time        : {avg_wait:.1f} minutes")
    print(f" Average Boarded Passengers     : {avg_boarded:.1f} / {MAX_SEAT_CAPACITY} seats")
    print(f" Total Recorded Passenger Churn : {total_walkaways} passengers lost")
    print("-" * 72)
    print(" CHURN RISK & DISPATCH THRESHOLD METRICS:")
    print(f"  • Wait < {CHURN_RISK_WAIT_MINS} mins (Disciplined)   : {churn_rate_under:.2f} walk-aways/trip | Earning: Rs {rate_disciplined:.1f}/hr")
    print(f"  • Wait >= {CHURN_RISK_WAIT_MINS} mins (Stalled for 5/5): {churn_rate_over:.2f} walk-aways/trip | Earning: Rs {rate_stalled:.1f}/hr")
    print("-" * 72)
    print(" CONCRETE DISPATCH RULE FOR MANOJ MAHATO:")
    print(f"  1. Capped Wait Target: Set a hard timer for {TARGET_DISPATCH_WAIT_MINS} minutes upon arriving at the stand.")
    print(f"  2. Threshold Departure: If at minute {TARGET_DISPATCH_WAIT_MINS} you have {MIN_PROFITABLE_PASSENGERS}+ passengers, DEPART IMMEDIATELY.")
    print(f"  3. Avoid the 8-Minute Trap: Holding for a 4th or 5th passenger past {CHURN_RISK_WAIT_MINS} minutes")
    print(f"     causes seated students to deboard ({churn_rate_over:.1f} lost/trip to passing autos),")
    print(f"     collapsing net hourly earnings from Rs {rate_disciplined:.0f}/hr down to Rs {rate_stalled:.0f}/hr.")
    print("=" * 72)


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 main.py [path_to_data.csv]")
        print("Analyzes e-rickshaw dispatch and passenger churn for NIT Jamshedpur gate.")
        sys.exit(0)

    filepath = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    trips, skipped = load_dataset(filepath)
    calculate_and_report(trips, skipped, filepath)


if __name__ == "__main__":
    main()
