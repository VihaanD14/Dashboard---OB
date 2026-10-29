import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import json
import os
from utils.data_loader import load_employees, get_segment_metrics, get_enterprise_settings

from config import APP_TITLE, APP_ICON, COLORS, DEPARTMENTS
from utils.styles import apply_custom_css
from utils.navigation import render_top_navbar

st.set_page_config(
    page_title=f"Intervention Tracker | {APP_TITLE}",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)
apply_custom_css()
render_top_navbar(active_page="tracker")

st.title("Intervention Tracker")
st.markdown('<p class="subtitle">Evaluate the operational effectiveness and financial ROI of retention actions over time.</p>', unsafe_allow_html=True)

settings = get_enterprise_settings()
salary_base = float(settings.get("salary_base", 25000.0))
salary_per_band = float(settings.get("salary_per_band", 25000.0))
mult_jr = float(settings.get("replacement_multiplier_junior", 0.75))
mult_mid = float(settings.get("replacement_multiplier_mid", 1.00))
mult_sr = float(settings.get("replacement_multiplier_senior", 1.50))

INTERVENTIONS_FILE = "data/interventions.json"

def load_interventions():
    if os.path.exists(INTERVENTIONS_FILE):
        with open(INTERVENTIONS_FILE, "r") as f:
            data = json.load(f)
            for item in data:
                item['start_date'] = pd.to_datetime(item['start_date'])
            return data
    return [
        {
            "name": "Mandatory Bi-Weekly 1-on-1s",
            "description": "Managers must schedule structured 1-on-1s with career roadmapping.",
            "segment": "Engineering - Junior",
            "start_date": datetime.now() - timedelta(days=60),
            "category": "Quick Win",
            "cost": 30000,
            "status": "Active",
            "risk_before": 92,
            "risk_checkpoints": {
                "30-Day Checkpoint": 86,
                "60-Day Checkpoint": 80,
                "90-Day Checkpoint": 76
            },
            "control_checkpoints": {
                "30-Day Checkpoint": 53,
                "60-Day Checkpoint": 51,
                "90-Day Checkpoint": 50
            },
            "control_segment": "Engineering - Senior",
            "control_before": 55,
            "risk_current": 80,
        },
        {
            "name": "Sales Comp Review Task Force",
            "description": "Reviewing commission accelerator structures and territory quotas.",
            "segment": "Sales - Mid",
            "start_date": datetime.now() - timedelta(days=30),
            "category": "Strategic Investment",
            "cost": 15000,
            "status": "In Progress",
            "risk_before": 65,
            "risk_checkpoints": {
                "30-Day Checkpoint": 65,
                "60-Day Checkpoint": 61,
                "90-Day Checkpoint": 58
            },
            "control_checkpoints": {
                "30-Day Checkpoint": 48,
                "60-Day Checkpoint": 47,
                "90-Day Checkpoint": 46
            },
            "control_segment": "Sales - Senior",
            "control_before": 50,
            "risk_current": 65,
        }
    ]

def save_interventions(data):
    save_data = []
    for item in data:
        new_item = item.copy()
        new_item['start_date'] = new_item['start_date'].isoformat() if hasattr(new_item['start_date'], 'isoformat') else str(new_item['start_date'])
        save_data.append(new_item)
    with open(INTERVENTIONS_FILE, "w") as f:
        json.dump(save_data, f, indent=4)

if 'interventions' not in st.session_state:
    st.session_state['interventions'] = load_interventions()

# SECTION 1: Log New Retention Action
with st.expander("➕ Log New Retention Intervention", expanded=False):
    with st.form("new_intervention"):
        c1, c2 = st.columns(2)
        name = c1.text_input("Intervention Initiative Name")
        segment = c2.selectbox("Target Workforce Segment", ["All"] + DEPARTMENTS)
        desc = st.text_area("Operational Description")
        
        c3, c4, c5 = st.columns(3)
        start_date = c3.date_input("Start Date")
        category = c4.selectbox("Strategy Category", ["Quick Win", "Strategic Investment", "Nice-to-Have", "Avoid"])
        cost = c5.number_input("Budget Allocated ($)", min_value=0, value=10000, step=1000)
        
        submitted = st.form_submit_button("Log Intervention", type="primary")
        if submitted and name:
            st.session_state['interventions'].append({
                "name": name,
                "description": desc,
                "segment": segment,
                "start_date": pd.to_datetime(start_date),
                "category": category,
                "cost": cost,
                "status": "Planned",
                "risk_before": 70,
                "risk_checkpoints": {
                    "30-Day Checkpoint": 67,
                    "60-Day Checkpoint": 64,
                    "90-Day Checkpoint": 60
                },
                "control_checkpoints": {
                    "30-Day Checkpoint": 50,
                    "60-Day Checkpoint": 49,
                    "90-Day Checkpoint": 48
                },
                "control_segment": "Operations - Senior",
                "control_before": 52,
                "risk_current": 70
            })
            save_interventions(st.session_state['interventions'])
            st.toast("Intervention logged successfully!", icon="✅")

# SECTION 2: Active Interventions
st.markdown("### Active Interventions")
df_int = pd.DataFrame(st.session_state['interventions'])

for i, row in df_int.iterrows():
    st.markdown(f"**{row['name']}** ({row['segment']}) &bull; *Status: {row['status']}*")
    c1, c2, c3 = st.columns(3)
    c1.metric("Risk Score (Baseline)", row['risk_before'])
    c2.metric("Risk Score (Current)", row['risk_current'], delta=row['risk_current'] - row['risk_before'], delta_color="inverse")
    c3.metric("Capital Allocated", f"${row['cost']:,}")
    st.markdown("<hr style='border-color: rgba(56, 189, 248, 0.15); margin-top: 5px; margin-bottom: 15px;'>", unsafe_allow_html=True)

st.markdown("---")

# SECTION 3: 3-Card Effectiveness & Financial Evaluation (Stage 6)
st.markdown("### Stage 6: Intervention Evaluation & ROI Tracker")

seg_metrics = get_segment_metrics()
seg_lookup = {s['segment']: s for s in seg_metrics}
all_segments = [s['segment'] for s in seg_metrics]
df_emp = load_employees()

def get_role_multiplier(segment_str):
    s = str(segment_str).lower()
    if any(k in s for k in ['senior', 'lead', 'manager', 'director']):
        return mult_sr
    elif 'mid' in s:
        return mult_mid
    return mult_jr

# Preset Mode or Live Interventions
col_sel1, col_sel2 = st.columns([2, 1])
with col_sel1:
    eval_mode = st.selectbox(
        "Evaluation Scenario / Benchmark Presets:",
        [
            "Interactive Intervention Evaluation",
            "Test A: Standard Payoff (92->80 vs 55->51, spend $30k, cost $75k, headcount 25, p_exit 0.32)",
            "Test B: Marginal Progress (Adjusted drop 3 -> Prevented 0.24)",
            "Test C: Negative Trend (Adjusted drop -2 -> Prevented 0)",
            "Test D: Unadjusted Baseline (No comparison team selected)"
        ]
    )

with col_sel2:
    selected_checkpoint = st.radio(
        "Evaluation Checkpoint:",
        ["30-Day Checkpoint", "60-Day Checkpoint", "90-Day Checkpoint"],
        horizontal=True
    )

# Setup parameters based on preset or interactive selection
if "Test A" in eval_mode:
    r_before_treated = 92.0
    r_current_treated = 80.0
    r_before_control = 55.0
    r_current_control = 51.0
    spend = 30000.0
    replacement_cost = 75000.0
    headcount = 25
    p_exit = 0.32
    control_selected = "Operations - Senior"
    has_control = True
elif "Test B" in eval_mode:
    # Test B: adjusted_drop 3 -> prevented 0.24, "Not yet clear"
    # treated 92->80 (drop 12), control 55->46 (drop 9) -> adjusted_drop 3
    r_before_treated = 92.0
    r_current_treated = 80.0
    r_before_control = 55.0
    r_current_control = 46.0
    spend = 30000.0
    replacement_cost = 75000.0
    headcount = 25
    p_exit = 0.32
    control_selected = "Operations - Senior"
    has_control = True
elif "Test C" in eval_mode:
    # Test C: adjusted_drop -2 -> prevented 0, "No measurable improvement"
    r_before_treated = 92.0
    r_current_treated = 84.0
    r_before_control = 55.0
    r_current_control = 45.0
    spend = 30000.0
    replacement_cost = 75000.0
    headcount = 25
    p_exit = 0.32
    control_selected = "Operations - Senior"
    has_control = True
elif "Test D" in eval_mode:
    # Test D: no control -> raw drop used, warning shown, verdict ends "(unadjusted)"
    r_before_treated = 92.0
    r_current_treated = 80.0
    r_before_control = 0.0
    r_current_control = 0.0
    spend = 30000.0
    replacement_cost = 75000.0
    headcount = 25
    p_exit = 0.32
    control_selected = "(None - Unadjusted)"
    has_control = False
else:
    # Interactive / Live intervention evaluation
    target_int = df_int.iloc[0] if not df_int.empty else None
    int_names = df_int['name'].tolist() if not df_int.empty else ["Default Initiative"]
    sel_int_name = st.selectbox("Select Active Retention Initiative:", int_names)
    
    if not df_int.empty and sel_int_name in df_int['name'].values:
        target_int = df_int[df_int['name'] == sel_int_name].iloc[0]
        
    t_seg = target_int['segment'] if target_int is not None else "Engineering - Junior"
    seg_info = seg_lookup.get(t_seg, {})
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown(f"**Treated Cohort:** `{t_seg}`")
        r_before_treated = float(target_int.get('risk_before', 92))
        checkpoints_dict = target_int.get('risk_checkpoints', {})
        r_current_treated = float(checkpoints_dict.get(selected_checkpoint, target_int.get('risk_current', 80)))
        
        c_sub1, c_sub2 = st.columns(2)
        r_before_treated = c_sub1.number_input("Treated Risk (Before)", value=r_before_treated, step=1.0)
        r_current_treated = c_sub2.number_input(f"Treated Risk ({selected_checkpoint})", value=r_current_treated, step=1.0)
        
    with col_c2:
        control_options = ["(None - Unadjusted)"] + [s for s in all_segments if s != t_seg]
        default_ctrl = target_int.get('control_segment', "Engineering - Senior") if target_int is not None else "Engineering - Senior"
        def_idx = control_options.index(default_ctrl) if default_ctrl in control_options else 0
        control_selected = st.selectbox("Comparison Team (Control Cohort):", control_options, index=def_idx)
        has_control = (control_selected != "(None - Unadjusted)")
        
        if has_control:
            ctrl_checkpoints = target_int.get('control_checkpoints', {}) if target_int is not None else {}
            ctrl_def_curr = float(ctrl_checkpoints.get(selected_checkpoint, 51.0))
            ctrl_def_before = float(target_int.get('control_before', 55.0)) if target_int is not None else 55.0
            
            c_ctrl1, c_ctrl2 = st.columns(2)
            r_before_control = c_ctrl1.number_input("Comparison Team Risk (Before)", value=ctrl_def_before, step=1.0)
            r_current_control = c_ctrl2.number_input(f"Comparison Team Risk ({selected_checkpoint})", value=ctrl_def_curr, step=1.0)
        else:
            r_before_control = 0.0
            r_current_control = 0.0
            
    col_e1, col_e2, col_e3, col_e4 = st.columns(4)
    with col_e1:
        spend = st.number_input("Intervention Spend ($)", min_value=0.0, value=float(target_int.get('cost', 30000.0)), step=1000.0)
    with col_e2:
        # Default replacement cost from salary settings
        avg_band = 2.5
        emp_salary = salary_base + (avg_band * salary_per_band)
        tier_m = get_role_multiplier(t_seg)
        calc_rep_cost = emp_salary * tier_m
        replacement_cost = st.number_input("Replacement Cost per Head ($)", min_value=1000.0, value=float(calc_rep_cost), step=5000.0)
    with col_e3:
        def_headcount = int(seg_info.get('total_active', 25))
        headcount = st.number_input("Treated Cohort Headcount", min_value=1, value=def_headcount, step=1)
    with col_e4:
        # Trailing 12-month exit rate definition
        def_p_exit = float(seg_info.get('exit_rate', 0.32))
        p_exit = st.number_input("p_exit (Trailing 12m exit rate)", min_value=0.0, max_value=1.0, value=float(def_p_exit), step=0.05,
                                 help="The treated cohort's trailing-12-month exits / active headcount")

# ==============================================================================
# CARD CALCULATIONS
# ==============================================================================
treated_drop = r_before_treated - r_current_treated

if has_control:
    comparison_drop = r_before_control - r_current_control
    adjusted_drop = treated_drop - comparison_drop
else:
    comparison_drop = 0.0
    adjusted_drop = treated_drop

# CARD 2
breakeven_exits = (spend / replacement_cost) if replacement_cost > 0 else 0.0

# CARD 3: p_exit = the treated cohort's trailing-12-month exits / active headcount
prevented_exits = max(0.0, headcount * (adjusted_drop / 100.0) * p_exit)

# VERDICT
if adjusted_drop <= 0:
    base_verdict = "No measurable improvement"
elif prevented_exits >= breakeven_exits:
    base_verdict = "Likely pays off"
else:
    base_verdict = "Not yet clear - re-check at the next 30/60/90-day point"

if not has_control:
    verdict = f"{base_verdict} (unadjusted)"
else:
    verdict = base_verdict

st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)

# THE THREE CARDS
col_c1, col_c2, col_c3 = st.columns(3)

# CARD 1: Did risk really fall?
with col_c1:
    st.markdown("""
    <div style="background: rgba(11, 15, 25, 0.85); border: 1px solid rgba(56, 189, 248, 0.28); border-radius: 12px; padding: 1.25rem; min-height: 250px;">
        <div style="font-size: 0.8rem; font-weight: 700; color: #38BDF8; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.5rem;">
            CARD 1
        </div>
        <div style="font-size: 1.15rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.75rem;">
            Did risk really fall?
        </div>
    """, unsafe_allow_html=True)
    
    st.metric(
        label="Adjusted Risk Drop",
        value=f"{adjusted_drop:+.1f} pts" if adjusted_drop != 0 else "0.0 pts"
    )
    
    st.markdown(f"• **Treated team's drop:** `{treated_drop:+.1f} pts` ({r_before_treated:.0f} → {r_current_treated:.0f})")
    if has_control:
        st.markdown(f"• **Comparison team's drop (what would have happened anyway):** `{comparison_drop:+.1f} pts` ({r_before_control:.0f} → {r_current_control:.0f})")
    else:
        st.warning("⚠️ Not adjusted for company-wide changes")
        
    st.markdown("</div>", unsafe_allow_html=True)

# CARD 2: What must we prevent to break even?
with col_c2:
    st.markdown("""
    <div style="background: rgba(11, 15, 25, 0.85); border: 1px solid rgba(56, 189, 248, 0.28); border-radius: 12px; padding: 1.25rem; min-height: 250px;">
        <div style="font-size: 0.8rem; font-weight: 700; color: #38BDF8; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.5rem;">
            CARD 2
        </div>
        <div style="font-size: 1.15rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.75rem;">
            What must we prevent to break even?
        </div>
    """, unsafe_allow_html=True)
    
    st.metric(
        label="Breakeven Exits",
        value=f"{breakeven_exits:.2f} exits"
    )
    
    st.markdown(f"• **Intervention Spend:** `${spend:,.0f}`")
    st.markdown(f"• **Per-Head Replacement Cost:** `${replacement_cost:,.0f}`")
    st.caption("Formula: breakeven_exits = intervention_spend / replacement_cost")
    
    st.markdown("</div>", unsafe_allow_html=True)

# CARD 3: What did we probably prevent?
with col_c3:
    st.markdown("""
    <div style="background: rgba(11, 15, 25, 0.85); border: 1px solid rgba(56, 189, 248, 0.28); border-radius: 12px; padding: 1.25rem; min-height: 250px;">
        <div style="font-size: 0.8rem; font-weight: 700; color: #38BDF8; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.5rem;">
            CARD 3
        </div>
        <div style="font-size: 1.15rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.75rem;">
            What did we probably prevent?
        </div>
    """, unsafe_allow_html=True)
    
    st.metric(
        label="Probably Prevented",
        value=f"{prevented_exits:.2f} exits"
    )
    
    st.markdown(f"• **Active Headcount:** `{headcount}` staff")
    st.markdown(f"• **p_exit (trailing-12-month exits / active headcount):** `{p_exit:.1%}`")
    st.caption("Formula: prevented_exits = max(0, headcount * (adjusted_drop / 100) * p_exit)")
    
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

# VERDICT DISPLAY
if "Likely pays off" in verdict:
    verdict_color = "#34D399"
    verdict_icon = "✅"
    verdict_bg = "rgba(16, 185, 129, 0.12)"
    verdict_border = "rgba(52, 211, 153, 0.35)"
elif "No measurable improvement" in verdict:
    verdict_color = "#F43F5E"
    verdict_icon = "⚠️"
    verdict_bg = "rgba(244, 63, 94, 0.12)"
    verdict_border = "rgba(244, 63, 94, 0.35)"
else:
    verdict_color = "#FBBF24"
    verdict_icon = "⏳"
    verdict_bg = "rgba(251, 191, 36, 0.12)"
    verdict_border = "rgba(251, 191, 36, 0.35)"

st.markdown(f"""
<div style="background: {verdict_bg}; border: 1px solid {verdict_border}; border-radius: 12px; padding: 1.1rem 1.5rem; display: flex; align-items: center; justify-content: space-between; margin-top: 0.5rem; margin-bottom: 1rem;">
    <div>
        <div style="font-size: 0.75rem; font-weight: 700; color: {verdict_color}; letter-spacing: 0.08em; text-transform: uppercase;">
            {selected_checkpoint} Synthesis Verdict
        </div>
        <div style="font-size: 1.35rem; font-weight: 800; color: #FFFFFF; margin-top: 0.2rem;">
            {verdict_icon} {verdict}
        </div>
    </div>
    <div style="text-align: right; color: #94A3B8; font-size: 0.85rem;">
        Prevented: <strong>{prevented_exits:.2f}</strong> vs Hurdle: <strong>{breakeven_exits:.2f}</strong><br>
        Adjusted Drop: <strong>{adjusted_drop:+.1f} pts</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# EXPANDER: Illustrative savings estimate
gross_savings = prevented_exits * replacement_cost
net_gain = gross_savings - spend
roi_pct = ((net_gain / spend) * 100.0) if spend > 0 else 0.0

with st.expander("💼 Illustrative savings estimate", expanded=True):
    col_sv1, col_sv2, col_sv3 = st.columns(3)
    with col_sv1:
        st.metric("Gross Modelled Savings", f"${gross_savings:,.0f}", help="prevented_exits * replacement_cost")
    with col_sv2:
        st.metric("Net Financial Gain", f"${net_gain:,.0f}", delta=f"{net_gain:,.0f}", delta_color="normal", help="gross_savings - spend")
    with col_sv3:
        st.metric("Modelled ROI", f"{roi_pct:+.1f}%", help="net_gain / spend * 100")
        
    st.caption("Estimate based on modelled assumptions, not observed outcomes.")

st.markdown("---")

# SECTION 4: Timeline View (Gantt)
st.markdown("### Intervention Timeline (Gantt)")
df_timeline = df_int.copy()
df_timeline['start_date'] = pd.to_datetime(df_timeline['start_date'])
df_timeline['end_date'] = df_timeline['start_date'] + pd.Timedelta(days=90)

fig_gantt = px.timeline(
    df_timeline,
    x_start="start_date",
    x_end="end_date",
    y="name",
    color="status",
    color_discrete_sequence=[COLORS['primary'], COLORS['warning'], COLORS['muted']]
)
fig_gantt.update_yaxes(autorange="reversed")
fig_gantt.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig_gantt, use_container_width=True, config={'displayModeBar': False, 'responsive': True})
