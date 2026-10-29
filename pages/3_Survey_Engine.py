import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from config import APP_TITLE, APP_ICON, COLORS, DEPARTMENTS
from utils.styles import apply_custom_css
from utils.navigation import render_top_navbar
from utils.data_loader import load_survey_responses
from ai_engine.gemini_client import GeminiClient
from ai_engine.survey_generator import SurveyGenerator

st.set_page_config(
    page_title=f"Survey Engine | {APP_TITLE}",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)
apply_custom_css()
render_top_navbar(active_page="survey")

st.title("Adaptive Survey Engine")
st.markdown('<p class="subtitle">AI-generated proactive micro-surveys and longitudinal response analytics.</p>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Generate Adaptive Survey", "Response Analytics"])

with tab1:
    st.markdown("### Generate Adaptive Survey")
    st.info("Survey questions employ evidence-based psychological framing: indirect inquiry, behavioral anchoring, and constructive prompts to ensure candor.")
    
    with st.expander("🧠 How the AI is Conditioned (Psychometric Prompt Guardrails)", expanded=False):
        st.markdown("""
        **Evidence-Based Framing Rules Injected into the Generative AI Prompt:**
        1. **Behavioral Anchoring:** Always asks about *observable actions*, not internal subjective feelings (e.g., *"How frequently does your manager provide actionable sprint feedback?"* instead of *"Do you like your manager?"*).
        2. **Timeframe Anchoring:** Anchors every inquiry to a precise window (*"In the past 30 days..."* or *"Over the last 2 weeks..."*) to prevent recency bias.
        3. **Indirect Inquiry (Job Embeddedness):** Never asks blunt, leading questions like *"Are you planning to quit?"*. Instead, it evaluates organizational link density and role alignment.
        4. **Constructive Framing:** Enforces forward-looking prompts (*"What would elevate your sprint velocity?"*) to eliminate venting distortion.
        5. **Standardized 5-Point Likert Mapping:** Maps every behavioral question to measurable frequencies (*Never, Rarely, Sometimes, Often, Consistently*).
        """)
    
    # Check for AI analysis from Exit Analyzer
    ai_analysis = st.session_state.get('ai_analysis')
    themes = []
    use_sample_themes = False
    
    if ai_analysis and 'themes' in ai_analysis:
        st.success("✅ Extracted themes from Exit Feedback Analyzer detected.")
        sorted_themes = sorted(ai_analysis['themes'], key=lambda x: x.get('frequency_pct', 0), reverse=True)
        themes = sorted_themes[:3]
    else:
        st.info("ℹ️ Complete the Exit Feedback Analyzer first to ingest live organizational themes.")
        use_sample_themes = st.checkbox("Load benchmark organizational themes for testing")
        if use_sample_themes:
            themes = [{"name": "Career Growth"}, {"name": "Management Alignment"}, {"name": "Work-Life Balance"}]
            
    col_t1, col_t2 = st.columns([1, 2])
    with col_t1:
        target_dept = st.selectbox("Target Department", ["All"] + DEPARTMENTS)
        generate_btn = st.button("Generate Survey Questions", type="primary", disabled=not themes)
        
    if generate_btn:
        with st.spinner("Generating targeted questions with AI engine..."):
            client = GeminiClient()
            generator = SurveyGenerator(client)
            questions = generator.generate_survey(themes, target_department=target_dept if target_dept != "All" else None)
            st.session_state['generated_survey'] = questions

    if 'generated_survey' in st.session_state:
        st.markdown("---")
        questions = st.session_state['generated_survey']
        
        survey_text = []
        for i, q in enumerate(questions):
            st.markdown(f"**Question {i+1}: {q['question']}**")
            st.markdown(f"*Core Vector: {q['theme']} &bull; Type: {q['response_type']}*")
            if q['options']:
                st.radio(f"Preview Q{i+1}", q['options'], key=f"preview_q_{i}", label_visibility="collapsed")
            else:
                st.text_area(f"Preview Q{i+1}", disabled=True, key=f"preview_q_{i}", label_visibility="collapsed")
            st.markdown("<hr style='margin-top: 10px; margin-bottom: 20px; border-color: rgba(56, 189, 248, 0.15);'>", unsafe_allow_html=True)
            
            survey_text.append(f"{i+1}. {q['question']}\nOptions: {', '.join(q['options']) if q['options'] else 'Open text'}")
            
        st.download_button("Export Survey as Text", "\n\n".join(survey_text), file_name="retain_generated_survey.txt", type="primary")
        
with tab2:
    st.markdown("### Historical Response Analytics")
    st.caption("🛡️ Never scores or reports on individuals; all outputs are aggregated at cohort level with a minimum of 5 responses. Individual-level text (exit notes, retros) is processed only to extract thematic clusters and is not accessible to managers.")
    st.caption("📅 *Telemetry Cadence:* Scores update on a scheduled quarterly cadence so leavers cannot be deduced by day-to-day shifts.")
    
    with st.expander("🛡️ Data Privacy & Statutory Consent Notice (DPDP Act 2023)", expanded=False):
        st.markdown("""
        **Compliance Notice under the Digital Personal Data Protection Act (DPDP Act 2023):**
        - **No Individual Scoring:** Never scores or reports on individuals; all outputs are aggregated at cohort level with a minimum of 5 responses. Individual-level text (exit notes, retros) is processed only to extract thematic clusters and is not accessible to managers.
        - **Strict k-Anonymity on Responses:** The $k \ge 5$ threshold is applied strictly to survey *responses*, not nominal headcount. Any cohort with fewer than 5 responses is marked as *"Insufficient data (n < 5 responses)"* and merged into parent aggregates.
        - **Anti-Differencing Defense:** Cohorts with 5 to 9 responses ($5 \le n < 10$) display qualitative rating bands rather than exact 2-decimal numbers. Complementary suppression prevents algebraic reverse-engineering.
        - **Cadence Protection:** Telemetry updates occur on a scheduled quarterly cadence so individual leavers cannot be deduced from day-to-day roster departures.
        """)
        
    df_surveys = load_survey_responses()
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        sel_rounds = st.multiselect("Select Survey Rounds", sorted(df_surveys['survey_round'].unique()), default=sorted(df_surveys['survey_round'].unique()))
    with col_f2:
        sel_depts = st.multiselect("Filter by Department", DEPARTMENTS, default=DEPARTMENTS)
        
    filtered = df_surveys[df_surveys['survey_round'].isin(sel_rounds) & df_surveys['department'].isin(sel_depts)]
    
    if filtered.empty:
        st.warning("No survey response telemetry available for the selected filters.")
    else:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Average Score by Theme")
            theme_scores = filtered.groupby(['question_theme', 'survey_round'])['avg_score'].mean().reset_index()
            theme_scores['survey_round'] = theme_scores['survey_round'].astype(str)
            fig_bar = px.bar(theme_scores, x='question_theme', y='avg_score', color='survey_round', barmode='group')
            fig_bar.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", yaxis_range=[1,5])
            st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False, 'responsive': True})
            
        with c2:
            st.markdown("#### Response Rate by Department")
            rr = filtered.groupby('department')['response_rate'].mean().reset_index()
            fig_rr = px.bar(rr, x='response_rate', y='department', orientation='h')
            fig_rr.update_traces(marker_color=COLORS['primary'])
            fig_rr.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", xaxis_tickformat='.0%')
            st.plotly_chart(fig_rr, use_container_width=True, config={'displayModeBar': False, 'responsive': True})
            
        c3, c4 = st.columns(2)
        with c3:
            st.markdown("#### Sentiment Score Distribution Heatmap")
            heatmap_data = filtered.groupby(['department', 'question_theme'])['avg_score'].mean().unstack()
            fig_heat = px.imshow(heatmap_data, text_auto=".1f", aspect="auto", color_continuous_scale="RdYlGn", zmin=1, zmax=5)
            fig_heat.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_heat, use_container_width=True, config={'displayModeBar': False, 'responsive': True})
            
        with c4:
            st.markdown("#### Sentiment Trajectory Across Rounds")
            trend_data = filtered.groupby(['survey_round', 'question_theme'])['avg_score'].mean().reset_index()
            fig_trend = px.line(trend_data, x='survey_round', y='avg_score', color='question_theme', markers=True)
            fig_trend.update_layout(template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", yaxis_range=[1,5])
            st.plotly_chart(fig_trend, use_container_width=True, config={'displayModeBar': False, 'responsive': True})
