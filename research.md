# Problem Research & Foundation: NIT Jamshedpur Main Gate E-Rickshaw Dispatch

**Author:** Vivek Paswan (Final-year B.Tech, NIT Jamshedpur)  
**Location:** NIT Jamshedpur Main Gate Stand, Adityapur-Kandra Road, Adityapur, Jharkhand  
**Target Operator:** Manoj Mahato (Blue E-Rickshaw, 4 years operating at NIT JSR Main Gate)  
**Date:** November 17, 2026  

---

## 1. The Problem

Outside NIT Jamshedpur Main Gate on Adityapur-Kandra Road, e-rickshaw drivers like Manoj Mahato operate short shared hops to Adityapur Station and Bistupur.
Passenger arrivals are highly stochastic and concentrated around class/lab dismissal bells, train arrivals, and mess meal timings.
Manoj constantly faces an optimal dispatch dilemma: depart immediately with 2–3 passengers at ₹15–₹20/head or idle at the gate hoping to fill all 5 seats.
Long idle waiting drains battery accessories, risks passenger churn to diesel auto-rickshaws, and cuts daily trip turnover from 14 down to 8 trips.
Conversely, departing prematurely forfeits batch arrivals walking down the campus avenue just 60 to 90 seconds behind.

---

## 2. Existing Solutions & Why They Don't Fit Manoj

### Solution 1: App Aggregators (Ola Auto, Uber Auto, Rapido Auto)
* **High Commission & Negative Unit Economics:** Aggregators charge 20%–25% platform commissions. On a short shared hop of ₹15–₹20 per seat, retaining ₹11–₹15 after platform cuts, mobile data costs, and payout processing renders the trip economically unviable.
* **Mismatched Ride-Hailing Paradigm:** NIT students exiting through the main gate turnstile do not book individual on-demand autos on their phones for a 1.8 km hop to Adityapur station. They look for the first moving vehicle, step in, and pay cash or UPI on deboarding.
* **Inability to Support Dynamic Pooling:** App algorithms enforce dedicated single-booking trips rather than the continuous seat-by-seat pooling and cash collection that drivers rely on along the Adityapur-Kandra industrial corridor.

### Solution 2: Fixed-Schedule Campus Shuttles / Rigid Timetables
* **Decentralized Owner-Driver Reality:** E-rickshaws at NIT gate are independently owned and operated by local unorganized drivers with zero central dispatch or institutional subsidy to absorb slack time.
* **Severe Traffic Variance on Adityapur-Kandra Road:** Rail-crossing closures at Adityapur station, heavy truck movements from Tata Growth Shop/Adityapur Industrial Area, and road-widening work cause trip transit times to fluctuate unpredictably between 6 and 22 minutes, making rigid clock-based departure times completely unworkable.
* **Inelasticity to Real Academic Cycles:** Static bus timetables miss stochastic campus surges—such as a metallurgy workshop dismissing 40 students 20 minutes early, or exam day dispersal shifts.

---

## 3. Real Sources Read & Practical Notes

### Source 1: Optimal Stopping Theory & Bulk-Service Queues ($M/G^k/1$ Batch Dispatch Models)
* *Reference:* Neuts, M. F. (1967), "A General Class of Bulk Queues with Poisson Input"; Powell, W. B. & Humblet, P. (1986), "The Bulk Service Queue with a General Control Policy".
* **Practical Note 1:** Bulk-service queuing models analyze dispatch decisions for a server with maximum capacity $K$ balancing passenger holding delay costs against vehicle departure costs under batch arrivals.
* **Practical Note 2:** Powell & Humblet establish that the optimal policy under general holding and dispatch costs is a dual-threshold $(M, T)$ policy: depart when $m \ge M$ passengers have boarded, or unconditionally dispatch once waiting time exceeds cutoff $T$.
* **Practical Note 3 (Application to Manoj):** Instead of Manoj intuitively holding out for full capacity ($K=5$), the model provides theoretical justification for an empirical cutoff time $T$ and minimum threshold $M=3$, preventing costly over-waiting.

### Source 2: NITI Aayog & WRI India — E-Rickshaw Economics in Tier-2 Indian Urban Clusters
* *Reference:* NITI Aayog / World Resources Institute (WRI) India (2020–2022), "Evaluating Electric First-and-Last-Mile Connectivity in Tier-2 Industrial Cities".
* **Practical Note 1:** Field data shows that 60%–70% of an e-rickshaw driver's net daily operating surplus in tier-2 railway/campus hubs is driven by total trip turnover per battery charge cycle rather than maximizing single-trip passenger fill factor.
* **Practical Note 2:** Excessive idle curb-waiting with auxiliary loads active (lighting, mobile chargers, controller draw) degrades usable daily battery range by 8–12% without generating passenger seat kilometers.
* **Practical Note 3 (Application to Manoj):** Manoj's blue e-rickshaw relies on a 48V 100Ah lead-acid pack providing roughly 65–75 km effective daily range; optimizing for trip count and fast turnaround yields higher net daily income than idling for marginal 4th/5th passengers.

