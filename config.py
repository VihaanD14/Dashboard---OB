import streamlit as st

# App Constants
APP_TITLE = "RetainlyAI | Predictive Talent Intelligence"
APP_ICON = "✦"

# Color Palette (NEONE Aesthetic: Deep Cosmic Obsidian & Electric Cyan)
COLORS = {
    # Core Brand & Surfaces (NEONE Aesthetic)
    "primary": "#38BDF8",        # Electric Cyan
    "secondary": "#60A5FA",      # Soft Electric Azure
    "background": "#030712",     # Deep Obsidian Void
    "card_bg": "#0B0F19",        # Translucent Dark Slate Surface
    "text": "#F8FAFC",           # Pure Ice White
    "text_muted": "#94A3B8",     # Cool Slate Muted
    "border": "rgba(56, 189, 248, 0.18)", # Subtle Cyan Rim Light
    "glow": "rgba(56, 189, 248, 0.25)",
    
    # RAG Risk Metrics (High-contrast, functional signal colors)
    "risk_high": "#F43F5E",      # Neon Rose / Critical Risk
    "risk_medium": "#FBBF24",    # Bright Amber / Watchlist
    "risk_low": "#10B981",       # Neon Mint / Stable Retention
    
    # Harmonized Multi-Series Plotly Palette
    "chart_palette": ["#38BDF8", "#818CF8", "#C084FC", "#34D399", "#FBBF24"],
    
    # Backward-compatibility aliases for existing project references
    "card": "#0B0F19",
    "muted": "#94A3B8",
    "danger": "#F43F5E",
    "warning": "#FBBF24",
    "success": "#10B981"
}

# Categories
DEPARTMENTS = ["Engineering", "Sales", "Marketing", "Operations", "HR", "Finance"]
ROLE_LEVELS = ["Junior", "Mid", "Senior", "Lead", "Manager"]

# Risk Levels (Functional RAG System)
RISK_LEVELS = {
    "High": {"color": COLORS["risk_high"], "description": "Critical intervention required"},
    "Medium": {"color": COLORS["risk_medium"], "description": "Monitor and engage"},
    "Low": {"color": COLORS["risk_low"], "description": "Stable retention"}
}
