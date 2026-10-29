import os

# 1. Update utils/styles.py
with open('utils/styles.py', 'r', encoding='utf-8') as f:
    styles = f.read().replace('\r\n', '\n')

old_css_part = """        /* Seamless full-bleed canvas sections: no dead gaps or empty bands */
        div[data-testid="stCustomComponentV1"]:has(iframe) {
            margin-top: 0 !important;
            margin-bottom: 0 !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }
        div.element-container:has(#why-retain) {
            display: none !important;
            height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        .contact-section-divider {
            height: 1px;
            width: 100%;
            max-width: 1200px;
            margin: 1.5rem auto 2.5rem auto;
            background: linear-gradient(90deg, transparent 0%, rgba(56, 189, 248, 0.35) 50%, transparent 100%);
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.25);
        }

        /* Constrain Streamlit Horizontal Block containing the Contact section */
        div[data-testid="stHorizontalBlock"]:has(.pilot-left-col),
        div[data-testid="stHorizontalBlock"]:has(#contact-section-anchor) {
            max-width: 1240px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            padding-left: clamp(1.25rem, 3vw, 2.5rem) !important;
            padding-right: clamp(1.25rem, 3vw, 2.5rem) !important;
            padding-top: 0.5rem !important;
            padding-bottom: 5rem !important;
            box-sizing: border-box !important;
            width: 100% !important;
            gap: 2.5rem !important;
            align-items: flex-start !important;
        }"""

new_css_part = """        /* Seamless full-bleed canvas sections: no dead gaps or empty bands */
        div[data-testid="stCustomComponentV1"]:has(iframe) {
            margin-top: 0 !important;
            margin-bottom: 0 !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }

        /* Collapse interstitial anchors to zero height and zero margin */
        div.element-container:has(#why-retain),
        div[data-testid="stElementContainer"]:has(#why-retain),
        div.element-container:has(#why-us),
        div[data-testid="stElementContainer"]:has(#why-us),
        div.element-container:has(#contact),
        div[data-testid="stElementContainer"]:has(#contact),
        div.element-container:has(#contact-section-anchor),
        div[data-testid="stElementContainer"]:has(#contact-section-anchor) {
            display: none !important;
            height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }

        /* Section 4 touches Section 3 with 0px gap */
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

        /* Constrain Section 5 and touch Section 4 bottom directly with 0px gap */
        div[data-testid="stHorizontalBlock"]:has(.pilot-left-col),
        div[data-testid="stHorizontalBlock"]:has(#contact-section-anchor) {
            max-width: 1240px !important;
            margin-left: auto !important;
            margin-right: auto !important;
            margin-top: -16px !important;
            padding-left: clamp(1.25rem, 3vw, 2.5rem) !important;
            padding-right: clamp(1.25rem, 3vw, 2.5rem) !important;
            padding-top: 2.5rem !important;
            padding-bottom: 5rem !important;
            box-sizing: border-box !important;
            width: 100% !important;
            gap: 2.5rem !important;
            align-items: flex-start !important;
        }"""

assert old_css_part in styles, "old_css_part not found in styles.py"
styles = styles.replace(old_css_part, new_css_part)
with open('utils/styles.py', 'w', encoding='utf-8') as f:
    f.write(styles)
print("Updated utils/styles.py successfully")

# 2. Update Dashboard.py & app.py
with open('Dashboard.py', 'r', encoding='utf-8') as f:
    dash = f.read().replace('\r\n', '\n')

old_dash_masks = """      return React.createElement('div', {
        className: 'relative w-full h-[780px] overflow-hidden bg-[#030712]'
      },
        // Top & Bottom Seamless Continuous Gradient Masks
        React.createElement('div', {
          className: 'absolute top-0 left-0 right-0 h-32 bg-gradient-to-b from-[#030712] via-[#030712]/50 to-transparent pointer-events-none z-10'
        }),
        React.createElement('div', {
          className: 'absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-t from-[#030712] via-[#030712]/50 to-transparent pointer-events-none z-10'
        }),

        // ====================================================================
        // BACKGROUND LAYER 1: 100% FULL-SCREEN 3D EXCEL SPREADSHEET LOOP
        // ====================================================================
        React.createElement('div', {"""

new_dash_masks = """      return React.createElement('div', {
        className: 'relative w-full h-[780px] overflow-hidden bg-[#030712]'
      },
        // ====================================================================
        // BACKGROUND LAYER 1: 100% FULL-SCREEN 3D EXCEL SPREADSHEET LOOP
        // ====================================================================
        React.createElement('div', {"""

old_contact_divider = """components.html(scroll_transition_html, height=780, scrolling=False)

# ==============================================================================
# SECTION 5: CONTACT & STAKEHOLDER DEMO INQUIRY
# ==============================================================================
st.markdown('<div class="contact-section-divider"></div><div id="contact"><span id="contact-section-anchor"></span></div>', unsafe_allow_html=True)"""

new_contact_divider = """components.html(scroll_transition_html, height=780, scrolling=False)

# ==============================================================================
# SECTION 5: CONTACT & STAKEHOLDER DEMO INQUIRY
# ==============================================================================
st.markdown('<div id="contact"><span id="contact-section-anchor"></span></div>', unsafe_allow_html=True)"""

assert old_dash_masks in dash, "old_dash_masks not found in Dashboard.py"
assert old_contact_divider in dash, "old_contact_divider not found in Dashboard.py"

dash = dash.replace(old_dash_masks, new_dash_masks).replace(old_contact_divider, new_contact_divider)

with open('Dashboard.py', 'w', encoding='utf-8') as f:
    f.write(dash)
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(dash)

print("Updated Dashboard.py and app.py successfully")
