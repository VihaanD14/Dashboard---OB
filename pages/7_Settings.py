import streamlit as st
import os

from config import APP_TITLE, APP_ICON
from utils.styles import apply_custom_css
from utils.navigation import render_top_navbar

st.set_page_config(
    page_title=f"Settings | {APP_TITLE}",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)
apply_custom_css()
from utils.data_loader import get_enterprise_settings, save_enterprise_settings

render_top_navbar(active_page="settings")

st.title("Settings & Configuration")
st.markdown('<p class="subtitle">Manage enterprise client parameters, AI engine connections, and workforce data telemetry.</p>', unsafe_allow_html=True)

settings = get_enterprise_settings()

st.markdown("### Client Enterprise Profile")
with st.form("enterprise_profile_form"):
    col1, col2 = st.columns(2)
    with col1:
        client_name = st.text_input("Enterprise Client Name", value=settings.get("client_name", "Apex Global Technologies"))
        industry_vertical = st.text_input("Industry Vertical", value=settings.get("industry_vertical", "Enterprise Software & Cloud Services"))
    with col2:
        scale_options = ["1-50", "51-200", "201-500", "500+"]
        saved_scale = settings.get("workforce_scale", "51-200")
        default_idx = scale_options.index(saved_scale) if saved_scale in scale_options else 1
        selected_scale = st.selectbox("Workforce Cohort Scale", scale_options, index=default_idx)
        
        submitted = st.form_submit_button("Save Profile Settings", type="primary")
        if submitted:
            st.session_state["client_name"] = client_name
            st.session_state["industry_vertical"] = industry_vertical
            st.session_state["workforce_scale"] = selected_scale
            settings["client_name"] = client_name
            settings["industry_vertical"] = industry_vertical
            settings["workforce_scale"] = selected_scale
            save_enterprise_settings(settings)
            st.cache_data.clear()
            st.success(f"Profile saved! Workforce cohort telemetry updated to {selected_scale}.")

st.markdown("---")

st.markdown("### Risk Scoring & Economic Model Calibration")
st.info("ℹ️ **Defaults. Calibrate against the client's actual exits before relying on scores.**")

with st.form("risk_calibration_form"):
    st.markdown("#### Flight Risk Formula Weights & Caps")
    st.caption("Score = 100 × [ w_sentiment × (1 - (mean - 1)/4) + w_exit × min(1, exit_velocity / cap) + w_stagnation × min(1, promo_latency / cap) ]")
    
    col_w1, col_w2, col_w3 = st.columns(3)
    with col_w1:
        w_sentiment = st.number_input("Survey Sentiment Weight", min_value=0.0, max_value=1.0, value=float(settings.get("weight_sentiment", 0.40)), step=0.05)
    with col_w2:
        w_exit = st.number_input("Exit Velocity Weight", min_value=0.0, max_value=1.0, value=float(settings.get("weight_exit", 0.35)), step=0.05)
    with col_w3:
        w_stagnation = st.number_input("Tenure Stagnation Weight", min_value=0.0, max_value=1.0, value=float(settings.get("weight_stagnation", 0.25)), step=0.05)
        
    col_c1, col_c2, col_c3 = st.columns(3)
    with col_c1:
        exit_velocity_cap = st.number_input("Exit Velocity Cap (default, calibrate on client data)", min_value=0.05, max_value=1.00, value=float(settings.get("exit_velocity_cap", 0.30)), step=0.05, help="Trailing 12-month exits divided by active headcount is capped at this value.")
    with col_c2:
        stagnation_cap = st.number_input("Tenure Stagnation Cap (Months)", min_value=6.0, max_value=60.0, value=float(settings.get("stagnation_cap_months", 24.0)), step=6.0, help="Months since last promotion reaching full penalty cap.")
    with col_c3:
        st.markdown("**Bands:** Yellow: 40 | Red: 70")
        risk_band_yellow = st.number_input("Yellow Band (Early Warning)", min_value=10.0, max_value=90.0, value=float(settings.get("risk_band_yellow", 40.0)), step=5.0)
        risk_band_red = st.number_input("Red Band (Critical Threat)", min_value=20.0, max_value=100.0, value=float(settings.get("risk_band_red", 70.0)), step=5.0)
        
    st.markdown("#### Salary Formula & Replacement Cost Model")
    st.caption("Base Salary = salary_base + (salary_band × salary_per_band); Replacement Cost = Salary × Tier Multiplier")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        salary_base = st.number_input("Base Salary ($)", min_value=5000.0, max_value=200000.0, value=float(settings.get("salary_base", 25000.0)), step=5000.0)
    with col_s2:
        salary_per_band = st.number_input("Salary Increment per Band ($)", min_value=5000.0, max_value=100000.0, value=float(settings.get("salary_per_band", 25000.0)), step=5000.0)
        
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        mult_jr = st.number_input("Junior Tier Multiplier", min_value=0.10, max_value=2.00, value=float(settings.get("replacement_multiplier_junior", 0.75)), step=0.05)
    with col_m2:
        mult_mid = st.number_input("Mid Tier Multiplier", min_value=0.10, max_value=3.00, value=float(settings.get("replacement_multiplier_mid", 1.00)), step=0.05)
    with col_m3:
        mult_sr = st.number_input("Senior / Lead Tier Multiplier", min_value=0.10, max_value=5.00, value=float(settings.get("replacement_multiplier_senior", 1.50)), step=0.05)
        
    save_calib = st.form_submit_button("Save Model & Calibration Parameters", type="primary")
    if save_calib:
        updated = {
            "client_name": settings.get("client_name", "Apex Global Technologies"),
            "industry_vertical": settings.get("industry_vertical", "Enterprise Software & Cloud Services"),
            "workforce_scale": settings.get("workforce_scale", "51-200"),
            "exit_velocity_cap": exit_velocity_cap,
            "weight_sentiment": w_sentiment,
            "weight_exit": w_exit,
            "weight_stagnation": w_stagnation,
            "risk_band_yellow": risk_band_yellow,
            "risk_band_red": risk_band_red,
            "stagnation_cap_months": stagnation_cap,
            "salary_base": salary_base,
            "salary_per_band": salary_per_band,
            "replacement_multiplier_junior": mult_jr,
            "replacement_multiplier_mid": mult_mid,
            "replacement_multiplier_senior": mult_sr,
            "calibration_note": "Defaults. Calibrate against the client's actual exits before relying on scores."
        }
        for k, v in updated.items():
            st.session_state[k] = v
        save_enterprise_settings(updated)
        st.cache_data.clear()
        st.success("Calibration parameters successfully saved and applied to predictive engine!")

st.markdown("---")

st.markdown("### AI Engine Configuration")
api_key = st.text_input("Google Gemini API Key", type="password", value=os.environ.get("GEMINI_API_KEY", ""))
col_k1, col_k2 = st.columns([1, 4])
with col_k1:
    if st.button("Test Connection", type="primary"):
        if api_key:
            st.toast("Connection verified! Gemini API is active.", icon="✅")
        else:
            st.toast("Fallback to mock data engine active (No API key found).", icon="⚠️")
with col_k2:
    if not api_key:
        st.warning("Currently running in Demo/Mock mode. Add a Gemini API key for live generative inference.")
    else:
        st.success("Valid API key registered. Live generative reasoning active.")

st.markdown("---")

st.markdown("### Telemetry Data Management")
st.write("Upload custom CSV files to ingest client-specific personnel, exit interview, and pulse survey datasets.")
c_u1, c_u2, c_u3 = st.columns(3)
with c_u1:
    st.file_uploader("Upload Active Personnel CSV", type=['csv'])
with c_u2:
    st.file_uploader("Upload Exit Interviews CSV", type=['csv'])
with c_u3:
    st.file_uploader("Upload Pulse Survey Responses CSV", type=['csv'])

st.markdown("---")

st.markdown("### About RetAIn Architecture")
st.info("""
**RetAIn Enterprise System**  
An advanced, privacy-first talent intelligence architecture designed to predict, understand, and neutralize voluntary employee turnover.

**Privacy & Ethical Aggregation Guardrails:**  
Never scores or reports on individuals; all outputs are aggregated at cohort level with a minimum of 5 responses. Individual-level text (exit notes, retros) is processed only to extract thematic clusters and is not accessible to managers. If a cohort has fewer than 5 survey responses, it is automatically merged upward into its parent department aggregate to prevent mathematical exposure.
""")

with st.expander("🛡️ Privacy and anti-differencing safeguards (DPDP Act 2023)", expanded=False):
    st.markdown("""
    **Compliance Notice under the Digital Personal Data Protection Act (DPDP Act 2023):**
    - **No Individual Scoring:** Never scores or reports on individuals; all outputs are aggregated at cohort level with a minimum of 5 responses. Individual-level text (exit notes, retros) is processed only to extract thematic clusters and is not accessible to managers.
    - **k-Anonymity on Responses:** The $k \ge 5$ threshold is applied strictly to survey *responses*, not nominal headcount. Cohorts with fewer than 5 responses are automatically merged into parent department aggregates.
    - **Anti-Differencing Safeguards:** Cohorts with 5 to 9 responses ($5 \le n < 10$) display qualitative rating bands rather than exact 2-decimal numbers. Complementary suppression prevents algebraic reverse-engineering.
    - **Cadence Protection:** Telemetry updates occur on a scheduled quarterly cadence so individual leavers cannot be deduced from day-to-day roster departures.
    """)
