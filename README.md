# NIT Jamshedpur Main Gate E-Rickshaw Dispatch Optimizer

**Location:** E-Rickshaw Stand, NIT Jamshedpur Main Gate (Adityapur-Kandra Road, Jamshedpur, Jharkhand)  
**Target Operator / Informant:** Manoj Mahato (Blue Mayuri E-Rickshaw, 4 years operating at NIT Gate)  
**Author:** Vivek Paswan (Final-year B.Tech, NIT Jamshedpur)  
**Date:** November 17, 2026  

---

## Overview

At the main gate of NIT Jamshedpur, e-rickshaws provide essential first-and-last-mile connectivity between campus, Adityapur Railway Station (~1.8 km), and Bistupur (~5.2 km). E-rickshaw drivers routinely face an optimal stopping dilemma: depart with 2–3 passengers (₹30–₹45) or wait at the gate curb hoping to fill all 5 seats (₹75–₹100). 

Based on field observations and conversations with Manoj Mahato, holding past **8 minutes** does not just burn idle time and auxiliary battery—it triggers severe **passenger churn**, as seated students abandon the stalled vehicle to catch passing diesel Vikram autos. This tool analyzes 24 empirical dispatch cycles, quantifies the exact churn threshold, and provides a clear, actionable dispatch policy for Manoj to maximize daily earnings.

---

## Quickstart & Execution

This project uses **zero external dependencies** and runs entirely on the standard Python 3 runtime (`csv`, `statistics`, `sys`).

### Run the Optimizer:
```bash
python3 main.py data.csv
```

### Run with Help Flag:
```bash
python3 main.py --help
```

---

## Actual Terminal Output

```text
$ python3 main.py data.csv
========================================================================
 NIT JAMSHEDPUR MAIN GATE: E-RICKSHAW DISPATCH OPTIMIZATION TOOL
 Field Informant: Manoj Mahato (Blue E-Rickshaw, 4 Years at Stand)
 Target Route   : NIT Main Gate -> Adityapur Station / Bistupur
========================================================================
 Dataset Source                 : data.csv
 Valid Trips Processed          : 24
 Average Stand Wait Time        : 8.7 minutes
 Average Boarded Passengers     : 3.4 / 5 seats
 Total Recorded Passenger Churn : 16 passengers lost
------------------------------------------------------------------------
 CHURN RISK & DISPATCH THRESHOLD METRICS:
  • Wait < 8 mins (Disciplined)   : 0.00 walk-aways/trip | Earning: Rs 228.0/hr
  • Wait >= 8 mins (Stalled for 5/5): 1.60 walk-aways/trip | Earning: Rs 102.0/hr
------------------------------------------------------------------------
 CONCRETE DISPATCH RULE FOR MANOJ MAHATO:
  1. Capped Wait Target: Set a hard timer for 6 minutes upon arriving at the stand.
  2. Threshold Departure: If at minute 6 you have 3+ passengers, DEPART IMMEDIATELY.
  3. Avoid the 8-Minute Trap: Holding for a 4th or 5th passenger past 8 minutes
     causes seated students to deboard (1.6 lost/trip to passing autos),
     collapsing net hourly earnings from Rs 228/hr down to Rs 102/hr.
========================================================================
```

---

## What This Tool Gets Wrong (Honest Limitations & Edge Cases)

While the mathematical threshold policy offers immediate operational value, real-world conditions at the NIT Jamshedpur gate introduce several edge cases this simple heuristic does not account for:

1. **Weather Shocks (Sudden Monsoon Downpours):**  
   During sudden heavy rain, passenger price sensitivity and churn collapse to zero. Students will pack 6 inside the e-rickshaw and wait patiently rather than step out onto flooded Adityapur-Kandra Road. The 8-minute churn penalty does not apply under adverse weather.
2. **Asymmetric Evening Return Loads at Adityapur Station:**  
   The model evaluates trips initiating from the NIT Main Gate. However, between 18:30 and 20:30, arriving trains (e.g., Tatanagar passenger shuttles, Steel Express connections) flood Adityapur Station with inbound passengers. Running an underfilled 2-passenger rickshaw out of NIT gate at 18:40 is actually optimal because the return leg from the station guarantees an instantaneous 5-passenger load at full fare.
3. **Battery State of Charge (SoC) Non-Linearities:**  
   The tool assumes vehicle speed and transit time are invariant. In reality, Manoj's 48V lead-acid battery pack suffers voltage sag when State of Charge drops below 25% (typically after 16:00). At low SoC, carrying 5 heavy adults up the slight incline towards Adityapur flyover causes severe motor strain, making 3–4 passenger loads mechanically preferable regardless of wait time.
4. **Driver Social Dynamics & Stand Queue Etiquette:**  
   E-rickshaws queue in a line-of-first-arrival outside the gate. If Manoj is #3 in the queue, he cannot unilaterally decide to depart at minute 6 if #1 and #2 are blocking the narrow curb lane without causing conflict among fellow drivers.

---

## 3-Minute Walkthrough Video Demo

- **Loom / Screen Recording Link:** `[DEMO LINK PLACEHOLDER - Insert 3-min walkthrough video link here]`
- *The demo walkthrough covers: (1) physical location context outside NIT Main Gate, (2) editing thresholds live in `main.py`, (3) feeding corrupted rows to showcase graceful error recovery, and (4) explaining the churn cutoff recommendation.*

---

## Repository Structure

```text
.
├── README.md               # Overview, quickstart, real output, and honest limitations
├── research.md             # 5-line problem statement, critique of existing tech, paper references
├── fieldwork.md            # Gate observation notes, photos reference, dialogue with Manoj
├── data.csv                # 24 raw recorded trips with timestamps, wait times, fares, and churn
├── main.py                 # Core analysis script with tunable constants and error handling
├── reflection.md           # Engineering reflections on initial assumptions, cuts, and AI usage
├── photos/                 # Timestamped photographic documentation
│   ├── gate_stand_wide.jpg
│   └── field_notes_tally.jpg
└── ai-chats/               # Exported AI prompt logs and architectural discussion
```
