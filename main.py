#!/usr/bin/env python3
"""
NIT Jamshedpur Main Gate E-Rickshaw Dispatch Optimizer
Author: Vivek Paswan (NIT Jamshedpur)
Informant & Driver: Manoj Mahato (Blue E-Rickshaw, NIT Main Gate Stand)
Date: November 17, 2026
"""

import csv
import sys
from statistics import mean

# ==============================================================================
# INTERVIEW-TUNABLE THRESHOLDS (Easily modifiable during live walkthrough)
# ==============================================================================
MAX_SEAT_CAPACITY = 5            # Physical passenger seating limit of e-rickshaw
CHURN_RISK_WAIT_MINS = 8         # Wait time beyond which seated passengers start deboarding
MIN_PROFITABLE_PASSENGERS = 3    # Minimum passenger count to break even on energy + time
TARGET_DISPATCH_WAIT_MINS = 6    # Maximum recommended waiting target before departing
AVG_ONEWAY_TRANSIT_MINS = 12     # Typical transit time to Adityapur Station / Bistupur


def load_and_analyze(filepath="data.csv"):
    trips = []
    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            trips.append({
                "trip_id": int(row["trip_id"]),
                "arrival_time": row["arrival_time"],
                "depart_time": row["depart_time"],
                "wait_mins": float(row["wait_mins"]),
                "passengers_boarded": int(row["passengers_boarded"]),
                "passengers_walked_away": int(row["passengers_walked_away"]),
                "destination": row["destination"],
                "fare_total_inr": float(row["fare_total_inr"]),
                "notes": row["notes"],
            })

    total_trips = len(trips)
    if total_trips == 0:
        print("No trips to analyze.")
        return

    # Aggregate metrics
    wait_times = [t["wait_mins"] for t in trips]
    boarded_counts = [t["passengers_boarded"] for t in trips]
    fares = [t["fare_total_inr"] for t in trips]
    walked_away_counts = [t["passengers_walked_away"] for t in trips]

    avg_wait = mean(wait_times)
    avg_boarded = mean(boarded_counts)
    total_revenue = sum(fares)
    total_walkaways = sum(walked_away_counts)

    # Churn analysis: trips where driver waited > CHURN_RISK_WAIT_MINS vs <= CHURN_RISK_WAIT_MINS
    trips_over_churn = [t for t in trips if t["wait_mins"] >= CHURN_RISK_WAIT_MINS]
    trips_under_churn = [t for t in trips if t["wait_mins"] < CHURN_RISK_WAIT_MINS]

    walkaways_over_churn = sum(t["passengers_walked_away"] for t in trips_over_churn)
    churn_rate_over = (walkaways_over_churn / len(trips_over_churn)) if trips_over_churn else 0.0

    walkaways_under_churn = sum(t["passengers_walked_away"] for t in trips_under_churn)
    churn_rate_under = (walkaways_under_churn / len(trips_under_churn)) if trips_under_churn else 0.0

    # Hourly earning rate comparison
    # Total cycle time = wait_mins + AVG_ONEWAY_TRANSIT_MINS
    def rev_per_hour(trip_subset):
        if not trip_subset:
            return 0.0
        total_rev = sum(t["fare_total_inr"] for t in trip_subset)
        total_time_mins = sum(t["wait_mins"] + AVG_ONEWAY_TRANSIT_MINS for t in trip_subset)
        return (total_rev / total_time_mins) * 60.0

    earning_rate_disciplined = rev_per_hour(trips_under_churn)
    earning_rate_stalled = rev_per_hour(trips_over_churn)

    print("==================================================================")
    print(" NIT JAMSHEDPUR MAIN GATE: E-RICKSHAW DISPATCH OPTIMIZATION TOOL")
    print(" Field Data Informant: Manoj Mahato (Blue E-Rickshaw)")
    print("==================================================================")
    print(f"Total Observed Trips Analyzed : {total_trips}")
    print(f"Average Stand Wait Time       : {avg_wait:.1f} mins")
    print(f"Average Boarded Passengers    : {avg_boarded:.1f} / {MAX_SEAT_CAPACITY}")
    print(f"Total Passenger Walk-Aways    : {total_walkaways}")
    print("------------------------------------------------------------------")
    print(f"Churn When Wait < {CHURN_RISK_WAIT_MINS}m : {churn_rate_under:.2f} walk-aways/trip")
    print(f"Churn When Wait >= {CHURN_RISK_WAIT_MINS}m: {churn_rate_over:.2f} walk-aways/trip (CRITICAL RISK)")
    print(f"Effective Earning Rate (<{CHURN_RISK_WAIT_MINS}m) : Rs {earning_rate_disciplined:.1f}/hr")
    print(f"Effective Earning Rate (>={CHURN_RISK_WAIT_MINS}m): Rs {earning_rate_stalled:.1f}/hr")
    print("------------------------------------------------------------------")
    print("ACTIONABLE RECOMMENDATION FOR MANOJ MAHATO:")
    print(f"  * Strict 6-Minute Rule: Wait up to {TARGET_DISPATCH_WAIT_MINS} mins if demand is trickling.")
    print(f"  * Threshold Trigger: If you reach {MIN_PROFITABLE_PASSENGERS}+ passengers at minute {TARGET_DISPATCH_WAIT_MINS}, DEPART IMMEDIATELY.")
    print(f"  * Never hold past {CHURN_RISK_WAIT_MINS} mins: Waiting for 5/5 capacity past minute {CHURN_RISK_WAIT_MINS}")
    print(f"    causes seated passengers to abandon the vehicle ({churn_rate_over:.1f} lost/trip),")
    print(f"    lowering hourly earnings from Rs {earning_rate_disciplined:.0f}/hr to Rs {earning_rate_stalled:.0f}/hr.")
    print("==================================================================")


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    load_and_analyze(filepath)
