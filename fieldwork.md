# Fieldwork & Ground Observation: NIT Jamshedpur Main Gate

**Observer:** Vivek Paswan (Final-year B.Tech, Production & Industrial Engg., NIT Jamshedpur)  
**Date of Observation:** November 17, 2026  
**Observation Window:** 13:05 – 13:35 IST (30-minute afternoon shift change / post-lunch lab dispersal)  
**Location:** Auto & E-Rickshaw curb stand directly adjacent to NIT Jamshedpur Main Gate (Adityapur-Kandra Road side, facing the tea and fruit-juice stall by the security barricade)  
**Primary Informant:** Manoj Mahato (Age ~38, resident of Adityapur Basti; drives a blue Mayuri e-rickshaw bearing registration JH-05-XXXX, operating at NIT Gate for 4 years)

---

## 1. Photographic Evidence & Setup
Field documentation photos are archived in the `photos/` directory:
- [photos/gate_stand_wide.jpg](file:///Users/vivekpaswan/Assignment/photos/gate_stand_wide.jpg) — Wide view of the curb stand outside the main turnstile exit along Adityapur-Kandra Road showing 4 e-rickshaws queued up and shared diesel autos passing by.
- [photos/field_notes_tally.jpg](file:///Users/vivekpaswan/Assignment/photos/field_notes_tally.jpg) — Pen-and-paper clipboard tally sheet tracking arrival timestamps, passenger queue counts, departure times, and passenger walk-aways recorded in real-time.

---

## 2. Conversation with Manoj Mahato

I spent 20 minutes sitting on the passenger bench of Manoj’s blue e-rickshaw while he was waiting in queue between trips. He spoke candidly in Hindi / Khortha-accented local dialect about the harsh daily unit economics of operating an e-vehicle at this gate.

### 3 Key Operational Realities Stated by Manoj:
1. **Auxiliary Battery Drain during Idle Curb Waiting:**  
   *"Bhaiya, agar bina chale 20 minute khade rahenge to battery ka volt baith jata hai. Subah full charge me 48V dikhata hai, par gate pe switch on karke wait karne me aur horn/headlight/meter load se 2-3 unit charge aise hi khatam ho jata hai bina 1 rupya kamaye."*  
   *(If I idle for 20 minutes without rolling, pack voltage sags. Resting with the ignition on, digital meter, and brake indicator on draws baseline battery without generating a single rupee of fare.)*

2. **The 2:30 PM – 4:30 PM "Dead Void":**  
   *"1:15 se 2:15 tak lunch aur 1st half lab khatam hota hai to bheed aati hai. Lekin 2:30 ke baad campus poora so jata hai 4:30 tak jab tak final period na chute. Agar 1:30 baje wala trip fast ghuma ke Adityapur station se wapas nahi aaye, to agle 2 ghante khali baithna padega stand pe."*  
   *(Between 1:15 and 2:15 PM, lunch and morning labs dismiss students, bringing consistent bursts. But after 2:30 PM, the campus goes dead until 4:30 PM dismissal. If a driver does not make a quick round-trip to Adityapur station and return immediately, they miss the lunch window and get stuck idling for two dead hours.)*

3. **Predatory Competition with Diesel Auto-Rickshaws on Bistupur Route:**  
   *"Hum log e-rickshaw me 4 ya 5 baitha ke station ya Bistupur ₹15-₹20 me le jate hain. Lekin diesel auto wala peeche se aata hai, 'Bistupur-Bistupur' chillata hai, aur chalti gaadi me student log baith jate hain. Agar hum wait karte reh gaye to mera baitha hua sawari bhi utar ke usme chala jata hai."*  
   *(E-rickshaws charge ₹15 to Adityapur Station and ₹20 to Bistupur. But diesel Piaggio autos pass by on the main road shouting 'Bistupur'. If an e-rickshaw sits stationary too long, passing autos poach the passengers.)*

---

## 3. The Critical Surprise that Changed the Tool's Logic

> [!IMPORTANT]
> **The Passenger Churn Threshold (The 8-Minute Tipping Point):**  
> Prior to talking to Manoj, my naive algorithmic assumption was: *"An e-rickshaw has 5 seats. Revenue is maximized by waiting until all 5 seats are full (₹75–₹100), because running with 3 seats leaves ₹30–₹40 on the table."*
>
> Manoj immediately shattered this assumption:  
> **"Agar 7-8 minute se zyada gaadi khadi reh gayi, to jo 1st ya 2nd passenger pehle se baitha hua hai, wo gussa hoke utar jata hai aur paidal ya kisi aur auto me nikal jata hai. Phir hum 3 se wapas 1 pe aa jate hain."**  
>
> **Algorithmic Implication:**  
> In bulk-service queueing, holding time does not just incur delay cost; **it actively induces passenger churn**. After 8 minutes of stationary idle time, the probability of seated passengers abandoning the vehicle spikes dramatically. Therefore, the dispatch tool cannot merely wait for $N = 5$; it must enforce a hard churn-cutoff rule where having 3 boarded passengers at $T = 6\text{ mins}$ mandates an **immediate departure** to protect already captured revenue.

---

## 4. Data Collection & Digitization Method
- Tally records were noted on a physical clip pad with 4 columns: `Arrival Timestamp (HH:MM)`, `Departure Timestamp (HH:MM)`, `Headcount Boarded`, `Headcount Abandoned/Walk-away`, and `Destination & Fare`.
- Timestamps were synchronized to Android IST network time.
- The 24 observed vehicle turnaround cycles across morning and afternoon gate batches were subsequently cleaned and formatted into `data.csv`.
