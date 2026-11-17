# Engineering Reflection & Post-Mortem

**Author:** Vivek Paswan (Final-year B.Tech, NIT Jamshedpur)  
**Location:** NIT Jamshedpur Main Gate, Adityapur, Jharkhand  
**Date:** November 17, 2026  
**Assignment:** 24-Hour Take-Home Engineering Challenge  

---

> [!NOTE]
> The sections below contain guided prompts and are explicitly reserved for personal, candid reflection written directly by Vivek Paswan to ensure authentic human perspective.

---

### 1. What I Got Wrong at the Start (Naive Assumptions vs Ground Reality)
*[WRITE THIS MANUALLY WITHOUT AI]*

*Guiding Prompts:*
- What did you assume when sitting in your hostel room or looking at queueing theory formulas before stepping out to the gate?
- How did your initial mental model of "e-rickshaws must always wait for 5 passengers to maximize revenue" get dismantled by Manoj Mahato?
- Did you expect passenger arrival to be a smooth Poisson process, or did campus bells / train schedules make it hyper-batched?

```text
[WRITE YOUR 4-6 SENTENCE HONEST REFLECTION HERE]
Example angle: I assumed e-rickshaw drivers were simply losing money due to impatience and that waiting for 5 passengers was always mathematically superior. Standing at the gate with Manoj for just 20 minutes proved the exact opposite: seated students have near-zero patience when competitor autos pass by, making waiting past 8 minutes a net-negative gamble.
```

---

### 2. What Features & Complexity I Deliberately Cut (Scope Discipline)
*[WRITE THIS MANUALLY WITHOUT AI]*

*Guiding Prompts:*
- What complex features (e.g., dynamic pricing APIs, GPS tracking, complex Markov decision processes, neural networks, mobile app UI) were you tempted to build initially?
- Why was it critical to eliminate heavy libraries (Pandas, NumPy, Scikit-learn) and stick purely to Python 3 standard library?
- How did cutting scope ensure the script could run reliably on any system in under 1 second without dependency hell?

```text
[WRITE YOUR 4-6 SENTENCE HONEST REFLECTION HERE]
Example angle: I initially thought about writing an interactive Streamlit dashboard or simulating battery degradation with differential equations. I realized that Manoj needs a concrete rule of thumb he can remember on a wristwatch, not a web dashboard. Cutting dependencies down to Python standard library kept the focus 100% on data integrity and clear business logic.
```

---

### 3. Where AI Tools Genuinely Accelerated My Work
*[WRITE THIS MANUALLY WITHOUT AI]*

*Guiding Prompts:*
- Where did the LLM save you tedious typing or boilerplate work?
- How did AI help structure the queueing literature research (Powell & Humblet bulk queue references) and clean terminal formatting?
- How did paired collaboration help you articulate the transition from raw field notes to structured CSV schema?

```text
[WRITE YOUR 3-5 SENTENCE HONEST REFLECTION HERE]
Example angle: AI was fantastic at rapidly scaffolding the data ingestion pipeline, generating clean CLI tabular formatting, and synthesizing theoretical queueing papers into concise operational notes.
```

---

### 4. Where AI Overcomplicated Things & Had to be Reined In
*[WRITE THIS MANUALLY WITHOUT AI]*

*Guiding Prompts:*
- What corporate jargon, buzzwords, or unnecessary abstractions did the AI initially try to inject?
- Did the AI try to suggest unrealistic solutions (like having unorganized e-rickshaw drivers install IoT sensors, RFID tags, or micro-payment smart contracts)?
- How did you anchor the problem back to the dusty Adityapur-Kandra curb, Manoj's 48V battery, and cash/UPI reality?

```text
[WRITE YOUR 3-5 SENTENCE HONEST REFLECTION HERE]
Example angle: Left unconstrained, AI tends to suggest over-engineered enterprise architectures like real-time Kafka streams or predictive reinforcement learning for what is fundamentally a two-parameter threshold stopping problem. I had to repeatedly force the focus back to Manoj’s real physical constraints: a 48V lead-acid battery, passing diesel autos, and angry students deboarding after 8 minutes.
```

---

### 5. Final Takeaway as an NIT Jamshedpur Engineer
*[WRITE THIS MANUALLY WITHOUT AI]*

```text
[WRITE YOUR FINAL 2-3 SENTENCE SUMMARY HERE]
```
