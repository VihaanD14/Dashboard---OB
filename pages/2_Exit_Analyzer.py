import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from config import APP_TITLE, APP_ICON, COLORS
from utils.styles import apply_custom_css
from utils.navigation import render_top_navbar
from utils.data_loader import load_exit_interviews, load_survey_responses
from ai_engine.gemini_client import GeminiClient
from ai_engine.theme_extractor import ThemeExtractor

st.set_page_config(
    page_title=f"Exit Analyzer | {APP_TITLE}",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)
apply_custom_css()
render_top_navbar(active_page="exit")

st.title("Exit Feedback Analyzer")
st.markdown('<p class="subtitle">Qualitative exit interview analysis and AI-driven theme extraction.</p>', unsafe_allow_html=True)

df_exits = load_exit_interviews()
df_exits['exit_date'] = pd.to_datetime(df_exits['exit_date'])

# SECTION 1: Exit Data Overview & Filters
st.markdown("### Data Filters")
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    departments = ["All"] + list(df_exits['department'].unique())
    sel_dept = st.selectbox("Department", departments)
with col_f2:
    roles = ["All"] + list(df_exits['role_level'].unique())
    sel_role = st.selectbox("Role Level", roles)
with col_f3:
    sel_range = st.date_input("Date Range", [df_exits['exit_date'].min().date(), df_exits['exit_date'].max().date()])

filtered_df = df_exits.copy()
if sel_dept != "All": filtered_df = filtered_df[filtered_df['department'] == sel_dept]
if sel_role != "All": filtered_df = filtered_df[filtered_df['role_level'] == sel_role]
if len(sel_range) == 2:
    start_d, end_d = sel_range
    filtered_df = filtered_df[(filtered_df['exit_date'].dt.date >= start_d) & (filtered_df['exit_date'].dt.date <= end_d)]

st.markdown("### Filtered Exit Telemetry")
col_s1, col_s2, col_s3, col_s4 = st.columns(4)
with col_s1: st.metric("Total Exits (Filtered)", len(filtered_df))
with col_s2: st.metric("Avg Tenure at Exit", f"{filtered_df['tenure_at_exit'].mean():.1f} yrs" if len(filtered_df)>0 else "N/A")
with col_s3: 
    top_reason = filtered_df['stated_reason'].mode()[0] if len(filtered_df)>0 else "N/A"
    st.metric("Top Stated Reason", top_reason)
with col_s4: st.metric("Avg Satisfaction", f"{filtered_df['satisfaction_rating'].mean():.1f}/5" if len(filtered_df)>0 else "N/A")

with st.expander("View Raw Interview Records (Includes Free-Text Comments)"):
    st.dataframe(filtered_df[['employee_id', 'exit_date', 'department', 'role_level', 'stated_reason', 'free_text_feedback']], use_container_width=True)

st.markdown("---")

# SECTION 2: AI Theme Analysis
st.markdown("### AI Theme Analysis")
st.write("Extract hidden insights and implicit turnover drivers from unstructured feedback using generative NLP.")

if 'ai_analysis' not in st.session_state:
    st.session_state['ai_analysis'] = None

if st.button("Analyze Exit Feedback", type="primary"):
    with st.spinner("Analyzing feedback records with AI engine..."):
        client = GeminiClient()
        extractor = ThemeExtractor(client)
        feedbacks = filtered_df['free_text_feedback'].dropna().tolist()
        if feedbacks:
            st.session_state['ai_analysis'] = extractor.extract_themes(feedbacks)
        else:
            st.warning("No feedback text available in the filtered dataset.")

if st.session_state['ai_analysis']:
    analysis = st.session_state['ai_analysis']
    
    col_ai1, col_ai2 = st.columns([1, 1])
    
    with col_ai1:
        st.markdown("#### Primary Themes & Sentiment Index")
        themes_df = pd.DataFrame(analysis['themes'])
        themes_df = themes_df.sort_values('frequency_pct', ascending=True)
        
        fig_themes = px.bar(
            themes_df, x='frequency_pct', y='name', orientation='h',
            color='sentiment', color_continuous_scale="RdYlGn",
            range_color=[-1, 1],
            text='frequency_pct'
        )
        fig_themes.update_traces(texttemplate='%{text}%')
        fig_themes.update_layout(
            template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Frequency (%)", yaxis_title="", margin=dict(t=10)
        )
        st.plotly_chart(fig_themes, use_container_width=True, config={'displayModeBar': False, 'responsive': True})
        
    with col_ai2:
        st.markdown("#### Stated vs. Actual Implied Reasons")
        for item in analysis.get('stated_vs_implied', []):
            st.info(f"**{item['issue']}**\n- **Stated:** {item['stated_reason']}\n- **Implied:** {item['actual_implied_reason']}")
            
        st.markdown("#### Emerging Organizational Concerns")
        for concern in analysis.get('emerging_concerns', []):
            st.error(f"⚠️ {concern}")

st.markdown("---")

# SECTION 3: Demographic Breakdown
st.markdown("### Demographic Breakdown")
col_d1, col_d2, col_d3 = st.columns(3)

with col_d1:
    fig_dept = px.bar(filtered_df['department'].value_counts().reset_index(), x='department', y='count', title="Exits by Department")
    fig_dept.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="")
    fig_dept.update_traces(marker_color=COLORS['primary'])
    st.plotly_chart(fig_dept, use_container_width=True, config={'displayModeBar': False, 'responsive': True})

with col_d2:
    bins = [0, 1, 3, 5, 20]
    labels = ['0-1yr', '1-3yr', '3-5yr', '5+yr']
    filtered_df['tenure_band'] = pd.cut(filtered_df['tenure_at_exit'], bins=bins, labels=labels)
    fig_tenure = px.bar(filtered_df['tenure_band'].value_counts().reset_index(), x='tenure_band', y='count', title="Exits by Tenure Band")
    fig_tenure.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="")
    fig_tenure.update_traces(marker_color=COLORS['secondary'])
    st.plotly_chart(fig_tenure, use_container_width=True, config={'displayModeBar': False, 'responsive': True})

with col_d3:
    fig_role = px.bar(filtered_df['role_level'].value_counts().reset_index(), x='role_level', y='count', title="Exits by Role Level")
    fig_role.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", xaxis_title="", yaxis_title="")
    fig_role.update_traces(marker_color=COLORS['muted'])
    st.plotly_chart(fig_role, use_container_width=True, config={'displayModeBar': False, 'responsive': True})

st.markdown("#### Cross-Departmental Reason Distribution")
heatmap_data = pd.crosstab(filtered_df['stated_reason'], filtered_df['department'])
fig_heat = px.imshow(heatmap_data, text_auto=True, aspect="auto", color_continuous_scale="Blues")
fig_heat.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", margin=dict(t=10))
st.plotly_chart(fig_heat, use_container_width=True, config={'displayModeBar': False, 'responsive': True})

st.markdown("---")

# SECTION 4: Timeline View
st.markdown("### Longitudinal Timeline View")
monthly_exits = filtered_df.resample('ME', on='exit_date').size().reset_index(name='exits')
fig_time = px.line(monthly_exits, x='exit_date', y='exits', markers=True, title="Monthly Exits Relative to Survey Rounds")

df_surveys = load_survey_responses()
survey_dates = pd.to_datetime(df_surveys['survey_date'].unique())

for sd in survey_dates:
    fig_time.add_vline(x=sd.timestamp() * 1000, line_width=1, line_dash="dash", line_color=COLORS['warning'], annotation_text="Survey")

fig_time.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
fig_time.update_traces(line_color=COLORS['danger'], line_width=2)
st.plotly_chart(fig_time, use_container_width=True, config={'displayModeBar': False, 'responsive': True})
