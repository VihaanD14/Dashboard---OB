# RetainAI: Closed-Loop Predictive Workforce Retention Architecture

RetainAI is a privacy-first talent intelligence architecture designed to predict, understand, and neutralize voluntary employee turnover before it occurs.

---

## 1. Deterministic Composite Flight Risk Formula

All flight risk scores ($R \in [0, 100]$) are computed deterministically in Python backend routines; the LLM is strictly confined to qualitative explanations.

$$R = 100 \times \left[ w_{\text{sentiment}} \cdot S_{\text{inv}} + w_{\text{exit}} \cdot E_{\text{term}} + w_{\text{stagnation}} \cdot T_{\text{stag}} \right]$$

### Terms & Parameters

1. **Survey Sentiment Inversion ($S_{\text{inv}}$):**
   $$S_{\text{inv}} = 1 - \frac{\text{mean\_survey\_score} - 1}{4.0}$$
   *Survey scale is 1–5, so the worst mean (1.0) yields full risk ($1.0$), and the best mean (5.0) yields zero risk ($0.0$).*

2. **Exit Velocity Term ($E_{\text{term}}$):**
   $$\text{exit\_velocity} = \frac{\text{exits in trailing 12 months}}{\text{active cohort headcount}}$$
   $$E_{\text{term}} = \min\left(1.0, \frac{\text{exit\_velocity}}{\text{exit\_velocity\_cap}}\right)$$
   *Default `exit_velocity_cap = 0.30` (configurable in `enterprise_settings.json` and editable in Settings).*

3. **Tenure Stagnation Index ($T_{\text{stag}}$):**
   $$T_{\text{stag}} = \min\left(1.0, \frac{\text{months since last promotion}}{\text{stagnation\_cap}}\right)$$
   *Default `stagnation_cap = 24.0` months (configurable).*

4. **Configurable Defaults (`enterprise_settings.json`):**
   - Weights: $w_{\text{sentiment}} = 0.40$, $w_{\text{exit}} = 0.35$, $w_{\text{stagnation}} = 0.25$
   - Risk Bands: Yellow threshold $= 40.0$, Red threshold $= 70.0$
   - Stagnation Cap: $24.0$ months
   - Exit Velocity Cap: $0.30$
   - Salary Formula Constants: Base salary $\$25,000$, per-band increment $\$25,000$, tier multipliers ($0.75$ Junior, $1.00$ Mid, $1.50$ Senior)
   - **Calibration Note:** *"Defaults. Calibrate against the client's actual exits before relying on scores."*

---

## 2. Risk Bands & Labels

- 🟢 **Green (Low Risk):** $R < 40.0$
- 🟡 **Yellow:** `"Early warning (sentiment / stagnation)"` ($40.0 \le R < 70.0$)
- 🔴 **Red:** `"Critical (adverse signals plus real departures)"` ($R \ge 70.0$)

> **Zero-Exit Boundary Rule:**  
> With zero exits in the trailing 12 months, the maximum possible risk score is:  
> $$R_{\max} = 100 \times [0.40 \times 1.0 + 0.35 \times 0.0 + 0.25 \times 1.0] = 65.0$$  
> Because $65.0 < 70.0$, entering the Red band requires actual observed departures.

---

## 3. Stage 6: Intervention Evaluation & ROI Tracker

Stage 6 simplifies intervention evaluation into three transparent cards computed at each 30, 60, and 90-day checkpoint:

### CARD 1: "Did risk really fall?"
$$\text{adjusted\_drop} = (R_{\text{before, treated}} - R_{\text{current, treated}}) - (R_{\text{before, control}} - R_{\text{current, control}})$$
- Shows the treated drop, the comparison drop (*"Comparison team's drop (what would have happened anyway)"*), and the adjusted drop.
- If no control cohort is selected, uses raw treated drop and warns:  
  *⚠️ "Not adjusted for company-wide changes"*.

### CARD 2: "What must we prevent to break even?"
$$\text{breakeven\_exits} = \frac{\text{intervention\_spend}}{\text{replacement\_cost}}$$

### CARD 3: "What did we probably prevent?"
$$\text{prevented\_exits} = \max\left(0, \text{headcount} \times \left(\frac{\text{adjusted\_drop}}{100}\right) \times p_{\text{exit}}\right)$$
*where $p_{\text{exit}} = \text{the treated cohort's trailing-12-month exits / active headcount}$.*

### Synthesis Verdict:
- If $\text{adjusted\_drop} \le 0$: `"No measurable improvement"`
- Else if $\text{prevented\_exits} \ge \text{breakeven\_exits}$: `"Likely pays off"`
- Otherwise: `"Not yet clear - re-check at the next 30/60/90-day point"`
- *Append `"(unadjusted)"` if no control cohort was used.*

### Expander: "Illustrative savings estimate"
- $\text{gross\_savings} = \text{prevented\_exits} \times \text{replacement\_cost}$
- $\text{net\_gain} = \text{gross\_savings} - \text{spend}$
- $\text{roi\_pct} = \frac{\text{net\_gain}}{\text{spend}} \times 100$
- *Caption: "Estimate based on modelled assumptions, not observed outcomes."*

---

## 4. Academic Foundations & Theoretical Provenance

| Academic Theory & Citation | Core Psychological Premise | Direct Implementation in RetainAI |
| :--- | :--- | :--- |
| **Theory of Organizational Equilibrium**<br>March & Simon (1958) | Employees stay when Inducements $\ge$ Contributions. Flight is governed by desirability of movement paired with ease of movement. | Module 4 correlates internal satisfaction degradation with market role level and tenure velocity to model true departure probability. |
| **Intermediate Linkages Model**<br>Mobley, W. H. (1977) | Turnover follows a cognitive path: *Dissatisfaction $\to$ Thoughts of Quitting $\to$ Utility Evaluation $\to$ Search Intentions $\to$ Resignation*. | RetainAI captures friction at the early stages (Thoughts of Quitting / Utility Evaluation), before Job Search and formal resignation, when intervention is still possible. |
| **Job Embeddedness Theory**<br>Mitchell et al. (2001) | Retention is driven by web of ties across Links, Fit, and Sacrifice. | Micro-Pulse Engine questions evaluate team link density and role fit rather than blunt affective happiness. |
| **Cost of Human Turnover Framework**<br>Cascio, W. F. (2000) & SHRM (2022) | Replacement cost extends beyond recruitment: encompasses separation pay, vacancy productivity loss, ramp-up lag, and team contagion. | Formula 3 integrates Cascio's 0.50x–2.00x multiplier range (consistent with Section 3) into all intervention ROI models. |
| **Social Desirability & Common Method Bias**<br>Podsakoff et al. (2012) | Standard surveys trigger defensive response distortions when employees fear surveillance or managerial backlash. | Enforces anonymous aggregate cohort tracking ($n \ge 5$) and indirect behavioral question framing to neutralize bias. |
| **Expectancy Theory of Motivation**<br>Vroom, V. H. (1964) | Effort depends on believing high performance leads to rewards (Instrumentality). Promotion stalls break this cognitive link. | Tenure Stagnation Index (Formula 2) heavily weights employees reaching full penalty at 24 months (configurable). |

---

## Privacy and anti-differencing safeguards

RetainAI strictly complies with the Digital Personal Data Protection Act (DPDP Act 2023):
- **No Individual Scoring:** Never scores or reports on individuals; all outputs are aggregated at cohort level ($k \ge 5$).
- **$k$-Anonymity on Responses:** The $k \ge 5$ threshold is enforced strictly on actual survey responses, not nominal headcount. Cohorts under 5 responses are automatically merged into parent department aggregates.
- **Anti-Differencing Safeguards:** Borderline cohorts ($5 \le n < 10$) display qualitative risk bands (Green/Yellow/Red) rather than exact numbers. Complementary suppression breaks algebraic determinism.
- **Cadence Protection:** Telemetry updates occur on a scheduled quarterly cadence to prevent inferring individual departures from daily roster shifts.
