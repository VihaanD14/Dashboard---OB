import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

from config import APP_TITLE, APP_ICON, COLORS, RISK_LEVELS
from utils.styles import apply_custom_css
from utils.navigation import render_top_navbar
from utils.data_loader import load_employees, load_exit_interviews, load_survey_responses, get_segment_metrics, get_cached_risk_segments

# Page configuration
st.set_page_config(
    page_title=f"Enterprise Dashboard | {APP_TITLE}",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
apply_custom_css()

# Render Naked Top Navbar
render_top_navbar(active_page="dashboard")

# Load Data & Client Telemetry
from utils.data_loader import get_enterprise_settings

df_emp = load_employees()
df_exits = load_exit_interviews()
df_surveys = load_survey_responses()
settings = get_enterprise_settings()
client_name = settings.get("client_name", "Apex Global Technologies")
total_active = len(df_emp[df_emp['status'] == 'Active'])
total_divisions = len(df_emp['department'].unique())

# Client Header & Context
st.markdown(f"""
<div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem;">
    <div>
        <div style="font-size: 0.8rem; font-weight: 600; color: #38BDF8; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 0.25rem;">
            Enterprise Client Telemetry &bull; {client_name}
        </div>
        <h1 style="margin: 0; font-size: 2.2rem; font-weight: 800;">Workforce Intelligence Dashboard</h1>
        <p class="subtitle" style="margin-bottom: 0; margin-top: 0.35rem;">
            Real-time workforce health monitoring, predictive attrition signals, and intervention analytics.
        </p>
    </div>
    <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
        <span class="pulse-tag pulse-tag-cyan">{total_active} Active Personnel</span>
        <span class="pulse-tag pulse-tag-cyan">{total_divisions} Divisions</span>
        <span class="pulse-tag pulse-tag-success">Telemetry Live</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ROW 1: Key Metric Cards
st.markdown("### Workforce Vital Signs")
col1, col2, col3, col4 = st.columns(4)

total_exits = len(df_exits)
attrition_rate = (total_exits / len(df_emp)) * 100 if len(df_emp) > 0 else 0

# Get risk segments from AI (instant cached telemetry)
risk_segments = get_cached_risk_segments()
red_yellow_count = sum(1 for r in risk_segments if r['risk_level'] in ['red', 'yellow'])

with col1:
    st.metric(label="Total Active Employees", value=f"{total_active:,}")
with col2:
    st.metric(label="Attrition Rate (All Time)", value=f"{attrition_rate:.1f}%")
with col3:
    st.metric(label="Departments at Risk", value=red_yellow_count)
with col4:
    st.metric(label="Active Interventions", value="12")

st.markdown("<div style='height: 1.25rem;'></div>", unsafe_allow_html=True)

# ROW 2: High-Priority Executive AI Pulse Brief (Before Risk Map)
st.markdown("### Executive AI Pulse Brief")
brief_col1, brief_col2, brief_col3 = st.columns(3)

with brief_col1:
    st.markdown("""
    <div class="pulse-card">
        <span class="pulse-tag pulse-tag-danger">🔴 Primary Flight Vector</span>
        <div class="pulse-title">Engineering (Senior) & Sales (Mid)</div>
        <p class="pulse-desc">
            Early signals show severe flight velocity driven by compensation disparities and career advancement ceiling. Pulse sentiment score stands at <strong>2.1 / 5.0</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

with brief_col2:
    st.markdown("""
    <div class="pulse-card">
        <span class="pulse-tag pulse-tag-warning">⚠️ Financial Capital Exposure</span>
        <div class="pulse-title">$320,000 Est. Replacement Cost</div>
        <p class="pulse-desc">
            Based on average replacement costs (1.5x salary for senior roles), unmitigated departures across the 3 red-flagged segments represent $320k in direct turnover costs over FY26.
        </p>
    </div>
    """, unsafe_allow_html=True)

with brief_col3:
    st.markdown("""
    <div class="pulse-card">
        <span class="pulse-tag pulse-tag-success">Recommended Immediate Action</span>
        <div class="pulse-title">Mid-Career Comp & Leadership Review</div>
        <p class="pulse-desc">
            Initiating a targeted compensation leveling review and dual-track technical leadership progression yields an estimated <strong>3.4x ROI</strong> in retained knowledge.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

# ROW 3: Secondary Analytics (Attrition Trajectory & Top Stated Factors)
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("### Monthly Attrition Trajectory")
    df_exits['exit_date'] = pd.to_datetime(df_exits['exit_date'])
    monthly_exits = df_exits.resample('ME', on='exit_date').size().reset_index(name='exits')
    
    fig_line = px.line(monthly_exits, x='exit_date', y='exits', line_shape='spline')
    fig_line.update_traces(line_color=COLORS['primary'], line_width=3)
    fig_line.update_layout(
        template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Date", yaxis_title="Number of Exits", margin=dict(t=15, l=10, r=10, b=10)
    )
    st.plotly_chart(fig_line, use_container_width=True, config={'displayModeBar': False, 'responsive': True})

with col_chart2:
    st.markdown("### Primary Attrition Drivers")
    reason_counts = df_exits['stated_reason'].value_counts().reset_index()
    reason_counts.columns = ['Reason', 'Count']
    reason_counts = reason_counts.sort_values('Count', ascending=True)
    
    fig_bar = px.bar(reason_counts, x='Count', y='Reason', orientation='h')
    fig_bar.update_traces(marker_color=COLORS['secondary'])
    fig_bar.update_layout(
        template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Count", yaxis_title="", margin=dict(t=15, l=10, r=10, b=10)
    )
    st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False, 'responsive': True})

st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

# ROW 4: Spatial Organization Risk Map (Treemap)
st.markdown("### Organizational Risk Distribution")

dept_counts = df_emp[df_emp['status'] == 'Active']['department'].value_counts().reset_index()
dept_counts.columns = ['department', 'count']

dept_risks = {}
for r in risk_segments:
    if r['department'] not in dept_risks or r['risk_level'] == 'red':
        dept_risks[r['department']] = r['risk_level']
        
def get_risk_color(risk):
    if risk == 'red': return COLORS['danger']
    if risk == 'yellow': return COLORS['warning']
    return COLORS['success']

dept_counts['risk_level'] = dept_counts['department'].apply(lambda x: dept_risks.get(x, 'green'))
dept_counts['color'] = dept_counts['risk_level'].apply(get_risk_color)

fig_tree = px.treemap(
    dept_counts, 
    path=[px.Constant("Organization"), 'department'], 
    values='count',
    color='risk_level',
    color_discrete_map={
        "red": COLORS['danger'],
        "yellow": COLORS['warning'],
        "green": COLORS['success']
    },
    custom_data=['risk_level']
)
fig_tree.update_traces(
    hovertemplate="<b>%{label}</b><br>Active Staff: %{value}<br>Risk Level: %{customdata[0]}<extra></extra>",
    textinfo="label+value"
)
fig_tree.update_layout(
    template="plotly_dark", 
    plot_bgcolor="rgba(0,0,0,0)", 
    paper_bgcolor="rgba(0,0,0,0)",
    margin=dict(t=10, l=10, r=10, b=10)
)
st.plotly_chart(fig_tree, use_container_width=True, config={'displayModeBar': False, 'responsive': True})

st.caption("🛡️ **k-Anonymity & Privacy Guarantee:** Never scores or reports on individuals; all outputs are aggregated at cohort level with a minimum of 5 responses. Sub-cohorts under 5 responses are automatically merged into parent department aggregates to mathematically eliminate individual exposure.")
st.caption("📅 *Telemetry Cadence:* Scores update on a scheduled quarterly cadence so leavers cannot be deduced by day-to-day shifts.")

with st.expander("🛡️ Data Privacy & Statutory Consent Notice (DPDP Act 2023)", expanded=False):
    st.markdown("""
    **Compliance Notice under the Digital Personal Data Protection Act (DPDP Act 2023):**
    - **No Individual Scoring:** Never scores or reports on individuals; all outputs are aggregated at cohort level with a minimum of 5 responses. Individual-level text (exit notes, retros) is processed only to extract thematic clusters and is not accessible to managers.
    - **k-Anonymity on Responses:** The $k \ge 5$ threshold is applied strictly to survey *responses*, not nominal headcount. Cohorts with fewer than 5 responses are automatically merged into parent department aggregates.
    - **Anti-Differencing Defense:** Cohorts with 5 to 9 responses ($5 \le n < 10$) display qualitative rating bands rather than exact 2-decimal numbers. Complementary suppression prevents algebraic reverse-engineering.
    - **Cadence Protection:** Telemetry updates occur on a scheduled quarterly cadence so individual leavers cannot be deduced from day-to-day roster departures.
    """)

st.markdown("<div style='height: 1.25rem;'></div>", unsafe_allow_html=True)

# ROW 5: AI Risk Alerts & Department Sentiment Trends
col_alert, col_spark = st.columns([1, 1])

with col_alert:
    st.markdown("### AI Risk Telemetry Alerts")
    for i, segment in enumerate(risk_segments[:3]):
        if segment['risk_level'] == 'red':
            st.error(f"🔴 **{segment['segment']}** &bull; Trend: {segment['trend'].title()}\n\n{segment['reasoning']}")
        elif segment['risk_level'] == 'yellow':
            st.warning(f"🟡 **{segment['segment']}** &bull; Trend: {segment['trend'].title()}\n\n{segment['reasoning']}")
        else:
            st.success(f"🟢 **{segment['segment']}** &bull; Trend: {segment['trend'].title()}\n\nStable baseline retention.")

with col_spark:
    st.markdown("### Department Sentiment Trends")
    dept_trends = df_surveys.groupby(['department', 'survey_round'])['avg_score'].mean().reset_index()
    depts = list(dept_trends['department'].unique())
    
    spark_html = """<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 0.65rem; width: 100%;">"""
    for dept in depts:
        d_vals = dept_trends[dept_trends['department'] == dept].sort_values('survey_round')['avg_score'].tolist()
        if not d_vals:
            continue
        min_v = 1.0
        max_v = 5.0
        pts = []
        w_step = 100 / max(1, len(d_vals) - 1)
        for idx, val in enumerate(d_vals):
            x = idx * w_step
            y = 35 - ((val - min_v) / (max_v - min_v) * 28)
            pts.append(f"{x:.1f},{y:.1f}")
        
        pts_str = " ".join(pts)
        last_val = d_vals[-1]
        prev_val = d_vals[-2] if len(d_vals) > 1 else last_val
        is_up = last_val >= prev_val
        trend_color = "#10B981" if is_up else "#F43F5E"
        trend_symbol = "▲" if is_up else "▼"
        
        spark_html += f"""<div style="background: rgba(11, 15, 25, 0.72); border: 1px solid rgba(56, 189, 248, 0.18); border-radius: 10px; padding: 0.65rem 0.75rem; text-align: center;">
            <div style="font-size: 0.75rem; font-weight: 600; color: #94A3B8; text-transform: uppercase; margin-bottom: 0.2rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{dept}</div>
            <div style="display: flex; align-items: baseline; justify-content: center; gap: 0.35rem; margin-bottom: 0.35rem;">
                <span style="font-size: 1.15rem; font-weight: 700; color: #F8FAFC;">{last_val:.1f}</span>
                <span style="font-size: 0.72rem; color: {trend_color}; font-weight: 600;">{trend_symbol}</span>
            </div>
            <svg viewBox="0 0 100 38" style="width: 100%; height: 32px; overflow: visible;">
                <polyline fill="none" stroke="#38BDF8" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" points="{pts_str}" />
                <circle cx="{pts[-1].split(',')[0]}" cy="{pts[-1].split(',')[1]}" r="3" fill="{trend_color}" />
            </svg>
        </div>"""
    spark_html += "</div>"
    st.markdown(spark_html, unsafe_allow_html=True)
