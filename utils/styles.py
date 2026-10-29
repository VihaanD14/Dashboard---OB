import streamlit as st

def apply_custom_css():
    st.markdown("""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..700&family=Instrument+Sans:ital,wght@0,400..600;1,400..600&display=swap" rel="stylesheet">""", unsafe_allow_html=True)
    st.markdown("""<style>
        /* ==========================================================================
           Google Fonts Variables & Global Shell Performance
           ========================================================================== */
        :root {
            --font-display: 'Bricolage Grotesque', sans-serif;
            --font-body: 'Instrument Sans', sans-serif;
        }

        /* Hardware-accelerated fluid page/tab transitions & ultra-smooth scrolling */
        html {
            scroll-behavior: smooth;
        }

        section[data-testid="stMain"] {
            scroll-behavior: smooth;
            -webkit-overflow-scrolling: touch;
        }

        iframe {
            will-change: transform;
            transform: translateZ(0);
            backface-visibility: hidden;
        }

        [data-testid="stMainBlockContainer"] {
            animation: tabFadeIn 160ms cubic-bezier(0.16, 1, 0.3, 1) both;
            will-change: opacity, transform;
        }

        @keyframes tabFadeIn {
            0% {
                opacity: 0.88;
                transform: translateY(3px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* ==========================================================================
           NEONE Aesthetic Theme - Deep Cosmic Obsidian, Glassmorphism & Electric Cyan
           ========================================================================== */

        /* Base Application Shell with ONE Seamless, Continuous Background */
        .stApp {
            background: radial-gradient(ellipse at 50% 15%, rgba(56, 189, 248, 0.18) 0%, rgba(14, 165, 233, 0.05) 50%, #030712 85%) !important;
            background-color: #030712 !important;
            color: #F8FAFC !important;
            font-family: var(--font-body) !important;
        }

        /* Streamlit Native Elements, Widgets & Typography Overrides */
        .stApp,
        input,
        textarea,
        select,
        button,
        label,
        div[data-baseweb="input"] input,
        div[data-baseweb="select"],
        div[data-baseweb="base-input"],
        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox,
        div[data-testid="stWidgetLabel"] label,
        div[data-testid="stWidgetLabel"] p,
        div[data-testid="stButton"] button,
        div[data-testid="stDownloadButton"] button,
        div[data-testid="stFormSubmitButton"] button,
        div[data-testid="stTabContent"] button,
        div[data-testid="stTabs"] button,
        [data-testid="stBaseButton-primary"],
        [data-testid="stBaseButton-secondary"],
        [data-testid="baseButton-primary"],
        [data-testid="baseButton-secondary"],
        .naked-nav-links,
        .naked-nav-link,
        .naked-signin-text,
        .naked-book-demo-btn,
        .neone-pill-btn,
        .naked-telemetry-btn,
        .subtitle,
        .hero-desc,
        .pulse-desc,
        .pipeline-desc,
        .framer-card-desc,
        .brand-tag,
        .portal-tag,
        .hero-badge,
        .pulse-tag,
        .framer-step-num,
        .framer-metric-chip,
        .pipeline-label,
        .pipeline-meta,
        .proof-label,
        .metric-label,
        [data-testid="stMetricLabel"],
        .tedy-user-role,
        .tedy-quote,
        .tedy-status-pill,
        .wp-live {
            font-family: var(--font-body) !important;
        }

        /* Section Headlines & Card/Box Titles */
        h1, h2,
        .hero-title,
        .section-title,
        .pulse-title,
        .framer-card-title,
        .pipeline-title,
        .card-title,
        .box-title,
        .bento-title,
        .metric-title {
            font-family: var(--font-display) !important;
            font-weight: 700;
            letter-spacing: -0.01em !important;
        }

        /* EXCLUSIONS */
        /* 1. RetAIn Logo Text MUST NOT change font */
        .brand-title,
        .brand-title *,
        .naked-brand-link,
        .naked-brand-link *,
        .brand-spark,
        .brand-ai,
        #nav-brand-link,
        #nav-brand-link *,
        .splash-title-text,
        .splash-title-text * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }

        /* 2. WhatsApp Message Cards in Hero MUST NOT change font */
        .wa-card,
        .wa-card *,
        .wa-sender,
        .wa-body,
        .wa-meta,
        .wa-ticks,
        .wa-reactions-pill {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
        }

        .naked-nav-container, header[data-testid="stHeader"] {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }

        /* Hide Streamlit Native Vertical Sidebar, Nav & Controls */
        [data-testid="stSidebarNav"],
        section[data-testid="stSidebar"],
        .stSidebar,
        button[data-testid="baseButton-headerNoPadding"],
        [data-testid="stSidebarCollapseButton"],
        div[data-testid="collapsedControl"] {
            display: none !important;
            visibility: hidden !important;
            width: 0px !important;
            height: 0px !important;
            position: absolute !important;
            left: -9999px !important;
            pointer-events: none !important;
        }

        /* Hide zero-height helper script iframes */
        iframe[height="0"],
        div[data-testid="stElementContainer"]:has(iframe[height="0"]),
        div[data-testid="stIFrame"]:has(iframe[height="0"]) {
            display: none !important;
            height: 0px !important;
            margin: 0px !important;
            padding: 0px !important;
        }

        /* ==========================================================================
           Streamlit Header & System Clutter Removal
           Hide Streamlit running person status widget, hamburger menu, and footer
           ========================================================================== */
        [data-testid="stStatusWidget"], 
        .stStatusWidget {
            visibility: hidden !important;
            display: none !important;
        }

        /* Hide default Streamlit toolbar and footer */
        #MainMenu, header[data-testid="stHeader"], footer, [data-testid="stToolbar"], div[data-testid="stDecoration"] {
            visibility: hidden !important;
            display: none !important;
        }

        header[data-testid="stHeader"] {
            display: none !important;
            height: 0px !important;
            min-height: 0px !important;
            padding: 0 !important;
        }

        /* Main Content Container Stabilization */
        /* For Portal / Dashboard tabs: Elegant centered container with comfortable padding so text never cuts into the left edge */
        div.block-container,
        div[data-testid="stMainBlockContainer"],
        div.stMainBlockContainer {
            max-width: 1360px !important;
            width: 100% !important;
            margin-left: auto !important;
            margin-right: auto !important;
            padding-left: clamp(2rem, 4vw, 3.5rem) !important;
            padding-right: clamp(2rem, 4vw, 3.5rem) !important;
            padding-top: 1rem !important;
            padding-bottom: 85px !important;
            box-sizing: border-box !important;
            animation: none !important;
            transform: none !important;
        }

        /* Allow Homepage full-bleed interactive canvas iframes to span 100% edge-to-edge with NO side borders/margins */
        div.block-container:has(#homepage-root),
        div[data-testid="stMainBlockContainer"]:has(#homepage-root),
        section.stMain:has(#homepage-root) div.block-container,
        div.block-container:has(iframe[height="750"]),
        div.block-container:has(iframe[height="780"]),
        div[data-testid="stMainBlockContainer"]:has(iframe[height="750"]),
        div[data-testid="stMainBlockContainer"]:has(iframe[height="780"]) {
            max-width: 100% !important;
            width: 100% !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
            margin: 0 !important;
        }

        /* Full width for large interactive canvas iframe element containers on homepage */
        div[data-testid="stElementContainer"]:has(iframe[height="750"]),
        div[data-testid="stElementContainer"]:has(iframe[height="780"]),
        div.element-container:has(iframe[height="750"]),
        div.element-container:has(iframe[height="780"]),
        div[data-testid="stIFrame"]:has(iframe[height="750"]),
        div[data-testid="stIFrame"]:has(iframe[height="780"]) {
            width: 100% !important;
            max-width: 100% !important;
            margin-left: 0 !important;
            margin-right: 0 !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
        }

        /* Remove default Streamlit vertical block gaps between homepage full-bleed canvas sections */
        div[data-testid="stMainBlockContainer"]:has(#homepage-root) > div[data-testid="stVerticalBlock"],
        div[data-testid="stMainBlockContainer"]:has(iframe[height="750"]) > div[data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }

        /* Ensure Iframes span full width edge-to-edge */
        div[data-testid="stIFrame"] iframe,
        div[data-testid="stElementContainer"] iframe,
        iframe {
            width: 100% !important;
            max-width: 100% !important;
            display: block !important;
            border: none !important;
        }

        /* Hide Skeleton Placeholder Flicker */
        [data-testid="stSkeleton"],
        .stSkeleton {
            display: none !important;
        }

        /* ==========================================================================
           Seamless Merged Top Navigation Bar (NEONE Aesthetic)
           Floating Glass Capsule & Constrained 1200px Centered Container
           ========================================================================== */
        /* Top Navigation Bar (Constrained 1200px Centered Container - Normal Flow / Scrolls naturally) */
        div[data-testid="stElementContainer"]:has(.naked-nav-container),
        div.element-container:has(.naked-nav-container) {
            position: relative !important;
            top: auto !important;
            z-index: 999 !important;
            pointer-events: auto !important;
        }

        .naked-nav-container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 16px 24px;
            box-sizing: border-box;
            position: relative;
            z-index: 999999;
            pointer-events: auto !important;
            background: transparent !important;
            backdrop-filter: none !important;
            -webkit-backdrop-filter: none !important;
            border: none !important;
            border-bottom: none !important;
            box-shadow: none !important;
            transition: padding 200ms ease;
        }

        /* Align portal navbar cleanly with the portal content below it */
        div.block-container:not(:has(#homepage-root)):not(:has(iframe[height="750"])) .naked-nav-container,
        div[data-testid="stMainBlockContainer"]:not(:has(#homepage-root)):not(:has(iframe[height="750"])) .naked-nav-container {
            max-width: 100% !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            padding-top: 14px !important;
            padding-bottom: 14px !important;
        }

        /* Streamlit Tabs Polish - Ensure tabs have proper left margin and spacing */
        div[data-testid="stTabs"] {
            margin-top: 0.5rem;
            margin-bottom: 1.5rem;
        }

        div[data-testid="stTabs"] [data-baseweb="tab-list"] {
            gap: 8px !important;
            background-color: transparent !important;
            border-bottom: 1px solid rgba(56, 189, 248, 0.2) !important;
            padding-bottom: 4px !important;
        }

        div[data-testid="stTabs"] button[role="tab"] {
            padding: 8px 18px !important;
            font-size: 0.92rem !important;
            font-weight: 500 !important;
            color: #94A3B8 !important;
            border-radius: 8px 8px 0 0 !important;
            transition: all 0.2s ease !important;
        }

        div[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
            color: #38BDF8 !important;
            background-color: rgba(56, 189, 248, 0.1) !important;
            border-bottom: 2px solid #38BDF8 !important;
            font-weight: 600 !important;
        }

        .naked-nav-inner {
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-sizing: border-box;
        }

        .naked-nav-brand {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            flex: 1;
            justify-content: flex-start;
            flex-shrink: 0;
        }

        .brand-title,
        .naked-brand-link {
            color: #F8FAFC !important;
            text-decoration: none !important;
            font-size: 1.25rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }

        .brand-logo-icon {
            width: 22px;
            height: 22px;
            color: #38BDF8;
            filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.45));
            flex-shrink: 0;
            display: inline-block;
            vertical-align: middle;
        }

        .brand-spark {
            color: #38BDF8;
            font-size: 1.05rem;
            text-shadow: 0 0 12px rgba(56, 189, 248, 0.85);
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }

        .brand {
            color: #F8FAFC !important;
            font-weight: 700;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            letter-spacing: -0.02em;
        }

        .brand-ai {
            color: #38BDF8 !important;
            font-weight: 800 !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }

        .brand-tag {
            font-size: 0.65rem;
            color: #94A3B8;
            background: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.22);
            border-radius: 9999px;
            padding: 0.15rem 0.55rem;
            font-weight: 500;
            letter-spacing: 0.03em;
            text-transform: uppercase;
        }

        /* Floating Center Glass Pill Container */
        .naked-nav-links {
            height: 44px !important;
            box-sizing: border-box !important;
            background: rgba(255, 255, 255, 0.04) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(56, 189, 248, 0.25) !important;
            border-radius: 9999px !important;
            padding: 0 16px !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 4px !important;
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.12), inset 0 1px 0 0 rgba(255, 255, 255, 0.08) !important;
            position: relative !important;
            transition: padding 200ms ease, background 200ms ease, border-color 200ms ease, box-shadow 200ms ease !important;
            margin: 0 !important;
            flex-shrink: 0 !important;
        }

        /* Scrolled state: reduce pill padding by ~12%, faint cyan border */
        .naked-nav-container.nav-scrolled .naked-nav-links {
            padding: 0 14px !important;
            background: rgba(255, 255, 255, 0.05) !important;
            border-color: rgba(56, 189, 248, 0.30) !important;
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.14) !important;
        }

        /* Soft hover state with subtle cyan accent glow */
        .naked-nav-links:hover {
            border-color: rgba(56, 189, 248, 0.40) !important;
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.18), inset 0 1px 0 0 rgba(255, 255, 255, 0.12) !important;
        }

        /* Subtle cyan-tinted highlight sliding behind links */
        .nav-sliding-indicator {
            position: absolute;
            top: 0;
            left: 0;
            border-radius: 9999px;
            background: rgba(56, 189, 248, 0.15) !important;
            border: 1px solid rgba(56, 189, 248, 0.20);
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.15);
            pointer-events: none;
            z-index: 1;
            opacity: 0;
            transition: transform 250ms cubic-bezier(0.16, 1, 0.3, 1),
                        width 250ms cubic-bezier(0.16, 1, 0.3, 1),
                        height 250ms cubic-bezier(0.16, 1, 0.3, 1),
                        opacity 250ms ease;
        }

        .naked-nav-link {
            position: relative;
            z-index: 2;
            color: rgba(255, 255, 255, 0.70) !important;
            text-decoration: none !important;
            font-size: 0.88rem;
            font-weight: 500;
            padding: 6px 14px;
            border-radius: 9999px;
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
            transition: color 200ms ease;
            white-space: nowrap;
            display: inline-flex;
            align-items: center;
        }

        .naked-nav-link:hover {
            color: #FFFFFF !important;
            background: transparent !important;
            box-shadow: none !important;
            text-shadow: none !important;
        }

        .naked-nav-link.active {
            color: #22D3EE !important;
            background: transparent !important;
            box-shadow: none !important;
            text-shadow: 0 0 10px rgba(34, 211, 238, 0.4) !important;
        }

        .naked-nav-link.nav-active-pending {
            color: #22D3EE !important;
            font-weight: 600 !important;
        }

        #nav-loading-bar {
            position: fixed;
            top: 0;
            left: 0;
            height: 2.5px;
            width: 0%;
            background: linear-gradient(90deg, #38BDF8, #818CF8, #C084FC);
            box-shadow: 0 0 10px rgba(56, 189, 248, 0.8), 0 0 5px rgba(129, 140, 248, 0.6);
            z-index: 999999999;
            pointer-events: none;
            transition: width 0.3s cubic-bezier(0.1, 0.8, 0.3, 1), opacity 0.3s ease;
            opacity: 0;
        }

        /* 5px dot with a slow, subtle pulse */
        .nav-live-dot {
            display: inline-block;
            width: 5px;
            height: 5px;
            background-color: #10B981;
            border-radius: 50%;
            margin-right: 6px;
            box-shadow: none !important;
            animation: nav-dot-pulse 3s infinite ease-in-out;
            flex-shrink: 0;
        }

        @keyframes nav-dot-pulse {
            0%, 100% {
                opacity: 0.6;
                transform: scale(1);
            }
            50% {
                opacity: 1;
                transform: scale(1.15);
            }
        }

        /* Right Side Actions: Plain Sign In + Solid Book a Demo Button */
        .naked-nav-cta {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            gap: 16px;
            flex: 1;
            flex-shrink: 0;
        }

        /* Plain "Sign in" text link: soft white, turning cyan on hover */
        .naked-signin-text {
            color: rgba(255, 255, 255, 0.85) !important;
            text-decoration: none !important;
            font-size: 0.88rem;
            font-weight: 500;
            transition: color 180ms ease, text-shadow 180ms ease;
            background: transparent !important;
            border: none !important;
            padding: 0;
            cursor: pointer;
            white-space: nowrap;
        }

        .naked-signin-text:hover {
            color: #22D3EE !important;
            text-shadow: 0 0 10px rgba(34, 211, 238, 0.55) !important;
        }

        /* Neon "Book a demo" button: bright cyan fill (#22d3ee), layered cyan glow */
        .naked-book-demo-btn {
            height: 44px;
            box-sizing: border-box;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0 18px;
            background: #22D3EE !important;
            color: #030712 !important;
            font-size: 0.88rem;
            font-weight: 700;
            border-radius: 10px !important;
            border: 1px solid rgba(34, 211, 238, 0.8) !important;
            box-shadow: 0 0 12px rgba(34, 211, 238, 0.50), 0 0 28px rgba(34, 211, 238, 0.50) !important;
            text-shadow: none !important;
            text-decoration: none !important;
            transition: background 180ms ease, transform 180ms ease, box-shadow 180ms ease;
            cursor: pointer;
            white-space: nowrap;
        }

        .naked-book-demo-btn:hover {
            background: #67E8F9 !important;
            color: #030712 !important;
            transform: translateY(-1px);
            box-shadow: 0 0 16px rgba(34, 211, 238, 0.80), 0 0 36px rgba(34, 211, 238, 0.65) !important;
        }

        .neone-pill-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            font-size: 0.84rem;
            font-weight: 600;
            color: #030712 !important;
            text-decoration: none !important;
            background: #FFFFFF;
            border: 1px solid rgba(255, 255, 255, 0.9);
            border-radius: 9999px;
            padding: 0.45rem 1.25rem;
            box-shadow: 0 0 16px rgba(255, 255, 255, 0.35), 0 0 24px rgba(56, 189, 248, 0.25);
            transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .neone-pill-btn:hover {
            background: #E0F2FE;
            color: #030712 !important;
            box-shadow: 0 0 24px rgba(255, 255, 255, 0.5), 0 0 32px rgba(56, 189, 248, 0.5);
            transform: translateY(-1px);
        }

        .portal-tag {
            background: rgba(16, 185, 129, 0.1) !important;
            color: #10B981 !important;
            border-color: rgba(16, 185, 129, 0.3) !important;
        }

        .naked-telemetry-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            font-size: 0.78rem;
            font-weight: 600;
            color: #38BDF8 !important;
            text-decoration: none !important;
            background: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.28);
            border-radius: 9999px;
            padding: 0.35rem 0.85rem;
            transition: all 0.2s ease;
        }

        .naked-telemetry-btn:hover {
            background: rgba(56, 189, 248, 0.16);
            border-color: rgba(56, 189, 248, 0.5);
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.3);
            color: #FFFFFF !important;
        }

        .telemetry-dot {
            width: 6px;
            height: 6px;
            background-color: #10B981;
            border-radius: 50%;
            box-shadow: 0 0 8px #10B981;
            display: inline-block;
        }

        /* ==========================================================================
           Typography & Headings
           ========================================================================== */
        h1, h2, h3, h4, h5, h6 {
            color: #F8FAFC !important;
            font-family: var(--font-display) !important;
            font-weight: 700;
            letter-spacing: -0.01em !important;
        }

        h1 {
            background: -webkit-linear-gradient(45deg, #F8FAFC 25%, #38BDF8 85%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            font-family: var(--font-display) !important;
            font-weight: 700 !important;
            letter-spacing: -0.01em !important;
        }

        h2 {
            font-family: var(--font-display) !important;
            font-weight: 700 !important;
            letter-spacing: -0.01em !important;
        }

        .subtitle {
            color: #94A3B8 !important;
            font-size: 1.05rem !important;
            margin-bottom: 1.85rem !important;
            font-weight: 400 !important;
            letter-spacing: 0.01em !important;
            font-family: var(--font-body) !important;
        }

        /* ==========================================================================
           Hero Section Styling (NEONE Celestial Arc)
           ========================================================================== */
        .hero-container {
            text-align: center;
            padding: 3rem 1.5rem 2.5rem 1.5rem;
            max-width: 900px;
            margin: 0 auto;
            position: relative;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.28);
            border-radius: 9999px;
            padding: 0.35rem 1.1rem;
            color: #38BDF8;
            font-size: 0.82rem;
            font-weight: 500;
            letter-spacing: 0.03em;
            margin-bottom: 1.5rem;
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.15);
        }

        .hero-title {
            font-family: var(--font-display) !important;
            font-size: 3.2rem;
            font-weight: 700;
            line-height: 1.15;
            letter-spacing: -0.01em;
            margin-bottom: 1.25rem;
            color: #F8FAFC;
        }

        .hero-title-highlight {
            background: linear-gradient(135deg, #38BDF8 0%, #818CF8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-desc {
            font-size: 1.15rem;
            color: #94A3B8;
            line-height: 1.65;
            max-width: 720px;
            margin: 0 auto 2rem auto;
            font-weight: 400;
        }

        .hero-actions {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1.25rem;
            margin-bottom: 2.5rem;
        }

        /* ==========================================================================
           Card Glassmorphism (.metric-card, .glass-card, st.metric containers)
           ========================================================================== */
        .metric-card,
        .glass-card,
        .stMetric,
        div[data-testid="stMetric"],
        div[data-testid="metric-container"] {
            background: rgba(11, 15, 25, 0.75) !important;
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
            border: 1px solid rgba(56, 189, 248, 0.18) !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.6), 0 0 1px rgba(56, 189, 248, 0.2) !important;
            padding: 1.15rem 1.35rem !important;
            color: #F8FAFC !important;
            transition: border-color 0.24s cubic-bezier(0.16, 1, 0.3, 1),
                        box-shadow 0.24s cubic-bezier(0.16, 1, 0.3, 1),
                        transform 0.24s cubic-bezier(0.16, 1, 0.3, 1) !important;
        }

        .metric-card:hover,
        .glass-card:hover,
        .stMetric:hover,
        div[data-testid="stMetric"]:hover,
        div[data-testid="metric-container"]:hover {
            border-color: rgba(56, 189, 248, 0.42) !important;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.75), 0 0 16px rgba(56, 189, 248, 0.32) !important;
            transform: translateY(-1px) !important;
        }

        /* Metric Labels & Subtitles */
        div[data-testid="stMetric"] label,
        div[data-testid="stMetric"] [data-testid="stMetricLabel"],
        div[data-testid="metric-container"] > div > div:nth-child(1),
        [data-testid="stMetricLabel"],
        .metric-label {
            color: #94A3B8 !important;
            font-size: 0.88rem !important;
            font-weight: 500 !important;
            letter-spacing: 0.02em !important;
            margin-bottom: 0.35rem !important;
        }

        div[data-testid="stMetric"] label p,
        div[data-testid="stMetric"] [data-testid="stMetricLabel"] p {
            color: #94A3B8 !important;
            font-size: 0.88rem !important;
            margin: 0 !important;
        }

        /* Metric Values */
        div[data-testid="stMetric"] [data-testid="stMetricValue"],
        div[data-testid="metric-container"] > div > div:nth-child(2),
        [data-testid="stMetricValue"],
        .metric-value {
            color: #F8FAFC !important;
            font-size: 1.85rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em !important;
            text-shadow: 0 0 18px rgba(56, 189, 248, 0.15) !important;
        }

        div[data-testid="stMetric"] [data-testid="stMetricValue"] * {
            color: #F8FAFC !important;
        }

        /* Metric Deltas */
        [data-testid="stMetricDelta"],
        .delta-positive {
            color: #10B981 !important;
            font-weight: 500 !important;
            font-size: 0.85rem !important;
        }

        div[data-testid="stMetricDelta"]:has(svg[data-testid="stMetricDeltaIcon-Up"]) {
            color: #10B981 !important;
        }

        div[data-testid="stMetricDelta"]:has(svg[data-testid="stMetricDeltaIcon-Down"]),
        .delta-negative {
            color: #F43F5E !important;
            font-weight: 500 !important;
            font-size: 0.85rem !important;
        }

        /* ==========================================================================
           Executive Pulse Brief & Highlights Cards
           ========================================================================== */
        .pulse-card {
            background: rgba(11, 15, 25, 0.75);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(56, 189, 248, 0.18);
            border-radius: 12px;
            padding: 1.3rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            transition: all 0.22s ease;
        }

        .pulse-card:hover {
            border-color: rgba(56, 189, 248, 0.4);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7), 0 0 14px rgba(56, 189, 248, 0.25);
            transform: translateY(-1px);
        }

        .pulse-tag {
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            padding: 0.2rem 0.6rem;
            border-radius: 9999px;
            display: inline-block;
            margin-bottom: 0.75rem;
        }

        .pulse-tag-danger {
            background: rgba(244, 63, 94, 0.15);
            color: #F43F5E;
            border: 1px solid rgba(244, 63, 94, 0.35);
        }

        .pulse-tag-warning {
            background: rgba(251, 191, 36, 0.15);
            color: #FBBF24;
            border: 1px solid rgba(251, 191, 36, 0.35);
        }

        .pulse-tag-success {
            background: rgba(16, 185, 129, 0.15);
            color: #10B981;
            border: 1px solid rgba(16, 185, 129, 0.35);
        }

        .pulse-tag-cyan {
            background: rgba(56, 189, 248, 0.15);
            color: #38BDF8;
            border: 1px solid rgba(56, 189, 248, 0.35);
        }

        .pulse-title {
            color: #F8FAFC;
            font-family: var(--font-display) !important;
            font-size: 1.05rem;
            font-weight: 600;
            letter-spacing: -0.01em;
            margin-bottom: 0.45rem;
        }

        .pulse-desc {
            color: #94A3B8;
            font-size: 0.88rem;
            line-height: 1.55;
            margin: 0;
        }

        /* ==========================================================================
           Tedy-Inspired Floating Cards & Hero Showcase
           ========================================================================== */
        .tedy-hero-wrapper {
            position: relative;
            padding: 2.5rem 1rem 1.5rem 1rem;
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
        }

        .tedy-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.25rem;
            max-width: 1160px;
            margin: 2.5rem auto 1rem auto;
            perspective: 1000px;
        }

        .tedy-card {
            background: rgba(11, 15, 25, 0.78);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(56, 189, 248, 0.18);
            border-radius: 16px;
            padding: 1.35rem 1.45rem;
            text-align: left;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.55), 0 0 1px rgba(56, 189, 248, 0.2);
            transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
        }

        .tedy-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.4), transparent);
        }

        .tedy-card-float-1 {
            animation: tedyFloatA 6s ease-in-out infinite;
        }

        .tedy-card-float-2 {
            animation: tedyFloatB 7s ease-in-out infinite 0.7s;
        }

        .tedy-card-float-3 {
            animation: tedyFloatA 6.5s ease-in-out infinite 1.4s;
        }

        .tedy-card-float-4 {
            animation: tedyFloatB 7.5s ease-in-out infinite 2.1s;
        }

        @keyframes tedyFloatA {
            0%, 100% { transform: translateY(0px) rotate(-0.5deg); }
            50% { transform: translateY(-7px) rotate(0.5deg); }
        }

        @keyframes tedyFloatB {
            0%, 100% { transform: translateY(0px) rotate(0.5deg); }
            50% { transform: translateY(-9px) rotate(-0.5deg); }
        }

        .tedy-card:hover {
            transform: translateY(-5px) scale(1.02) !important;
            border-color: rgba(56, 189, 248, 0.5) !important;
            box-shadow: 0 14px 40px rgba(0, 0, 0, 0.75), 0 0 20px rgba(56, 189, 248, 0.35) !important;
            z-index: 10;
        }

        .tedy-card-header {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 0.85rem;
        }

        .tedy-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.82rem;
            background: linear-gradient(135deg, rgba(56, 189, 248, 0.2), rgba(96, 165, 250, 0.2));
            border: 1px solid rgba(56, 189, 248, 0.35);
            color: #38BDF8;
            flex-shrink: 0;
        }

        .tedy-user-info {
            flex-grow: 1;
        }

        .tedy-user-name {
            font-size: 0.9rem;
            font-weight: 600;
            color: #F8FAFC;
            line-height: 1.2;
        }

        .tedy-user-role {
            font-size: 0.74rem;
            color: #94A3B8;
        }

        .tedy-quote {
            font-size: 0.88rem;
            color: #CBD5E1;
            line-height: 1.5;
            margin-bottom: 0.9rem;
            font-style: italic;
        }

        .tedy-status-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.03em;
            padding: 0.22rem 0.65rem;
            border-radius: 9999px;
            text-transform: uppercase;
        }

        .tedy-status-danger {
            background: rgba(244, 63, 94, 0.12);
            color: #F43F5E;
            border: 1px solid rgba(244, 63, 94, 0.3);
        }

        .tedy-status-warning {
            background: rgba(251, 191, 36, 0.12);
            color: #FBBF24;
            border: 1px solid rgba(251, 191, 36, 0.3);
        }

        .tedy-status-success {
            background: rgba(16, 185, 129, 0.12);
            color: #10B981;
            border: 1px solid rgba(16, 185, 129, 0.3);
        }

        /* Proof / Credibility Counters */
        .proof-strip {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 1.5rem;
            max-width: 1420px;
            margin: 0.5rem auto 3.5rem auto;
        }

        .proof-card {
            background: rgba(11, 15, 25, 0.65);
            border: 1px solid rgba(56, 189, 248, 0.15);
            border-radius: 12px;
            padding: 1.25rem;
            text-align: center;
            transition: all 0.2s ease;
        }

        .proof-card:hover {
            border-color: rgba(56, 189, 248, 0.35);
            transform: translateY(-2px);
        }

        .proof-value {
            font-size: 2.1rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, #F8FAFC 30%, #38BDF8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .proof-label {
            font-size: 0.82rem;
            color: #94A3B8;
            margin-top: 0.35rem;
            font-weight: 500;
        }

        /* Framer Horizontal Track & Process Showcase */
        .framer-track {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 3.5rem;
        }

        .framer-card {
            background: rgba(11, 15, 25, 0.75);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(56, 189, 248, 0.18);
            border-radius: 16px;
            padding: 2rem 1.75rem;
            position: relative;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.5);
        }

        .framer-card:hover {
            border-color: rgba(56, 189, 248, 0.5);
            box-shadow: 0 10px 36px rgba(0, 0, 0, 0.7), 0 0 20px rgba(56, 189, 248, 0.3);
            transform: translateY(-3px);
        }

        .framer-step-num {
            font-size: 0.75rem;
            font-weight: 700;
            color: #38BDF8;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.85rem;
        }

        .framer-card-title {
            font-family: var(--font-display) !important;
            font-size: 1.35rem;
            font-weight: 700;
            letter-spacing: -0.01em;
            color: #F8FAFC;
            margin-bottom: 0.75rem;
            line-height: 1.25;
        }

        .framer-card-desc {
            font-size: 0.92rem;
            color: #94A3B8;
            line-height: 1.6;
            margin-bottom: 1.5rem;
        }

        .framer-metric-chip {
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 600;
            color: #38BDF8;
            background: rgba(56, 189, 248, 0.08);
            border: 1px solid rgba(56, 189, 248, 0.25);
            border-radius: 9999px;
            padding: 0.25rem 0.75rem;
            margin-bottom: 1rem;
        }

        .framer-card-link {
            color: #38BDF8 !important;
            text-decoration: none !important;
            font-size: 0.88rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            transition: gap 0.2s ease;
        }

        .framer-card-link:hover {
            gap: 0.55rem;
            color: #FFFFFF !important;
        }

        /* Comparison Matrix (Why Us) */
        .comparison-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
            max-width: 1000px;
            margin: 2rem auto 3.5rem auto;
        }

        .comp-box-legacy {
            background: rgba(15, 23, 42, 0.45);
            border: 1px solid rgba(148, 163, 184, 0.15);
            border-radius: 14px;
            padding: 1.75rem;
        }

        .comp-box-retain {
            background: rgba(11, 15, 25, 0.85);
            border: 1px solid rgba(56, 189, 248, 0.35);
            border-radius: 14px;
            padding: 1.75rem;
            box-shadow: 0 0 24px rgba(56, 189, 248, 0.18);
            position: relative;
        }

        .comp-box-retain::before {
            content: '✦ AI NATIVE';
            position: absolute;
            top: -10px;
            right: 20px;
            font-size: 0.65rem;
            font-weight: 700;
            background: linear-gradient(135deg, #0284C7, #38BDF8);
            color: #FFFFFF;
            padding: 0.2rem 0.65rem;
            border-radius: 9999px;
        }

        /* ==========================================================================
           Plotly Chart & Data Table Integration
           ========================================================================== */
        .stPlotlyChart,
        .js-plotly-plot,
        .plotly,
        .plot-container,
        .main-svg {
            background: transparent !important;
            background-color: transparent !important;
            border: none !important;
        }

        .stDataFrame,
        [data-testid="stTable"],
        div[data-testid="stDataFrame"] {
            background-color: rgba(11, 15, 25, 0.85) !important;
            border: 1px solid rgba(56, 189, 248, 0.18) !important;
            border-radius: 12px !important;
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
            padding: 10px !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5) !important;
        }

        [data-testid="stDataFrame"] th,
        [data-testid="stTable"] th {
            background-color: rgba(15, 23, 42, 0.95) !important;
            color: #94A3B8 !important;
            font-weight: 600 !important;
            border-bottom: 1px solid rgba(56, 189, 248, 0.22) !important;
        }

        [data-testid="stDataFrame"] td,
        [data-testid="stTable"] td {
            color: #F8FAFC !important;
            border-bottom: 1px solid rgba(56, 189, 248, 0.08) !important;
        }

        tr:hover td,
        div[role="row"]:hover {
            background-color: rgba(56, 189, 248, 0.09) !important;
            transition: background-color 0.15s ease !important;
        }

        /* ==========================================================================
           Interactive Controls: Primary & Secondary Buttons
           ========================================================================== */
        div[data-testid="stTabContent"] button[kind="primary"],
        div[data-testid="stTabContent"] [data-testid="stBaseButton-primary"],
        div[data-testid="stTabContent"] [data-testid="baseButton-primary"],
        div[data-testid="stTabs"] button[kind="primary"],
        div[data-testid="stTabs"] [data-testid="stBaseButton-primary"],
        button[kind="primary"],
        [data-testid="stBaseButton-primary"],
        [data-testid="baseButton-primary"],
        div[data-testid="stButton"] > button[kind="primary"],
        div[data-testid="stDownloadButton"] > button[kind="primary"],
        div[data-testid="stFormSubmitButton"] > button[kind="primary"] {
            background: linear-gradient(135deg, #0284C7 0%, #38BDF8 100%) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
            font-size: 0.93rem !important;
            letter-spacing: 0.015em !important;
            border-radius: 10px !important;
            padding: 0.55rem 1.35rem !important;
            border: 1px solid rgba(255, 255, 255, 0.28) !important;
            box-shadow: 0 4px 18px 0 rgba(56, 189, 248, 0.42),
                        0 0 10px rgba(56, 189, 248, 0.25),
                        inset 0 1px 1px 0 rgba(255, 255, 255, 0.35),
                        inset 0 -1px 2px 0 rgba(0, 0, 0, 0.32) !important;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.35) !important;
            cursor: pointer !important;
            transition: transform 0.14s cubic-bezier(0.4, 0, 0.2, 1),
                        box-shadow 0.14s cubic-bezier(0.4, 0, 0.2, 1),
                        background 0.14s cubic-bezier(0.4, 0, 0.2, 1),
                        border-color 0.14s cubic-bezier(0.4, 0, 0.2, 1) !important;
        }

        div[data-testid="stTabContent"] button[kind="primary"]:hover,
        div[data-testid="stTabContent"] [data-testid="stBaseButton-primary"]:hover,
        div[data-testid="stTabContent"] [data-testid="baseButton-primary"]:hover,
        div[data-testid="stTabs"] button[kind="primary"]:hover,
        div[data-testid="stTabs"] [data-testid="stBaseButton-primary"]:hover,
        button[kind="primary"]:hover,
        [data-testid="stBaseButton-primary"]:hover,
        [data-testid="baseButton-primary"]:hover,
        div[data-testid="stButton"] > button[kind="primary"]:hover,
        div[data-testid="stDownloadButton"] > button[kind="primary"]:hover,
        div[data-testid="stFormSubmitButton"] > button[kind="primary"]:hover {
            background: linear-gradient(135deg, #0369A1 0%, #38BDF8 100%) !important;
            border-color: rgba(255, 255, 255, 0.5) !important;
            box-shadow: 0 6px 24px 0 rgba(56, 189, 248, 0.58),
                        0 0 18px 2px rgba(56, 189, 248, 0.4),
                        inset 0 1px 1.5px 0 rgba(255, 255, 255, 0.5) !important;
            transform: translateY(-1px) !important;
            color: #FFFFFF !important;
        }

        div[data-testid="stTabContent"] button[kind="secondary"],
        div[data-testid="stTabContent"] [data-testid="stBaseButton-secondary"],
        button[kind="secondary"],
        [data-testid="stBaseButton-secondary"],
        div[data-testid="stButton"] > button[kind="secondary"] {
            background: rgba(11, 15, 25, 0.75) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            color: #F8FAFC !important;
            font-weight: 500 !important;
            border-radius: 10px !important;
            border: 1px solid rgba(56, 189, 248, 0.2) !important;
            box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.3) !important;
            transition: all 0.15s ease !important;
        }

        div[data-testid="stTabContent"] button[kind="secondary"]:hover,
        button[kind="secondary"]:hover,
        [data-testid="stBaseButton-secondary"]:hover,
        div[data-testid="stButton"] > button[kind="secondary"]:hover {
            background: rgba(15, 23, 42, 0.95) !important;
            border-color: rgba(56, 189, 248, 0.45) !important;
            box-shadow: 0 0 14px rgba(56, 189, 248, 0.22) !important;
            transform: translateY(-1px) !important;
            color: #FFFFFF !important;
        }

        /* Form Controls & Inputs */
        div[data-baseweb="input"],
        div[data-baseweb="select"] > div,
        .stTextInput > div > div,
        .stSelectbox > div > div,
        .stTextArea textarea {
            background-color: rgba(11, 15, 25, 0.85) !important;
            border: 1px solid rgba(56, 189, 248, 0.2) !important;
            border-radius: 9px !important;
            color: #F8FAFC !important;
        }

        div[data-baseweb="input"]:focus-within,
        div[data-baseweb="select"] > div:focus-within,
        .stTextInput > div > div:focus-within,
        .stSelectbox > div > div:focus-within,
        .stTextArea textarea:focus {
            border-color: #38BDF8 !important;
            box-shadow: 0 0 12px rgba(56, 189, 248, 0.3) !important;
        }

        /* Section anchor scroll offsets for clean positioning beneath floating navbar */
        #why-retain, #why-us, #contact {
            scroll-margin-top: 90px !important;
        }

        html, body, section.stMain, [data-testid="stMain"], [data-testid="stAppViewContainer"] {
            scroll-behavior: smooth !important;
        }

        /* Invisible layout container for client-side script helpers */
        iframe[height="0"] {
            position: absolute !important;
            width: 0 !important;
            height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            border: none !important;
            opacity: 0 !important;
            pointer-events: none !important;
        }
        /* ==========================================================================
           Section 5: Enterprise Piloting & Contact Centered Container
           Ensures the section never hugs the screen bezel and stays perfectly aligned
           with the 1200px navbar and bento cards.
           ========================================================================== */
        /* Seamless full-bleed canvas sections: no dead gaps or empty bands */
        div[data-testid="stIFrame"]:has(iframe),
        div[data-testid="stElementContainer"]:has(iframe) {
            margin-top: 0 !important;
            margin-bottom: 0 !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }

        /* Collapse interstitial anchors cleanly without hiding from document layout / scroll math */
        div.element-container:has(#why-retain),
        div[data-testid="stElementContainer"]:has(#why-retain),
        div.element-container:has(#why-us),
        div[data-testid="stElementContainer"]:has(#why-us),
        div.element-container:has(#contact),
        div[data-testid="stElementContainer"]:has(#contact),
        div.element-container:has(#contact-section-anchor),
        div[data-testid="stElementContainer"]:has(#contact-section-anchor) {
            display: block !important;
            height: 0 !important;
            min-height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            border: none !important;
            overflow: visible !important;
        }

        #why-retain, #why-us, #contact {
            display: block !important;
            height: 0 !important;
            scroll-margin-top: 90px !important;
        }

        /* Seamless connection: pull Section 2 and Section 4 flush against preceding sections */
        div[data-testid="stElementContainer"][height="690px"],
        div.element-container[height="690px"],
        div[data-testid="stElementContainer"]:has(iframe[height="690"]),
        div.element-container:has(iframe[height="690"]),
        div[data-testid="stElementContainer"][height="780px"],
        div.element-container[height="780px"],
        div[data-testid="stElementContainer"]:has(iframe[height="780"]),
        div.element-container:has(iframe[height="780"]) {
            margin-top: -16px !important;
            margin-bottom: 0 !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }

        /* Hide divider line to connect Section 4 seamlessly to Section 5 */
        .contact-section-divider {
            display: none !important;
            height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* Constrain Section 5, touch Section 4 bottom directly, and provide generous breathing room between left and right columns */
        div[data-testid="stHorizontalBlock"]:has(.pilot-left-col),
        div[data-testid="stHorizontalBlock"]:has(#contact-section-anchor) {
            max-width: 1320px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            margin-top: -16px !important;
            padding-left: clamp(1.5rem, 3.5vw, 3rem) !important;
            padding-right: clamp(1.5rem, 3.5vw, 3rem) !important;
            padding-top: 3.5rem !important;
            padding-bottom: 5.5rem !important;
            box-sizing: border-box !important;
            width: 100% !important;
            gap: clamp(3.5rem, 6vw, 6rem) !important;
            align-items: flex-start !important;
        }

        @media (max-width: 768px) {
            div[data-testid="stHorizontalBlock"]:has(.pilot-left-col) {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                gap: 1.5rem !important;
            }
        }

        .pilot-left-col {
            width: 100%;
            box-sizing: border-box;
            padding-left: clamp(0.25rem, 1vw, 0.75rem);
            padding-right: clamp(0.25rem, 1vw, 0.75rem);
        }

        .pilot-right-col {
            width: 100%;
            box-sizing: border-box;
            padding-left: clamp(0.25rem, 1vw, 0.75rem);
            padding-right: clamp(0.25rem, 1vw, 0.75rem);
        }

        .pipeline-container {
            display: flex;
            flex-direction: column;
            margin-bottom: 1.4rem;
        }

        .pipeline-step {
            position: relative;
            padding-left: 28px;
            padding-bottom: 32px;
            background: transparent;
            border: none;
            border-radius: 0;
            box-shadow: none;
        }

        .pipeline-step:last-child {
            padding-bottom: 0;
        }

        .pipeline-line {
            position: absolute;
            left: 14px;
            width: 1px;
            background-color: rgba(56, 189, 248, 0.20);
        }

        .pipeline-step-1 .pipeline-line {
            top: 37px;
            bottom: -1px;
        }

        .pipeline-step-2 .pipeline-line,
        .pipeline-step-3 .pipeline-line {
            top: 0;
            bottom: -1px;
        }

        .pipeline-step-4 .pipeline-line {
            top: 0;
            height: 37px;
        }

        .pipeline-node {
            position: absolute;
            left: 9.5px;
            top: 32px;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: #38BDF8;
            z-index: 2;
        }

        .pipeline-node-end {
            background-color: #34D399;
        }

        .pipeline-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 20px;
            margin-bottom: 6px;
            gap: 0.5rem;
        }

        .pipeline-label {
            font-size: 0.74rem;
            font-weight: 600;
            color: #94A3B8;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            font-family: inherit;
        }

        .pipeline-meta {
            font-size: 0.74rem;
            color: #94A3B8;
            font-family: inherit;
            text-align: right;
            white-space: nowrap;
        }

        .pipeline-title {
            font-family: var(--font-display) !important;
            font-size: 1.02rem;
            font-weight: 700;
            letter-spacing: -0.01em;
            color: #F8FAFC;
            margin-bottom: 0.35rem;
            line-height: 1.35;
        }

        .pipeline-desc {
            color: #94A3B8;
            font-size: 0.87rem;
            line-height: 1.52;
            margin: 0;
        }

        .pilot-gateway-card {
            background: rgba(11, 17, 32, 0.82);
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
            border: 1px solid rgba(56, 189, 248, 0.35);
            border-radius: 14px;
            padding: 1.25rem 1.4rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.45), inset 0 0 15px rgba(56, 189, 248, 0.05);
            transition: all 0.25s ease;
        }

        .pilot-gateway-card:hover {
            border-color: rgba(56, 189, 248, 0.6);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.65), 0 0 20px rgba(56, 189, 248, 0.25);
            transform: translateY(-1px);
        }

        /* Style the Streamlit Form to match the NEONE glass card aesthetics */
        div[data-testid="stHorizontalBlock"]:has(.pilot-left-col) div[data-testid="stForm"],
        div[data-testid="stHorizontalBlock"]:has(.pilot-right-col) div[data-testid="stForm"] {
            background: rgba(11, 15, 25, 0.75) !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            border: 1px solid rgba(56, 189, 248, 0.25) !important;
            border-radius: 16px !important;
            padding: 1.75rem 2rem !important;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.65), 0 0 1px rgba(56, 189, 248, 0.25) !important;
            transition: all 0.25s ease !important;
        }

        div[data-testid="stHorizontalBlock"]:has(.pilot-left-col) div[data-testid="stForm"]:hover,
        div[data-testid="stHorizontalBlock"]:has(.pilot-right-col) div[data-testid="stForm"]:hover {
            border-color: rgba(56, 189, 248, 0.45) !important;
            box-shadow: 0 12px 48px rgba(0, 0, 0, 0.75), 0 0 20px rgba(56, 189, 248, 0.2) !important;
        }

        /* 1. Form inputs, textarea and dropdown focus styling */
        [data-testid="stForm"] div[data-baseweb="input"],
        [data-testid="stForm"] div[data-baseweb="base-input"],
        [data-testid="stForm"] div[data-baseweb="textarea"],
        [data-testid="stForm"] div[data-baseweb="select"] > div {
            transition: border-color 150ms ease, box-shadow 150ms ease !important;
        }

        [data-testid="stForm"] div[data-baseweb="input"]:focus-within,
        [data-testid="stForm"] div[data-baseweb="base-input"]:focus-within,
        [data-testid="stForm"] div[data-baseweb="textarea"]:focus-within,
        [data-testid="stForm"] div[data-baseweb="select"]:focus-within > div,
        [data-testid="stForm"] div[data-baseweb="select"] > div:focus-within {
            border-color: #38BDF8 !important;
            box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.18) !important;
            outline: none !important;
        }

        [data-testid="stForm"] input:focus,
        [data-testid="stForm"] textarea:focus,
        [data-testid="stForm"] select:focus {
            outline: none !important;
            box-shadow: none !important;
        }

        /* 3. Step hover: title and description get slightly brighter */
        .pipeline-step {
            cursor: default;
        }

        .pipeline-step .pipeline-title,
        .pipeline-step .pipeline-desc {
            transition: color 150ms ease !important;
        }

        .pipeline-step:hover .pipeline-title {
            color: #FFFFFF !important;
        }

        .pipeline-step:hover .pipeline-desc {
            color: #CBD5E1 !important;
        }

        /* 2 & 4. Pipeline scroll-driven entrance animation (wrapped in prefers-reduced-motion) */
        @media (prefers-reduced-motion: no-preference) {
            @supports (animation-timeline: view()) {
                .pipeline-container {
                    view-timeline-name: --pipeline-timeline;
                    view-timeline-axis: block;
                }

                .pipeline-line {
                    transform-origin: top center;
                    animation-timeline: --pipeline-timeline;
                    animation-range: entry 0% entry 70%;
                    animation-fill-mode: both;
                }

                .pipeline-step-1 .pipeline-line {
                    animation-name: pipelineLineDraw1;
                }

                .pipeline-step-2 .pipeline-line {
                    animation-name: pipelineLineDraw2;
                }

                .pipeline-step-3 .pipeline-line {
                    animation-name: pipelineLineDraw3;
                }

                .pipeline-step-4 .pipeline-line {
                    animation-name: pipelineLineDraw4;
                }

                .pipeline-node {
                    animation-timeline: --pipeline-timeline;
                    animation-range: entry 0% entry 70%;
                    animation-fill-mode: both;
                }

                .pipeline-step-1 .pipeline-node {
                    animation-name: pipelineNodeLight1;
                }

                .pipeline-step-2 .pipeline-node {
                    animation-name: pipelineNodeLight2;
                }

                .pipeline-step-3 .pipeline-node {
                    animation-name: pipelineNodeLight3;
                }

                .pipeline-step-4 .pipeline-node {
                    animation-name: pipelineNodeLight4;
                }

                @keyframes pipelineLineDraw1 {
                    0% {
                        transform: scaleY(0);
                    }
                    25%, 100% {
                        transform: scaleY(1);
                    }
                }

                @keyframes pipelineLineDraw2 {
                    0%, 25% {
                        transform: scaleY(0);
                    }
                    50%, 100% {
                        transform: scaleY(1);
                    }
                }

                @keyframes pipelineLineDraw3 {
                    0%, 50% {
                        transform: scaleY(0);
                    }
                    75%, 100% {
                        transform: scaleY(1);
                    }
                }

                @keyframes pipelineLineDraw4 {
                    0%, 75% {
                        transform: scaleY(0);
                    }
                    100% {
                        transform: scaleY(1);
                    }
                }

                @keyframes pipelineNodeLight1 {
                    0% {
                        opacity: 0.25;
                        transform: scale(0.75);
                    }
                    10%, 100% {
                        opacity: 1;
                        transform: scale(1);
                    }
                }

                @keyframes pipelineNodeLight2 {
                    0%, 25% {
                        opacity: 0.25;
                        transform: scale(0.75);
                    }
                    35%, 100% {
                        opacity: 1;
                        transform: scale(1);
                    }
                }

                @keyframes pipelineNodeLight3 {
                    0%, 50% {
                        opacity: 0.25;
                        transform: scale(0.75);
                    }
                    60%, 100% {
                        opacity: 1;
                        transform: scale(1);
                    }
                }

                @keyframes pipelineNodeLight4 {
                    0%, 75% {
                        opacity: 0.25;
                        transform: scale(0.75);
                    }
                    85%, 100% {
                        opacity: 1;
                        transform: scale(1);
                    }
                }
            }
        }
        </style>""", unsafe_allow_html=True)
