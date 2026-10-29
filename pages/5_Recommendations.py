import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from config import APP_TITLE, APP_ICON, COLORS
from utils.styles import apply_custom_css
from utils.navigation import render_top_navbar
from utils.data_loader import load_policies, get_segment_metrics
from ai_engine.gemini_client import GeminiClient
from ai_engine.recommendation_engine import RecommendationEngine
from ai_engine.risk_scorer import RiskScorer

st.set_page_config(
    page_title=f"Recommendations | {APP_TITLE}",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)
apply_custom_css()
render_top_navbar(active_page="recommendations")

st.title("Retention Recommendations")
st.markdown('<p class="subtitle">AI-generated retention strategies, cost-impact modeling, and actionable playbooks.</p>', unsafe_allow_html=True)

# SECTION 1: Generate Button
st.markdown("### AI Recommendation Generator")
if st.button("Generate Recommendations", type="primary"):
    with st.spinner("Synthesizing optimal retention strategies with generative reasoning..."):
        client = GeminiClient()
        scorer = RiskScorer(client)
        engine = RecommendationEngine(client)
        
        metrics = get_segment_metrics()
        risk_segments = scorer.score_risk(metrics)
        high_risk = [r for r in risk_segments if r['risk_level'] in ['red', 'yellow']]
        policies = load_policies()
        
        recs = engine.generate_recommendations(high_risk, policies)
        st.session_state['recs'] = recs
        st.toast("Analysis complete! Recommendations generated.", icon="✅")

if 'recs' in st.session_state:
    recs = st.session_state['recs']
    df_recs = pd.DataFrame(recs)
    
    st.success(f"{len(recs)} strategic interventions synthesized for high-risk workforce cohorts.")
    st.markdown("---")
    
    # SECTION 2: Retention Action Matrix
    st.markdown("### Retention Action Matrix")
    
    val_map = {"low": 1, "medium": 2, "high": 3}
    df_recs['cost_val'] = df_recs['estimated_cost'].str.lower().map(val_map)
    df_recs['impact_val'] = df_recs['expected_impact'].str.lower().map(val_map)
    
    cat_colors = {
        "quick_win": COLORS['success'],
        "strategic": COLORS['primary'],
        "nice_to_have": COLORS['warning'],
        "avoid": COLORS['danger']
    }
    
    df_recs['cost_val_jitter'] = df_recs['cost_val'] + np.random.uniform(-0.15, 0.15, len(df_recs))
    df_recs['impact_val_jitter'] = df_recs['impact_val'] + np.random.uniform(-0.15, 0.15, len(df_recs))
    
    fig_matrix = px.scatter(
        df_recs, x='cost_val_jitter', y='impact_val_jitter', color='category',
        color_discrete_map=cat_colors, size_max=25, size=[20]*len(df_recs),
        hover_name='title', hover_data={'cost_val_jitter': False, 'impact_val_jitter': False, 'target_segment': True, 'estimated_cost': True, 'expected_impact': True}
    )
    
    fig_matrix.add_vline(x=2, line_width=1, line_dash="dash", line_color=COLORS['muted'])
    fig_matrix.add_hline(y=2, line_width=1, line_dash="dash", line_color=COLORS['muted'])
    
    fig_matrix.update_layout(
        template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(title="Estimated Cost", tickmode='array', tickvals=[1, 2, 3], ticktext=['Low', 'Medium', 'High'], range=[0.5, 3.5]),
        yaxis=dict(title="Expected Impact", tickmode='array', tickvals=[1, 2, 3], ticktext=['Low', 'Medium', 'High'], range=[0.5, 3.5]),
        height=500
    )
    
    fig_matrix.add_annotation(x=1.2, y=3.3, text="Quick Wins", showarrow=False, font=dict(color=COLORS['success'], size=14))
    fig_matrix.add_annotation(x=2.8, y=3.3, text="Strategic Investments", showarrow=False, font=dict(color=COLORS['primary'], size=14))
    fig_matrix.add_annotation(x=1.2, y=0.7, text="Nice-to-Have", showarrow=False, font=dict(color=COLORS['warning'], size=14))
    fig_matrix.add_annotation(x=2.8, y=0.7, text="Avoid", showarrow=False, font=dict(color=COLORS['danger'], size=14))
    
    st.plotly_chart(fig_matrix, use_container_width=True, config={'displayModeBar': False, 'responsive': True})
    
    st.markdown("#### Detailed Action Specifications")
    for cat in ["quick_win", "strategic", "nice_to_have", "avoid"]:
        cat_recs = df_recs[df_recs['category'] == cat]
        if not cat_recs.empty:
            st.markdown(f"**{cat.replace('_', ' ').title()}**")
            for _, r in cat_recs.iterrows():
                with st.expander(f"{r['title']} ({r['target_segment']})"):
                    st.write(r['description'])
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Deployment Timeline", r['timeline'])
                    c2.metric("Resource Cost", r['estimated_cost'].title())
                    c3.metric("Retention Impact", r['expected_impact'].title())
                    st.info(f"**Evidence Base:** {r['evidence']}")
                    
    st.markdown("---")
    
    # SECTION 3: Policy Alignment
    st.markdown("### Policy Alignment Analysis")
    st.markdown("Benchmarking suggested interventions against active organizational policies.")
    align_data = []
    policies = load_policies()
    for _, r in df_recs.iterrows():
        aligned = any(k.split('_')[0] in r['description'].lower() for k in policies.keys())
        align_data.append({
            "Recommendation": r['title'],
            "Status": "✅ Extends Existing Policy" if aligned else "New Initiative Blueprint"
        })
    st.dataframe(pd.DataFrame(align_data), use_container_width=True)
    
    st.markdown("---")
    
    # SECTION 4: Action Plan Export
    st.markdown("### Action Plan Export")
    
    report_text = "RetAIn Enterprise Action Plan\n=================================\n\n"
    for _, r in df_recs.iterrows():
        report_text += f"- [{r['category'].upper()}] {r['title']} (Target: {r['target_segment']})\n"
        report_text += f"  Timeline: {r['timeline']}, Cost: {r['estimated_cost']}, Impact: {r['expected_impact']}\n"
        report_text += f"  {r['description']}\n\n"
        
    st.download_button("Export Action Plan (TXT)", data=report_text, file_name="retain_action_plan.txt", type="primary")
