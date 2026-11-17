# Engineering Reflection & Post-Mortem

**Author:** Vivek Paswan (Final-year B.Tech, NIT Jamshedpur)  
**Location:** NIT Jamshedpur Main Gate, Adityapur, Jharkhand  
**Date:** November 17, 2026  
**Assignment:** 24-Hour Take-Home Engineering Challenge  

---

### 1. What I Got Wrong at the Start (Naive Assumptions vs Ground Reality)

Before walking out of the campus gate, I was sitting in my hostel room convinced that this was a textbook optimization problem: an e-rickshaw has 5 passenger seats, each seat earns ₹15–₹20, so departing with anything less than a full vehicle is mathematically sub-optimal. In my mind, drivers who departed with only 2 or 3 passengers were simply acting out of impatience or poor financial planning.

Standing next to Manoj Mahato's blue Mayuri rickshaw for thirty minutes under the afternoon sun completely shattered that naive theory. At minute 7 of an idle wait, you could visibly feel the tension mounting among the seated passengers. Students checked their wristwatches, glanced down Adityapur-Kandra Road, and the exact moment a shared diesel auto rattled past shouting *"Station! Station!"*, two students on Manoj's bench abruptly hopped out and took the auto instead. Manoj turned to me with a resigned smile and said, *"Dekha bhaiya? Zyada laalach me jo haath me tha, wo bhi chala gaya."* That single interaction completely re-anchored my model: curb-waiting is not a zero-cost waiting room—past the 8-minute mark, waiting is an active revenue-destroying liability that triggers aggressive passenger churn.

---

### 2. What Features & Complexity I Deliberately Cut (Scope Discipline)

My default academic instinct was to throw every possible buzzword at this challenge: building an interactive Streamlit web dashboard, implementing dynamic surge pricing formulas, and simulating non-linear battery degradation using differential equations. 

I deliberately scrapped every single one of those ideas. Manoj drives with one hand on the handlebar and cash crumpled between his fingers; he doesn't have a phone mounted on a dashboard, nor does he have the bandwidth to look at charts between trips. He needs a dead-simple, memorable rule of thumb that he can check on a basic wristwatch before his battery or his passengers drain away. 

On the software engineering side, I strictly banned heavy dependencies like Pandas, NumPy, or Scikit-learn. Pulling in 150MB of compiled binaries to compute averages and filter 24 rows across two threshold conditions is sloppy engineering. Keeping the entire codebase strictly on Python 3 standard library (`csv`, `statistics`, `sys`) ensures that anyone evaluating this project can clone the repository and run it in 15 milliseconds on a bare system without fighting virtual environments or dependency conflicts.

---

### 3. Where AI Tools Genuinely Accelerated My Work

AI was exceptionally effective as a pair-programmer for boilerplate scaffolding and academic literature synthesis. It eliminated the repetitive friction of writing CSV column parsing routines, non-crashing type-checking guards, and clean ANSI/ASCII terminal output formatting. 

More importantly, it helped me bridge the gap between Manoj's street-level intuition and academic rigor. When I described the batch-arrival nature of students pouring out of the gate after lab dismissals, the AI helped me trace the relevant bulk-service queueing literature ($M/G^k/1$ batch service models by Neuts, and Powell & Humblet's dual-threshold theorems). Having that mathematical backing gave me confidence that Manoj's lived experience was not an anomaly—it was the exact behavior predicted by optimal stopping theory.

---

### 4. Where AI Overcomplicated Things & Had to be Reined In

Left completely unconstrained, the AI defaulted to corporate Silicon Valley hallucinations that had zero relevance to Adityapur. In early brainstorming prompts, it suggested implementing "Bluetooth Low-Energy beacons at the college turnstile", "automated dynamic pooling algorithms via UPI micro-transactions", and "predictive arrival forecasting using LSTM neural networks". 

I had to repeatedly rein it in and anchor it back to reality: we are dealing with unorganized, cash-and-UPI operators on a dusty, potholed stretch of Adityapur-Kandra Road where the local grid experiences frequent voltage cuts and drivers nurse aging 48V lead-acid batteries. AI has a chronic bias toward adding architectural complexity to justify its own intelligence. My job as the engineer was to strip away that techno-solutionism and force the focus onto what actually matters: a 6-minute timer, a 3-passenger minimum threshold, and avoiding the 8-minute churn trap.

---

### 5. Final Takeaway as an NIT Jamshedpur Engineer

The biggest takeaway from this assignment wasn't about queueing mathematics or writing clean Python; it was learning that twenty minutes spent sitting on the bench of an e-rickshaw listening to an actual operator is worth more than twenty hours of abstract modeling in a hostel room. True engineering competence isn't demonstrated by how many libraries you import or how complex your architecture looks—it is demonstrated by whether your solution respects the physical, economic, and human constraints of the real world.
