import streamlit as st
import time

def show_splash_screen():
    if 'splash_shown' not in st.session_state:
        st.session_state.splash_shown = False

    if not st.session_state.splash_shown:
        html_content = """<style>
#splash-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #0b0f17;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 999999;
    font-family: 'Inter', sans-serif;
    pointer-events: none;
}
.ambient-glow {
    position: absolute;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.14) 0%, rgba(11, 15, 23, 0) 70%);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 0;
    pointer-events: none;
}
.logo-path {
    stroke-dasharray: 300;
    stroke-dashoffset: 300;
    animation: drawLine 0.7s cubic-bezier(0.65, 0, 0.35, 1) forwards;
}
@keyframes drawLine {
    to { stroke-dashoffset: 0; }
}
.fade-scale-in {
    opacity: 0;
    transform: scale(0.96);
    animation: fadeScaleIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.25s forwards;
    z-index: 10;
    margin-top: 20px;
}
@keyframes fadeScaleIn {
    to { opacity: 1; transform: scale(1); }
}
.tagline-fade {
    opacity: 0;
    transform: translateY(6px);
    animation: taglineFade 0.5s cubic-bezier(0.16, 1, 0.3, 1) 0.35s forwards;
    font-size: 0.75rem;
    color: #94a3b8;
    font-weight: 300;
    letter-spacing: 0.025em;
    line-height: 1.625;
    margin-top: 10px;
    z-index: 10;
}
@keyframes taglineFade {
    to { opacity: 1; transform: translateY(0); }
}
.splash-progress-container {
    width: 160px;
    height: 2px;
    background-color: rgba(30, 41, 59, 0.8);
    border-radius: 9999px;
    overflow: hidden;
    margin-top: 16px;
    z-index: 10;
}
.progress-bar-fill {
    width: 0%;
    height: 100%;
    background: linear-gradient(to right, #0284c7, #38bdf8, #22d3ee);
    border-radius: 9999px;
    animation: fillProgress 0.7s cubic-bezier(0.65, 0, 0.35, 1) 0.35s forwards;
}
@keyframes fillProgress {
    to { width: 100%; }
}
.splash-exit {
    animation: fadeOutContainer 0.4s cubic-bezier(0.4, 0, 0.2, 1) 1.15s forwards;
}
@keyframes fadeOutContainer {
    to {
        opacity: 0;
        visibility: hidden;
    }
}
.splash-logo-wrapper {
    position: relative;
    width: 64px;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
}
.splash-logo-svg {
    width: 100%;
    height: 100%;
    color: #38BDF8;
    filter: drop-shadow(0 0 16px rgba(56, 189, 248, 0.45));
}
.splash-title-text {
    font-size: 1.5rem;
    font-weight: 500;
    letter-spacing: -0.025em;
    color: #ffffff;
    margin: 0;
}
.splash-title-text span {
    color: #38BDF8;
    font-weight: 600;
}
</style>
<div id="splash-screen" class="splash-exit">
<div class="ambient-glow"></div>
<div class="splash-logo-wrapper">
<svg class="splash-logo-svg" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
<path class="logo-path" d="M16 52V12H36C43.732 12 50 18.268 50 26C50 33.732 43.732 40 36 40H16" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<path class="logo-path" style="animation-delay: 0.22s;" d="M34 40L50 52" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>
<path class="logo-path" style="animation-delay: 0.38s;" d="M36 12L45 6M36 40L45 46M16 12L10 6M16 52L10 58" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
</svg>
</div>
<div class="fade-scale-in">
<h1 class="splash-title-text">Ret<span>AI</span>n</h1>
</div>
<p class="tagline-fade">Anticipate turnover, anchor your talent.</p>
<div class="splash-progress-container">
<div class="progress-bar-fill"></div>
</div>
</div>"""

        st.markdown(html_content, unsafe_allow_html=True)
        st.session_state.splash_shown = True
