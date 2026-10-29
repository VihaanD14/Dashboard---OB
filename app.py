import streamlit as st
import streamlit.components.v1 as components
from config import APP_TITLE, APP_ICON, COLORS
from utils.styles import apply_custom_css
from utils.navigation import render_top_navbar
from utils.splash import show_splash_screen

# Page configuration
st.set_page_config(
    page_title=f"RetAIn | Predictive Talent Intelligence",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
apply_custom_css()
st.markdown('<div id="homepage-root"></div>', unsafe_allow_html=True)

# Show splash screen once per session
show_splash_screen()

# Handle query param routing
if st.query_params.get("page") in ["dashboard", "signin"]:
    st.query_params.clear()
    st.switch_page("pages/1_Enterprise_Dashboard.py")

# Render Naked Top Navbar (Public SaaS mode)
render_top_navbar(active_page="overview")

# ==============================================================================
# SECTION 1: INTERACTIVE FRAMER MOTION HERO (TEDY STYLE WITH WHATSAPP MESSAGE BOXES)
# ==============================================================================
framer_hero_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..700&family=Instrument+Sans:ital,wght@0,400..600;1,400..600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --font-display: 'Bricolage Grotesque', sans-serif;
    --font-body: 'Instrument Sans', sans-serif;
  }
  .brand {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    font-size: inherit;
    font-weight: 700;
    color: #F8FAFC !important;
    letter-spacing: -0.02em;
    display: inline-block;
  }
  .brand-ai {
    color: #38BDF8 !important;
    font-weight: 800 !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
  }
  body {
    background-color: transparent;
    color: #F8FAFC;
    font-family: var(--font-body);
    overflow: hidden;
    height: 750px;
    width: 100%;
    position: relative;
    user-select: none;
  }


  .framer-hero-viewport {
    position: relative;
    width: 100%;
    height: 750px;
    display: flex;
    align-items: center;
    justify-content: center;
    perspective: 1200px;
  }

  /* Center RetAIn Core Pitch */
  .center-stage {
    position: relative;
    z-index: 25;
    max-width: 500px;
    text-align: center;
    padding: 0.2rem 0.4rem;
    pointer-events: auto;
    transition: transform 0.1s ease-out, opacity 0.1s ease-out;
  }

  /* Soft radial cyan-blue light centered behind the headline */
  .center-stage::before {
    content: '';
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 600px;
    height: 380px;
    background: radial-gradient(circle, rgba(34, 211, 238, 0.15) 0%, rgba(59, 130, 246, 0.08) 50%, transparent 70%);
    filter: blur(60px);
    -webkit-filter: blur(60px);
    pointer-events: none;
    z-index: -1;
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid rgba(56, 189, 248, 0.28);
    border-radius: 9999px;
    padding: 0.25rem 0.85rem;
    color: #38BDF8;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 0.65rem;
    box-shadow: 0 0 14px rgba(56, 189, 248, 0.16);
  }

  .hero-title {
    font-family: var(--font-display);
    font-size: 2.3rem;
    font-weight: 700;
    line-height: 1.15;
    letter-spacing: -0.01em;
    color: #F8FAFC;
    margin-bottom: 0.85rem;
  }

  .hero-title span {
    background: linear-gradient(135deg, #22d3ee 0%, #3b82f6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  /* Key RetAIn Info Box (Direct User Pitch - Naked Floating Typography) */
  .hero-key-quote {
    background: transparent;
    border: none;
    border-radius: 0;
    padding: 0;
    margin: 0 auto 1.45rem auto;
    max-width: 480px;
    box-shadow: none;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }

  .hero-key-text {
    font-size: 1.02rem;
    color: #94A3B8;
    line-height: 1.62;
    font-weight: 400;
    letter-spacing: -0.01em;
  }

  .highlight-cyan {
    color: #38BDF8;
    font-weight: 600;
  }

  .highlight-white {
    color: #F8FAFC;
    font-weight: 600;
  }

  .hero-actions {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.8rem;
  }

  .btn-pill-primary {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    background: #22d3ee;
    color: #030712;
    font-weight: 700;
    font-size: 0.86rem;
    letter-spacing: -0.01em;
    padding: 0.62rem 1.45rem;
    border-radius: 9999px;
    border: 1px solid rgba(34, 211, 238, 0.8);
    box-shadow: 0 0 12px rgba(34, 211, 238, 0.50), 0 0 28px rgba(34, 211, 238, 0.50);
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .btn-pill-primary:hover {
    background: #67e8f9;
    color: #030712;
    transform: translateY(-2px);
    box-shadow: 0 0 16px rgba(34, 211, 238, 0.80), 0 0 36px rgba(34, 211, 238, 0.65);
  }

  .btn-pill-secondary {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(11, 15, 25, 0.75);
    color: #F8FAFC;
    font-weight: 500;
    font-size: 0.84rem;
    padding: 0.56rem 1.2rem;
    border-radius: 9999px;
    border: 1px solid rgba(34, 211, 238, 0.40);
    backdrop-filter: blur(12px);
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .btn-pill-secondary:hover {
    border-color: rgba(34, 211, 238, 0.85);
    background: rgba(15, 23, 42, 0.95);
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 0 14px rgba(34, 211, 238, 0.35);
  }

  /* WhatsApp Message Layer */
  .framer-cards-layer {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 10;
  }

  /* Authentic WhatsApp Message Bubble Matching User Reference Image (EXCLUSION: Keeps original font) */
  .wa-card,
  .wa-card * {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  }

  .wa-card {
    position: absolute;
    top: 0;
    left: 0;
    width: 224px;
    background: #FFFFFF;
    color: #111827;
    border-radius: 12px;
    padding: 8px 11px 12px 11px;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.55), 0 2px 6px rgba(0, 0, 0, 0.2), 0 0 20px rgba(56, 189, 248, 0.12);
    pointer-events: auto;
    cursor: pointer;
    transition: box-shadow 0.22s ease;
    will-change: transform;
    border: 1px solid rgba(255, 255, 255, 0.9);
  }

  .wa-card:hover {
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.8), 0 0 22px rgba(56, 189, 248, 0.5) !important;
    z-index: 100 !important;
  }

  /* WhatsApp Message Tails */
  .wa-card.tail-left::before {
    content: '';
    position: absolute;
    top: 0;
    left: -8px;
    width: 0;
    height: 0;
    border-top: 0 solid transparent;
    border-bottom: 9px solid transparent;
    border-right: 9px solid #FFFFFF;
  }

  .wa-card.tail-right::before {
    content: '';
    position: absolute;
    top: 0;
    right: -8px;
    width: 0;
    height: 0;
    border-top: 0 solid transparent;
    border-bottom: 9px solid transparent;
    border-left: 9px solid #FFFFFF;
  }

  /* WhatsApp Green Sent Bubble (Resolution & Playbooks) */
  .wa-card.wa-sent {
    background: #DCF8C6;
    border-color: rgba(220, 248, 198, 0.95);
  }
  .wa-card.wa-sent.tail-right::before {
    border-left-color: #DCF8C6;
  }
  .wa-card.wa-sent.tail-left::before {
    border-right-color: #DCF8C6;
  }

  .wa-sender {
    font-size: 11.8px;
    font-weight: 700;
    margin-bottom: 3px;
    letter-spacing: -0.01em;
  }

  .wa-body {
    font-size: 11.5px;
    line-height: 1.34;
    color: #111827;
    margin-bottom: 3px;
    word-break: break-word;
  }

  .wa-meta {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    gap: 3px;
    font-size: 10px;
    color: #667781;
    margin-top: 1px;
  }

  .wa-ticks {
    color: #53BDEB;
    font-weight: 800;
    font-size: 10px;
    letter-spacing: -2px;
  }

  /* Floating Reactions Pill (Exact WhatsApp Sticker Pill from User Reference) */
  .wa-reactions-pill {
    position: absolute;
    bottom: -9px;
    left: 12px;
    background: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 9999px;
    padding: 1px 6px;
    display: inline-flex;
    align-items: center;
    gap: 3px;
    font-size: 10px;
    font-weight: 600;
    color: #4B5563;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
    transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .wa-card:hover .wa-reactions-pill {
    transform: scale(1.1);
  }

  .wa-card.wa-sent .wa-reactions-pill {
    background: #F0FDF4;
    border-color: #BBF7D0;
  }
</style>
</head>
<body>

<div class="framer-hero-viewport" id="framerHero">
  <!-- Center RetAIn Pitch -->
  <div class="center-stage" id="centerStage">
    <h1 class="hero-title">
      Stop Losing Key Talent <br><span>Before They Leave.</span>
    </h1>

    <div class="hero-key-quote">
      <p class="hero-key-text">
        <span class="brand">Ret<span class="brand-ai">AI</span>n</span> decodes <span class="highlight-cyan">silent exit signals</span> and turns team sentiment into <span class="highlight-white">high-ROI retention playbooks</span> before resignation letters hit your desk.
      </p>
    </div>

    <div class="hero-actions">
      <button onclick="navigateParentToPortal()" class="btn-pill-primary">
        Launch Enterprise Portal &rarr;
      </button>
      <button onclick="scrollToPlatform()" class="btn-pill-secondary">
        Explore Platform &darr;
      </button>
    </div>
  </div>

  <!-- WhatsApp Message Boxes (Dynamic Contracted -> Spread Layer - 8 Balanced Cards) -->
  <div class="framer-cards-layer">
    <!-- Box 1: Alex Rivera (Cloud Architect) - Top Left -->
    <div class="wa-card tail-left" id="card1" data-cx="-310" data-cy="-160" data-sx="-560" data-sy="-180" data-crot="-3" data-srot="-6" data-phase="0">
      <div class="wa-sender" style="color: #7C3AED;">Alex Rivera</div>
      <div class="wa-body">
        Hey team, putting in my two weeks today. Just felt like there wasn't a clear path beyond Senior and compensation fell behind market. 💔
      </div>
      <div class="wa-meta">
        14:28 <span class="wa-ticks">✓✓</span>
      </div>
      <div class="wa-reactions-pill">
        💔 😢 14
      </div>
    </div>

    <!-- Box 2: Marcus Vance (Backend Lead) - Top Right -->
    <div class="wa-card tail-right" id="card2" data-cx="310" data-cy="-160" data-sx="560" data-sy="-180" data-crot="3" data-srot="6" data-phase="1.2">
      <div class="wa-sender" style="color: #EA580C;">Marcus Vance</div>
      <div class="wa-body">
        Recruiter reached out with +30% remote offer. Love working here, but inflation made staying unviable without a comp review... 🥺
      </div>
      <div class="wa-meta">
        09:12 <span class="wa-ticks">✓✓</span>
      </div>
      <div class="wa-reactions-pill">
        🥺 💸 11
      </div>
    </div>

    <!-- Box 3: Elena Rostova (Staff SRE / DevOps) - Mid-High Left -->
    <div class="wa-card tail-left" id="card3" data-cx="-345" data-cy="-35" data-sx="-600" data-sy="-45" data-crot="-4" data-srot="-8" data-phase="2.1">
      <div class="wa-sender" style="color: #E11D48;">Elena Rostova</div>
      <div class="wa-body">
        Third weekend on-call outage in a row. Team burnout is spiking when platform debt & incident follow-ups keep getting deprioritized... 🔋⚠️
      </div>
      <div class="wa-meta">
        13:45 <span class="wa-ticks">✓✓</span>
      </div>
      <div class="wa-reactions-pill">
        🔋 😴 12
      </div>
    </div>

    <!-- Box 4: Jordan Lee (Lead PM) - Mid-High Right -->
    <div class="wa-card tail-right" id="card4" data-cx="345" data-cy="-35" data-sx="600" data-sy="-45" data-crot="4" data-srot="8" data-phase="3.3">
      <div class="wa-sender" style="color: #D97706;">Jordan Lee</div>
      <div class="wa-body">
        Series B offer came with doubled equity grant. Really want to stay if leadership can align on a Principal track before quarter ends 📊
      </div>
      <div class="wa-meta">
        10:30 <span class="wa-ticks">✓✓</span>
      </div>
      <div class="wa-reactions-pill">
        💼 🤝 15
      </div>
    </div>

    <!-- Box 5: David Kim (Product Design) - Mid-Low Left -->
    <div class="wa-card tail-left" id="card5" data-cx="-340" data-cy="85" data-sx="-580" data-sy="85" data-crot="-2" data-srot="-5" data-phase="4.2">
      <div class="wa-sender" style="color: #2563EB;">David Kim</div>
      <div class="wa-body">
        Honestly feeling isolated working async without real mentorship. Skipped the last two quarterly HR surveys because feedback always disappears.
      </div>
      <div class="wa-meta">
        16:42 <span class="wa-ticks">✓✓</span>
      </div>
      <div class="wa-reactions-pill">
        😔 🫂 6
      </div>
    </div>

    <!-- Box 6: Maya Chen (Senior AE) - Mid-Low Right -->
    <div class="wa-card tail-right" id="card6" data-cx="340" data-cy="85" data-sx="580" data-sy="85" data-crot="2" data-srot="5" data-phase="5.0">
      <div class="wa-sender" style="color: #059669;">Maya Chen</div>
      <div class="wa-body">
        Changing commission accelerators mid-quarter really hurt team trust. Several senior AEs are already actively interviewing elsewhere...
      </div>
      <div class="wa-meta">
        11:05 <span class="wa-ticks">✓✓</span>
      </div>
      <div class="wa-reactions-pill">
        👀 🤐 8
      </div>
    </div>

    <!-- Box 7: Priya Patel (Engineering Director) - Lower Left -->
    <div class="wa-card tail-left" id="card7" data-cx="-290" data-cy="200" data-sx="-520" data-sy="215" data-crot="4" data-srot="7" data-phase="5.8">
      <div class="wa-sender" style="color: #9333EA;">Priya Patel</div>
      <div class="wa-body">
        RetAIn flagged flight risk in our mid-level backend cohort 3 weeks ago. We leveled bands and retained everyone before notices hit! 👏
      </div>
      <div class="wa-meta">
        18:04 <span class="wa-ticks">✓✓</span>
      </div>
      <div class="wa-reactions-pill">
        👏 💡 19
      </div>
    </div>

    <!-- Box 8: People Ops (Retention Resolution Action - Green Sent Bubble) - Lower Right -->
    <div class="wa-card wa-sent tail-right" id="card8" data-cx="290" data-cy="200" data-sx="520" data-sy="215" data-crot="-4" data-srot="-7" data-phase="6.5">
      <div class="wa-sender" style="color: #075E54;">People Ops &bull; Action</div>
      <div class="wa-body">
        Playbook #14 confirmed: Off-cycle comp adjustment to 85th percentile + Tech Lead track approved. Resignation prevented! 🎉
      </div>
      <div class="wa-meta">
        17:15 <span class="wa-ticks">✓✓</span>
      </div>
      <div class="wa-reactions-pill">
        🎉 🚀 24
      </div>
    </div>
  </div>
</div>

<script>
  const cards = [
    document.getElementById('card1'),
    document.getElementById('card2'),
    document.getElementById('card3'),
    document.getElementById('card4'),
    document.getElementById('card5'),
    document.getElementById('card6'),
    document.getElementById('card7'),
    document.getElementById('card8')
  ];
  const centerStage = document.getElementById('centerStage');

  // Framer Motion Spring States
  let introProgress = 0.0;
  let targetIntroProgress = 1.0;
  let scrollProgress = 0.0;
  let targetScrollProgress = 0.0;
  let mouseX = 0;
  let mouseY = 0;
  let targetMouseX = 0;
  let targetMouseY = 0;

  // Clickable reactions micro-interaction
  document.querySelectorAll('.wa-reactions-pill').forEach(pill => {
    pill.addEventListener('click', (e) => {
      e.stopPropagation();
      const parts = pill.innerText.trim().split(' ');
      const num = parseInt(parts[parts.length - 1]);
      if (!isNaN(num)) {
        parts[parts.length - 1] = (num + 1).toString();
        pill.innerText = parts.join(' ');
        pill.style.transform = 'scale(1.25)';
        setTimeout(() => { pill.style.transform = 'scale(1)'; }, 180);
      }
    });
  });

  // Track Mouse for subtle 3D Parallax
  window.addEventListener('mousemove', (e) => {
    const halfW = window.innerWidth / 2;
    const halfH = 370;
    targetMouseX = (e.clientX - halfW) / halfW;
    targetMouseY = (e.clientY - halfH) / halfH;
  }, { passive: true });

  // Helper to find the actual scrolling element in Streamlit (handles <main data-testid="stMain"> and older <section>)
  function getParentScroller() {
    try {
      if (window.parent && window.parent.document) {
        return window.parent.document.querySelector('[data-testid="stMain"], main#stMain, .stMain, section[data-testid="stMain"]') ||
               window.parent.document.scrollingElement ||
               window.parent.document.documentElement;
      }
    } catch(e) {}
    return null;
  }

  let virtualScroll = 0;
  let scrollTicking = false;

  function checkParentScroll() {
    if (!scrollTicking) {
      window.requestAnimationFrame(() => {
        let top = 0;
        try {
          const scroller = getParentScroller();
          if (scroller) {
            top = scroller.scrollTop || 0;
          }
          if (!top && window.parent) {
            top = window.parent.scrollY || 0;
          }
          
          const frame = window.frameElement;
          if (frame && window.parent) {
            const rect = frame.getBoundingClientRect();
            const winH = window.parent.innerHeight || 800;
            const inView = (rect.bottom > -50 && rect.top < winH + 50);
            if (inView !== isHeroVisible) {
              isHeroVisible = inView;
              if (isHeroVisible && !heroRaf) {
                startTime = performance.now();
                heroRaf = requestAnimationFrame(renderFrame);
              }
            }
          }
        } catch(err) {}

        const effectiveScroll = Math.max(top, virtualScroll);
        targetScrollProgress = Math.min(1.15, Math.max(0.0, effectiveScroll / 300));
        scrollTicking = false;
      });
      scrollTicking = true;
    }
  }

  try {
    const scroller = getParentScroller();
    if (scroller) {
      scroller.addEventListener('scroll', checkParentScroll, { passive: true });
    }
    if (window.parent) {
      window.parent.addEventListener('scroll', checkParentScroll, { passive: true });
    }
  } catch(err) {}

  // Direct mouse wheel & trackpad listener over hero viewport
  window.addEventListener('wheel', (e) => {
    virtualScroll += e.deltaY * 0.8;
    virtualScroll = Math.max(0, Math.min(400, virtualScroll));
    checkParentScroll();
  }, { passive: true });

  // Touch swipe support for mobile
  let touchStartY = 0;
  window.addEventListener('touchstart', (e) => {
    if (e.touches && e.touches.length > 0) touchStartY = e.touches[0].clientY;
  }, { passive: true });

  window.addEventListener('touchmove', (e) => {
    if (e.touches && e.touches.length > 0) {
      const currentY = e.touches[0].clientY;
      const diffY = touchStartY - currentY;
      touchStartY = currentY;
      virtualScroll += diffY * 1.2;
      virtualScroll = Math.max(0, Math.min(400, virtualScroll));
      checkParentScroll();
    }
  }, { passive: true });

  // Responsive scale calculation that preserves outer perimeter
  function getScale() {
    const w = window.innerWidth;
    if (w < 820) return 0.58;
    if (w < 1050) return 0.70;
    if (w < 1280) return 0.80;
    if (w < 1450) return 0.88;
    return 0.98;
  }

  let startTime = performance.now();
  let isHeroVisible = true;
  let heroRaf = null;

  try {
    const heroObserver = new IntersectionObserver((entries) => {
      isHeroVisible = entries[0].isIntersecting;
      if (isHeroVisible && !heroRaf) {
        startTime = performance.now();
        heroRaf = requestAnimationFrame(renderFrame);
      }
    }, { threshold: 0.02 });
    heroObserver.observe(document.body);
  } catch(e) {}

  function renderFrame(now) {
    if (!isHeroVisible) {
      heroRaf = null;
      return;
    }

    const dt = now - startTime;

    // Framer Spring Lerp physics
    introProgress += (targetIntroProgress - introProgress) * 0.08;
    scrollProgress += (targetScrollProgress - scrollProgress) * 0.09;
    mouseX += (targetMouseX - mouseX) * 0.05;
    mouseY += (targetMouseY - mouseY) * 0.05;

    const s = getScale();
    const centerX = window.innerWidth / 2;
    const centerY = 350; // Vertical midpoint calibrated for 750px height

    // Center Stage scaling and subtle parallax
    const centerScale = 1.0 + 0.03 * scrollProgress;
    centerStage.style.transform = `scale(${centerScale}) translate3d(${mouseX * -6}px, ${mouseY * -5}px, 0)`;

    // Update each WhatsApp Message Bubble
    cards.forEach((card) => {
      const cx = parseFloat(card.getAttribute('data-cx'));
      const cy = parseFloat(card.getAttribute('data-cy'));
      const sx = parseFloat(card.getAttribute('data-sx'));
      const sy = parseFloat(card.getAttribute('data-sy'));
      const crot = parseFloat(card.getAttribute('data-crot'));
      const srot = parseFloat(card.getAttribute('data-srot'));
      const phase = parseFloat(card.getAttribute('data-phase'));

      // Continuous organic levitation wave (Framer float feel)
      const floatY = Math.sin(dt * 0.0022 + phase) * 4;
      const floatX = Math.cos(dt * 0.0017 + phase) * 2;
      const floatRot = Math.sin(dt * 0.0019 + phase) * 1.2;

      // Dynamic interpolation from contracted state (0) to spread state (1)
      const interpX = cx + (sx - cx) * scrollProgress;
      const interpY = cy + (sy - cy) * scrollProgress;
      const interpRot = crot + (srot - crot) * scrollProgress;

      const spreadX = (interpX * s) + floatX + (mouseX * 12);
      const spreadY = (interpY * s) + floatY + (mouseY * 8);
      const spreadRot = interpRot + floatRot;

      const posX = centerX + spreadX - 112; // 112 is half of 224px card width
      const posY = centerY + spreadY - 50;

      // Safe bounds padding to ensure bubbles NEVER cut off at window edges
      const cardW = 224 * s;
      const minX = 16;
      const maxX = Math.max(minX, window.innerWidth - cardW - 16);
      const safeX = Math.max(minX, Math.min(maxX, posX));

      // Smooth hover scale and elevation integrated directly into translation
      const isHovered = card.matches(':hover');
      const hoverScale = isHovered ? 1.07 : 1.0;
      const hoverLift = isHovered ? -6 : 0;

      card.style.transform = `translate3d(${safeX}px, ${posY + hoverLift}px, 0) scale(${s * hoverScale}) rotate(${spreadRot}deg)`;
      card.style.opacity = Math.min(1.0, 0.45 + introProgress * 0.55);
    });

    heroRaf = requestAnimationFrame(renderFrame);
  }

  function navigateParentToPortal() {
    try {
      if (window.parent && window.parent.document) {
        const topLink = window.parent.document.querySelector('.naked-nav-links a[href="/Enterprise_Dashboard"]') ||
                        window.parent.document.querySelector('a.naked-signin-pill') ||
                        window.parent.document.querySelector('a[href="/Enterprise_Dashboard"]');
        if (topLink) {
          topLink.click();
          return;
        }
        const a = window.parent.document.createElement('a');
        a.href = '/Enterprise_Dashboard';
        a.target = '_self';
        window.parent.document.body.appendChild(a);
        a.click();
        a.remove();
        return;
      }
    } catch(e) {}
    window.location.href = '/Enterprise_Dashboard';
  }

  function scrollToPlatform() {
    virtualScroll = 340;
    targetScrollProgress = 1.0;
    try {
      const scroller = getParentScroller();
      const plat = window.parent.document.getElementById('platform');
      if (plat && scroller) {
        const topPos = plat.getBoundingClientRect().top + scroller.scrollTop - 70;
        scroller.scrollTo({ top: topPos, behavior: 'smooth' });
        return;
      }
    } catch(err) {}
  }

  heroRaf = requestAnimationFrame(renderFrame);
</script>

</body>
</html>
"""

components.html(framer_hero_html, height=750, scrolling=False)


# ==============================================================================
# SECTION 2: THE AUTONOMOUS RETENTION LOOP (DATA GALAXY LOOP BACKGROUND)
# ==============================================================================
st.markdown('<div id="platform"></div>', unsafe_allow_html=True)

retention_loop_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..700&family=Instrument+Sans:ital,wght@0,400..600;1,400..600&display=swap" rel="stylesheet">
<style>
  :root {
    --font-display: 'Bricolage Grotesque', sans-serif;
    --font-body: 'Instrument Sans', sans-serif;
  }
  .brand {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    font-size: inherit;
    font-weight: 700;
    color: #F8FAFC !important;
    letter-spacing: -0.02em;
    display: inline-block;
  }
  .brand-ai {
    color: #38BDF8 !important;
    font-weight: 800 !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
  }
  html, body {
    height: 100%;
    width: 100%;
    overflow: hidden;
    background-color: transparent;
    color: #F8FAFC;
    font-family: var(--font-body);
  }

  .galaxy-section {
    position: relative;
    width: 100%;
    height: 100%;
    min-height: 690px;
    display: flex;
    align-items: center;
    justify-content: center;
    background:
      radial-gradient(ellipse 70% 60% at 50% 50%, rgba(14, 165, 233, 0.14) 0%, rgba(3, 7, 18, 0) 70%),
      radial-gradient(ellipse 120% 90% at 50% 120%, rgba(15, 23, 42, 0.5) 0%, rgba(3, 7, 18, 0) 65%),
      #030712;
    overflow: hidden;
  }

  /* Canvas 3D Data Galaxy Background - Expanded & Vibrant */
  canvas#galaxy {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    display: block;
    z-index: 1;
    opacity: 0.82;
  }

  .galaxy-vignette {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 2;
    background:
      radial-gradient(ellipse 90% 80% at 50% 50%, rgba(3, 7, 18, 0.18) 15%, rgba(3, 7, 18, 0.88) 100%);
  }

  .section-divider-top {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, rgba(56, 189, 248, 0.42) 50%, transparent 100%);
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.38);
    z-index: 5;
  }

  .section-divider-bottom {
    display: none;
  }

  /* Foreground Content Container */
  .content-container {
    position: relative;
    z-index: 10;
    width: 100%;
    max-width: 1560px;
    margin: 0 auto;
    padding: 3.2rem 1.5rem 3.4rem 1.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .section-header {
    text-align: center;
    margin-bottom: 2.2rem;
  }

  .kicker-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.32);
    border-radius: 9999px;
    padding: 0.25rem 0.9rem;
    color: #38BDF8;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.2);
    margin-bottom: 0.6rem;
  }

  .section-title {
    font-family: var(--font-display);
    font-size: 2.3rem;
    font-weight: 700;
    letter-spacing: -0.01em;
    color: #F8FAFC;
    margin: 0 0 0.5rem 0;
    line-height: 1.18;
  }

  .section-subtitle {
    font-size: 1rem;
    color: #94A3B8;
    max-width: 640px;
    margin: 0 auto;
    line-height: 1.58;
    font-weight: 400;
  }

  /* 4-Column Architectural Grid */
  .loop-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.35rem;
    width: 100%;
  }

  @media (max-width: 1100px) {
    .loop-grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 640px) {
    .loop-grid {
      grid-template-columns: 1fr;
    }
  }

  /* Ultra-Sheer Ghost Glass Cards (Galaxy pulses flow visibly through) */
  .loop-card {
    background: rgba(8, 14, 26, 0.38);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(56, 189, 248, 0.28);
    border-radius: 14px;
    padding: 1.55rem 1.4rem 1.7rem 1.4rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1);
    transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease, background 0.22s ease;
    display: flex;
    flex-direction: column;
  }

  .loop-card:hover {
    transform: translateY(-4px);
    background: rgba(12, 22, 40, 0.55);
    border-color: rgba(56, 189, 248, 0.6);
    box-shadow: 0 16px 44px rgba(0, 0, 0, 0.65), 0 0 28px rgba(56, 189, 248, 0.35);
  }

  .loop-card-active {
    background: rgba(10, 20, 38, 0.48);
    border-color: rgba(56, 189, 248, 0.45);
  }

  .loop-step-num {
    font-size: 0.72rem;
    font-weight: 700;
    color: #38BDF8;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.55rem;
  }

  .loop-card-title {
    font-family: var(--font-display);
    font-size: 1.24rem;
    font-weight: 700;
    color: #F8FAFC;
    margin-bottom: 0.55rem;
    letter-spacing: -0.01em;
    line-height: 1.25;
  }

  .loop-tag {
    display: inline-block;
    align-self: flex-start;
    font-size: 0.7rem;
    font-weight: 600;
    color: #38BDF8;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 9999px;
    padding: 0.2rem 0.65rem;
    margin-bottom: 0.85rem;
  }

  .loop-card-desc {
    font-size: 0.88rem;
    color: #CBD5E1;
    line-height: 1.6;
    margin: 0;
    font-weight: 400;
    flex-grow: 1;
  }
</style>
</head>
<body>

<div class="galaxy-section">
  <!-- 3D Particle Data Galaxy Canvas -->
  <canvas id="galaxy" aria-label="Rotating 3D neural data network"></canvas>
  <div class="galaxy-vignette"></div>
  <div class="section-divider-top"></div>
  <div class="section-divider-bottom"></div>

  <!-- Foreground Content -->
  <div class="content-container">
    <div class="section-header">
      <h2 class="section-title">
        How <span class="brand">Ret<span class="brand-ai">AI</span>n</span> Protects Your Workforce
      </h2>
      <p class="section-subtitle">
        Closing the loop between why past employees left and how your current team feels right now.
      </p>
    </div>

    <div class="loop-grid">
      <!-- Step 1: Exit Mining -->
      <div class="loop-card">
        <div class="loop-step-num">01 &bull; INGEST &amp; LISTEN</div>
        <div class="loop-card-title">Qualitative Exit Mining</div>
        <div class="loop-tag">NLP Sentiment Ingestion</div>
        <p class="loop-card-desc">
          Extracts unstructured exit interview notes and HR transcripts into actionable root-cause themes. Uncovers hidden culture, compensation drift, and manager friction without reading private emails.
        </p>
      </div>

      <!-- Step 2: Dynamic Micro-Surveys (Survey Feature Highlighted!) -->
      <div class="loop-card loop-card-active">
        <div class="loop-step-num">02 &bull; PROBE &amp; VALIDATE</div>
        <div class="loop-card-title">Dynamic Micro-Surveys</div>
        <div class="loop-tag">AI-Adaptive Pulse Loops</div>
        <p class="loop-card-desc">
          Dispatches automated 2-question micro-pulse surveys tailored to emerging exit themes. Collects lightweight, high-frequency cohort feedback with zero survey fatigue.
        </p>
      </div>

      <!-- Step 3: Flight Velocity Radar -->
      <div class="loop-card">
        <div class="loop-step-num">03 &bull; PREDICT &amp; QUANTIFY</div>
        <div class="loop-card-title">Flight Velocity Radar</div>
        <div class="loop-tag">Ethical Cohort Scoring</div>
        <p class="loop-card-desc">
          Classifies department vulnerability into Red, Yellow, and Green tiers. Tracks flight velocity and team turnover probability while calculating replacement cost exposure ($).
        </p>
      </div>

      <!-- Step 4: High-ROI Playbooks -->
      <div class="loop-card">
        <div class="loop-step-num">04 &bull; PRESCRIBE &amp; RETAIN</div>
        <div class="loop-card-title">High-ROI Playbooks</div>
        <div class="loop-tag">Autonomous Retention Engine</div>
        <p class="loop-card-desc">
          Generates targeted retention interventions cross-referenced against your internal company policies. Equips leaders with pre-modeled compensation and career trajectory playbooks.
        </p>
      </div>
    </div>
  </div>
</div>

<script>
  // 3D Data Galaxy Loop Canvas Engine - High Performance & Dynamic Viewport Throttle
  (function () {
    var LOOP = 48; // seconds
    var TAU = Math.PI * 2;
    var cv = document.getElementById("galaxy");
    var ctx = cv.getContext("2d");
    var W = 0, H = 0, dpr = 1;

    var seed = 20261013;
    function rnd() { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; }
    function gauss() { return (rnd() + rnd() + rnd() + rnd() - 2) / 2; }

    var N = 240, nodes = [];
    for (var i = 0; i < N; i++) {
      var halo = rnd() < 0.22, x, y, z;
      if (halo) {
        var a = rnd() * TAU, b = Math.acos(2 * rnd() - 1), r = 0.45 + rnd() * 1.35;
        x = r * Math.sin(b) * Math.cos(a); y = r * Math.cos(b) * 0.65; z = r * Math.sin(b) * Math.sin(a);
      } else {
        var arm = Math.floor(rnd() * 3), rr = Math.pow(rnd(), 0.68) * 1.6 + 0.04;
        var th = arm * TAU / 3 + rr * 1.8 + gauss() * 0.45;
        x = rr * Math.cos(th); z = rr * Math.sin(th);
        y = gauss() * 0.28 * (1 - rr * 0.35);
      }
      nodes.push({
        x: x, y: y, z: z,
        kx: 1 + Math.floor(rnd() * 2), ky: 1 + Math.floor(rnd() * 2), kz: 1 + Math.floor(rnd() * 2),
        px: rnd() * TAU, py: rnd() * TAU, pz: rnd() * TAU,
        amp: 0.03 + rnd() * 0.045,
        size: 0.7 + rnd() * 1.3 + (rnd() < 0.08 ? 1.8 : 0),
        hue: rnd() < 0.48 ? 1 : 0,
        twk: 1 + Math.floor(rnd() * 3), tph: rnd() * TAU,
        sx: 0, sy: 0, sd: 0, ss: 0
      });
    }

    var edges = [], seen = {};
    for (var i2 = 0; i2 < N; i2++) {
      var ds = [];
      for (var j = 0; j < N; j++) {
        if (j === i2) continue;
        var dx = nodes[i2].x - nodes[j].x, dy = nodes[i2].y - nodes[j].y, dz = nodes[i2].z - nodes[j].z;
        var d2 = dx * dx + dy * dy + dz * dz;
        if (d2 < 0.12) ds.push([d2, j]);
      }
      ds.sort(function (p, q) { return p[0] - q[0]; });
      for (var m = 0; m < Math.min(3, ds.length); m++) {
        var a2 = Math.min(i2, ds[m][1]), b2 = Math.max(i2, ds[m][1]), key = a2 * 1000 + b2;
        if (seen[key]) continue;
        seen[key] = 1;
        var hasPulse = rnd() < 0.45;
        edges.push({
          a: a2, b: b2, pulse: hasPulse,
          pk: 1 + Math.floor(rnd() * 2),
          po: rnd(), dir: rnd() < 0.5 ? 1 : -1
        });
      }
    }

    var dust = [];
    for (var q = 0; q < 120; q++) {
      var aa = rnd() * TAU, bb = Math.acos(2 * rnd() - 1), rd = 0.5 + rnd() * 2.2;
      dust.push({ x: rd * Math.sin(bb) * Math.cos(aa), y: rd * Math.cos(bb) * 0.8, z: rd * Math.sin(bb) * Math.sin(aa), s: 0.45 + rnd() * 0.9, a: 0.18 + rnd() * 0.4 });
    }

    function sprite(r, g, b) {
      var c = document.createElement("canvas"); c.width = c.height = 64;
      var x = c.getContext("2d"), gr = x.createRadialGradient(32, 32, 0, 32, 32, 32);
      gr.addColorStop(0, "rgba(255,255,255,1)");
      gr.addColorStop(0.12, "rgba(" + r + "," + g + "," + b + ",0.95)");
      gr.addColorStop(0.4, "rgba(" + r + "," + g + "," + b + ",0.24)");
      gr.addColorStop(1, "rgba(" + r + "," + g + "," + b + ",0)");
      x.fillStyle = gr; x.fillRect(0, 0, 64, 64);
      return c;
    }
    var spBlue = sprite(47, 123, 255), spCyan = sprite(63, 230, 255);

    function resize() {
      dpr = Math.min(window.devicePixelRatio || 1, 1.25);
      W = cv.clientWidth; H = cv.clientHeight;
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    }
    window.addEventListener("resize", resize);
    resize();

    var CAM = 3.6;
    function frame(u) {
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, H);
      ctx.globalCompositeOperation = "lighter";

      var f = Math.max(W * 0.55, H * 0.95) * 1.65;
      var cx = W / 2, cy = H / 2;
      var yaw = u * TAU;
      var tilt = 0.5 + 0.08 * Math.sin(u * TAU);
      var cyw = Math.cos(yaw), syw = Math.sin(yaw), ct = Math.cos(tilt), st = Math.sin(tilt);

      function project(x, y, z, out) {
        var x1 = x * cyw + z * syw, z1 = -x * syw + z * cyw;
        var y2 = y * ct - z1 * st, z2 = y * st + z1 * ct;
        var depth = CAM + z2, s = f / depth;
        out.sx = cx + x1 * s; out.sy = cy + y2 * s; out.sd = depth; out.ss = s;
      }
      function depthAlpha(d) {
        var t = (CAM + 1.8 - d) / 3.4;
        return Math.max(0.15, Math.min(1, 0.2 + 0.85 * t));
      }

      var tmp = { sx: 0, sy: 0, sd: 0, ss: 0 };
      for (var k = 0; k < dust.length; k++) {
        var p = dust[k]; project(p.x, p.y, p.z, tmp);
        var da = depthAlpha(tmp.sd);
        ctx.globalAlpha = p.a * da * 0.75;
        var sz = p.s * 2.4 * (tmp.ss / f) * 3.4;
        ctx.drawImage(spBlue, tmp.sx - sz, tmp.sy - sz, sz * 2, sz * 2);
      }

      for (var i = 0; i < N; i++) {
        var n = nodes[i];
        var x = n.x + Math.sin(u * TAU * n.kx + n.px) * n.amp;
        var y = n.y + Math.sin(u * TAU * n.ky + n.py) * n.amp;
        var z = n.z + Math.sin(u * TAU * n.kz + n.pz) * n.amp;
        project(x, y, z, n);
      }

      ctx.lineCap = "round";
      for (var e = 0; e < edges.length; e++) {
        var ed = edges[e], A = nodes[ed.a], B = nodes[ed.b];
        var dm = (A.sd + B.sd) / 2, al = depthAlpha(dm);
        ctx.globalAlpha = al * 0.4;
        ctx.strokeStyle = "#2f7bff";
        ctx.lineWidth = Math.max(0.6, 1.0 * (f / dm) / f * 3.4);
        ctx.beginPath(); ctx.moveTo(A.sx, A.sy); ctx.lineTo(B.sx, B.sy); ctx.stroke();

        if (ed.pulse) {
          var ph = (u * ed.pk * ed.dir + ed.po) % 1; if (ph < 0) ph += 1;
          var tail = Math.max(0, ph - 0.15);
          var hx = A.sx + (B.sx - A.sx) * ph, hy = A.sy + (B.sy - A.sy) * ph;
          var tx = A.sx + (B.sx - A.sx) * tail, ty = A.sy + (B.sy - A.sy) * tail;
          var fade = Math.sin(ph * Math.PI);
          ctx.globalAlpha = al * 1.0 * fade;
          ctx.strokeStyle = "#7df0ff";
          ctx.lineWidth = Math.max(1.0, 1.8 * (f / dm) / f * 3.4);
          ctx.beginPath(); ctx.moveTo(tx, ty); ctx.lineTo(hx, hy); ctx.stroke();
          var gs = 12 * (f / dm) / f * 3.4;
          ctx.globalAlpha = al * fade;
          ctx.drawImage(spCyan, hx - gs, hy - gs, gs * 2, gs * 2);
        }
      }

      for (var i3 = 0; i3 < N; i3++) {
        var nd = nodes[i3], a3 = depthAlpha(nd.sd);
        var tw = 0.78 + 0.22 * Math.sin(u * TAU * nd.twk + nd.tph);
        var r = nd.size * 5.6 * (nd.ss / f) * 3.4;
        ctx.globalAlpha = Math.min(1, a3 * tw);
        ctx.drawImage(nd.hue ? spCyan : spBlue, nd.sx - r, nd.sy - r, r * 2, r * 2);
      }
      ctx.globalAlpha = 1;
      ctx.globalCompositeOperation = "source-over";
    }

    var isGalaxyVisible = true;
    var galaxyRaf = null;

    function checkGalaxyVisibility() {
      try {
        var frame = window.frameElement;
        if (frame && window.parent) {
          var rect = frame.getBoundingClientRect();
          var winH = window.parent.innerHeight || 800;
          var inView = (rect.bottom > -80 && rect.top < winH + 80);
          if (inView !== isGalaxyVisible) {
            isGalaxyVisible = inView;
            if (isGalaxyVisible && !galaxyRaf) {
              t0 = performance.now();
              galaxyRaf = requestAnimationFrame(tick);
            }
          }
        }
      } catch(e) {}
    }

    try {
      if (window.parent && window.parent.document) {
        var parentMain = window.parent.document.querySelector('section[data-testid="stMain"]') || window.parent;
        parentMain.addEventListener('scroll', checkGalaxyVisibility, { passive: true });
        window.parent.addEventListener('resize', checkGalaxyVisibility, { passive: true });
      }
    } catch(e) {}

    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) {
      frame(0.12);
      window.addEventListener("resize", function () { frame(0.12); });
    } else {
      var t0 = performance.now();
      function tick(now) {
        if (!isGalaxyVisible) {
          galaxyRaf = null;
          return;
        }
        frame((((now - t0) / 1000) % LOOP) / LOOP);
        galaxyRaf = requestAnimationFrame(tick);
      }
      galaxyRaf = requestAnimationFrame(tick);
    }
  })();
</script>
</body>
</html>
"""

components.html(retention_loop_html, height=690, scrolling=False)

# ==============================================================================
# SECTION 4: WHY RETAIN - BACKGROUND METAMORPHOSIS & BENTO PLATFORM
# ==============================================================================
st.markdown('<div id="why-retain"></div><div id="why-us"></div>', unsafe_allow_html=True)

scroll_transition_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..700&family=Instrument+Sans:ital,wght@0,400..600;1,400..600&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --font-display: 'Bricolage Grotesque', sans-serif;
    --font-body: 'Instrument Sans', sans-serif;
    --sheet-bg: #050b18;
    --cell-color: #9fb6d9;
    --line-color: #12243f;
    --red-alert: 255, 59, 70;
  }
  .brand {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    font-size: inherit;
    font-weight: 700;
    color: #F8FAFC !important;
    letter-spacing: -0.02em;
    display: inline-block;
  }
  .brand-ai {
    color: #38BDF8 !important;
    font-weight: 800 !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  }
  html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #030712;
    color: #F8FAFC;
    font-family: var(--font-body);
    user-select: none;
  }
  .excel-stage {
    position: absolute;
    inset: -60px;
    perspective: 1200px;
    overflow: hidden;
    pointer-events: none;
  }
  .excel-sheet {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 3600px;
    transform: translate(-50%, -50%) rotateX(15deg) rotateZ(-3deg) scale(1.22);
    font: 13px/1 "SF Mono", Menlo, Consolas, monospace;
    color: var(--cell-color);
    animation: excelPan 65s ease-in-out infinite alternate;
  }
  @keyframes excelPan {
    from { translate: 0 0; }
    to { translate: -700px 0; }
  }
  .excel-track {
    animation: excelScroll 55s linear infinite;
    will-change: transform;
  }
  @keyframes excelScroll {
    to { transform: translateY(var(--loop, -1360px)); }
  }
  .excel-row {
    display: grid;
    grid-template-columns: 80px 100px 170px 140px 150px 150px 90px 80px 110px 140px 560px 100px 140px 100px 120px;
    height: 34px;
    align-items: center;
    border-bottom: 1px solid var(--line-color);
    position: relative;
    white-space: nowrap;
  }
  .excel-row span {
    padding: 0 12px;
    overflow: hidden;
    text-overflow: ellipsis;
    border-right: 1px solid var(--line-color);
    height: 100%;
    display: flex;
    align-items: center;
  }
  .excel-row span:first-child { color: #4a6694; }
  .excel-row .err { color: #ff8f98; }
  .excel-row .dim { color: #4a6694; }
  .excel-row .hl { background: rgba(255, 214, 10, 0.12); }
  .excel-row .bl { background: rgba(60, 130, 255, 0.14); }
  .excel-row.risk::after {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(var(--red-alert), 0.22);
    box-shadow: inset 0 0 0 1px rgba(var(--red-alert), 0.50), 0 0 20px rgba(var(--red-alert), 0.30);
    opacity: 0;
    animation: excelFlash 5.5s ease-in-out infinite;
    animation-delay: var(--d, 0s);
  }
  @keyframes excelFlash {
    0%, 100% { opacity: 0; }
    15%, 32% { opacity: 0.9; }
    55% { opacity: 0; }
  }
  .excel-dof {
    position: absolute;
    inset: 0;
    pointer-events: none;
    backdrop-filter: blur(2.5px);
    -webkit-mask-image: linear-gradient(#000 0, #000 12%, transparent 32%, transparent 68%, #000 88%, #000 100%);
    mask-image: linear-gradient(#000 0, #000 12%, transparent 32%, transparent 68%, #000 88%, #000 100%);
  }
  .excel-light {
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: radial-gradient(75% 60% at 30% 40%, rgba(40, 90, 200, 0.22), transparent 75%),
                radial-gradient(130% 105% at 50% 50%, rgba(3, 7, 18, 0.45) 15%, rgba(3, 7, 18, 0.95) 100%);
  }
  .excel-scan {
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: repeating-linear-gradient(0deg, rgba(255,255,255,0.012) 0 1px, transparent 1px 3px);
    mix-blend-mode: screen;
  }

  /* Typewriter Blinking Cursor */
  .typewriter-cursor {
    display: inline-block;
    width: 3px;
    height: 1.15em;
    background-color: #38BDF8;
    margin-left: 5px;
    vertical-align: middle;
    animation: cursorBlink 0.8s infinite;
  }
  @keyframes cursorBlink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
  }

  /* ==========================================================================
     LAYER 2: WORKFORCE PULSE DASHBOARD LOOP STYLES
     ========================================================================== */
  .wp-app {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-rows: auto auto 1fr;
    gap: 12px;
    max-width: 100%;
    margin: 0 auto;
    padding: 24px 36px;
    pointer-events: none;
    box-sizing: border-box;
  }
  .wp-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .wp-title {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 600;
    letter-spacing: -0.01em;
    color: #cfe0ff;
  }
  .wp-live {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 11px;
    color: #7f97bd;
    font-family: var(--font-body);
  }
  .wp-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #2ee6a6;
    box-shadow: 0 0 10px #2ee6a6;
    animation: wpPulse 1.6s infinite;
  }
  @keyframes wpPulse { 50% { opacity: 0.35; } }
  .wp-kpis {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
  }
  .wp-card {
    background: rgba(12, 28, 52, 0.65);
    border: 1px solid rgba(120, 170, 255, 0.16);
    border-radius: 12px;
    padding: 10px 14px;
    backdrop-filter: blur(8px);
    position: relative;
  }
  .wp-card small {
    color: #7f97bd;
    font-size: 11px;
    display: block;
  }
  .wp-card b {
    display: block;
    font-size: 22px;
    font-weight: 700;
    margin-top: 2px;
    color: #dce9ff;
    font-variant-numeric: tabular-nums;
  }
  .wp-card i {
    font-style: normal;
    font-size: 11px;
  }
  .wp-main {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    grid-template-rows: 1.25fr 1fr;
    gap: 10px;
    min-height: 0;
  }
  .wp-main .wp-card {
    display: flex;
    flex-direction: column;
  }
  .wp-t {
    font-size: 11px;
    color: #7f97bd;
    margin-bottom: 6px;
    display: flex;
    justify-content: space-between;
  }
  .wp-leg span { margin-left: 10px; }
  .wp-leg em {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    margin-right: 4px;
  }
  .wp-canvas {
    width: 100%;
    flex: 1;
    min-height: 0;
    display: block;
  }
  .wp-line { grid-row: 1; }
  .wp-heat { grid-column: 2; grid-row: 1 / 3; }
  .wp-ai { grid-row: 2; }
  #wp-hm {
    display: grid;
    gap: 3px;
    flex: 1;
    min-height: 0;
    grid-template-columns: 85px repeat(10, 1fr);
    align-items: stretch;
  }
  #wp-hm .l {
    font-size: 10px;
    color: #7f97bd;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-right: 4px;
  }
  #wp-hm .c {
    border-radius: 3px;
    min-height: 10px;
  }
  .wp-scale {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 10px;
    color: #7f97bd;
    margin-top: 6px;
  }
  .wp-scale div {
    flex: 1;
    height: 4px;
    border-radius: 2px;
    background: linear-gradient(90deg, #2ee6a6, #ffb84a, #ff5a6e);
  }

  /* Frosted Glass Bento Capability Card */
  .bento-card-interactive {
    position: relative;
    background: rgba(10, 20, 45, 0.45);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    height: 170px;
    box-sizing: border-box;
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1),
                background 0.35s ease,
                border-color 0.35s ease;
    overflow: hidden;
  }
  .bento-card-interactive:hover {
    background: rgba(10, 20, 45, 0.65);
    transform: translateY(-2px);
    border-color: rgba(56, 189, 248, 0.25);
  }
</style>
</head>
<body class="bg-[#030712] w-full h-full overflow-hidden m-0 p-0">
  <div id="transition-root" class="w-full h-full m-0 p-0 overflow-hidden"></div>

  <script>
    const { useState, useEffect, useRef } = React;

    // SPREADSHEET ROW GENERATOR
    function generateSpreadsheetRows() {
      let s = 11;
      const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
      const pick = a => a[Math.floor(r() * a.length)];
      const names = ["A. Rao","M. Chen","S. Okafor","L. Meyer","P. Iyer","J. Silva","K. Tanaka","D. Novak","R. Haddad","E. Brooks","N. Kapoor","T. Larsen","Priya S.","chen, wei"];
      const depts = ["Engineering","Sales","Support","Finance","Product","Ops","People","Cust. Success"];
      const roles = ["Analyst","Sr. Engineer","Manager","Lead","Associate","Director","Sr Eng II","Acct Exec"];
      const mgrs = ["R. Mehta","B. Alvarez","#N/A","C. Ford","H. Lindqvist","(blank)","V. Rao","Unknown"];
      const reasons = ["Better offer","Career growth","Manager","Burnout","Comp","Relocation","Other","Personal"];
      const status = ["Filed","Pending","Unread","Unread","Filed","Review?","Unread","Closed"];
      const notes = [
        "Role matched expectations; happy with team",
        "Growth path unclear after reorg, no promo in 3 yrs",
        "Workload unsustainable for 3 quarters, asked for help twice",
        "Manager rarely gave feedback; skip-level never happened",
        "Compensation below market, counter-offer came too late",
        "Strong peers but limited promotion; 2 teammates also leaving",
        "Remote policy changed without notice",
        "Burned out, no backfill since March",
        "Accepted offer, 40% increase",
        "Praised onboarding, left for relocation"
      ];
      const risky = new Set([1, 2, 3, 4, 5, 6, 7]);
      const dt = () => {
        const d = 1 + Math.floor(r() * 28), m = 1 + Math.floor(r() * 12), y = pick([2024, 2025]);
        return `${d}/${m}/${y}`;
      };
      const N = 40;
      let rowsHtml = "";
      for (let i = 0; i < N; i++) {
        const n = Math.floor(r() * notes.length);
        const st = pick(status);
        const risk = risky.has(n) && st !== "Filed" && st !== "Closed" && r() > 0.3;
        const mg = pick(mgrs);
        const rt = r() > 0.85 ? "#REF!" : (1 + r() * 4).toFixed(1);
        const cd = r() > 0.8 ? "" : (r() > 0.5 ? "+" : "-") + Math.floor(r() * 30) + "%";
        rowsHtml += `
          <div class="excel-row ${risk ? "risk" : ""}" style="--d: ${(r() * 5.5).toFixed(2)}s">
            <span>${1000 + i}</span>
            <span>E${20000 + Math.floor(r() * 9999)}</span>
            <span>${pick(names)}</span>
            <span>${pick(depts)}</span>
            <span>${pick(roles)}</span>
            <span class="${mg[0] === "#" || mg[0] === "(" ? "err" : ""}">${mg}</span>
            <span>${(1 + r() * 9).toFixed(1)}y</span>
            <span class="${rt[0] === "#" ? "err" : ""}">${rt}</span>
            <span>${dt()}</span>
            <span class="${r() > 0.8 ? "hl" : ""}">${pick(reasons)}</span>
            <span>${notes[n]}</span>
            <span class="${st === "Unread" ? "err" : "dim"}">${st}</span>
            <span class="${r() > 0.7 ? "bl" : ""}">${cd || ""}</span>
            <span class="dim">${r() > 0.5 ? "Q" + (1 + Math.floor(r() * 4)) : ""}</span>
            <span class="${r() > 0.85 ? "err" : "dim"}">${r() > 0.85 ? "#VALUE!" : pick(["", "v2", "FINAL", "copy"])}</span>
          </div>`;
      }
      return { html: rowsHtml + rowsHtml, height: N * 34 };
    }

    // MAIN TRANSITION COMPONENT
    function TransitionComponent() {
      const [progress, setProgress] = useState(0); // 0 = Traditional HR Excel, 1 = RetAIn Platform

      // Simultaneous Typewriter Effect (Replays whenever scrolled into view)
      const fullText = "Billions lost to silent resignations, buried in endless spreadsheets.";
      const [typedText, setTypedText] = useState("");

      const triggerTypewriter = () => {
        if (window._typewriterTimer) {
          clearInterval(window._typewriterTimer);
          window._typewriterTimer = null;
        }
        setTypedText("");
        let idx = 0;
        window._typewriterTimer = setInterval(() => {
          if (idx <= fullText.length) {
            setTypedText(fullText.slice(0, idx));
            idx++;
          } else {
            clearInterval(window._typewriterTimer);
            window._typewriterTimer = null;
          }
        }, 34);
      };

      // Populate Spreadsheet Rows on Mount
      useEffect(() => {
        const track = document.getElementById("excel-track-fullscreen");
        if (track) {
          const { html, height } = generateSpreadsheetRows();
          track.innerHTML = html;
          track.style.setProperty("--loop", `-${height}px`);
        }
      }, []);

      // Mount Workforce Pulse Dashboard Loop Canvas Engine
      useEffect(() => {
        const ln = document.getElementById('wp-ln');
        const ai = document.getElementById('wp-ai');
        const hm = document.getElementById('wp-hm');
        if (!ln || !ai || !hm) return;

        const lx = ln.getContext('2d');
        const ax = ai.getContext('2d');
        const TAU = Math.PI * 2;
        const T = 16;
        const depts = ['Engineering','Sales','Support','Finance','Product','Marketing','Operations','Legal'];
        const COLS = 10;
        const cells = [];

        hm.innerHTML = '';
        depts.forEach((d, i) => {
          const l = document.createElement('div');
          l.className = 'l';
          l.innerHTML = `<span>${d}</span><b style="font-weight:500;color:#cfe0ff" id="wp-r${i}"></b>`;
          hm.appendChild(l);
          cells[i] = [];
          for (let j = 0; j < COLS; j++) {
            const c = document.createElement('div');
            c.className = 'c';
            hm.appendChild(c);
            cells[i][j] = c;
          }
        });
        hm.style.gridTemplateRows = `repeat(${depts.length}, 1fr)`;

        function heatCol(v) {
          const g = [46, 230, 166], a = [255, 184, 74], r = [255, 90, 110];
          const [p, q, f] = v < 0.5 ? [g, a, v * 2] : [a, r, (v - 0.5) * 2];
          return p.map((x, i) => Math.round(x + (q[i] - x) * f));
        }

        let LD = 1, AD = 1;
        function sz(cv) {
          const D = Math.min(window.devicePixelRatio || 1, 2);
          const b = cv.getBoundingClientRect();
          cv.width = b.width * D;
          cv.height = b.height * D;
          return D;
        }
        function rs() {
          if (ln && ai) {
            LD = sz(ln);
            AD = sz(ai);
          }
        }
        window.addEventListener('resize', rs);
        rs();

        const sig = [
          (x, u) => 0.55 + 0.16 * Math.sin(TAU * (x * 1.3 + u * 1)) + 0.07 * Math.sin(TAU * (x * 3.1 + u * 2)),
          (x, u) => 0.68 + 0.12 * Math.sin(TAU * (x * 1.9 + u * 1 + 0.2)) + 0.06 * Math.sin(TAU * (x * 4 + u * 3)),
          (x, u) => 0.42 + 0.17 * Math.sin(TAU * (x * 1.1 + u * 1 + 0.6)) + 0.05 * Math.sin(TAU * (x * 3.7 + u * 2))
        ];
        const cols = ['61,139,255', '46,230,166', '255,184,74'];

        function drawLine(u) {
          const w = ln.width, h = ln.height, D = LD, pl = 34 * D, pb = 18 * D, pt = 6 * D;
          lx.clearRect(0, 0, w, h);
          lx.font = `${10 * D}px system-ui`;
          lx.fillStyle = '#6f87ad';
          lx.strokeStyle = 'rgba(120,170,255,.1)';
          lx.lineWidth = D;
          for (let i = 0; i <= 4; i++) {
            const y = pt + (h - pt - pb) * i / 4;
            lx.beginPath(); lx.moveTo(pl, y); lx.lineTo(w, y); lx.stroke();
            lx.fillText(100 - i * 20, 2 * D, y + 3 * D);
          }
          sig.forEach((f, k) => {
            const pts = [];
            for (let i = 0; i <= 120; i++) {
              const s = i / 120;
              pts.push([pl + s * (w - pl), pt + (h - pt - pb) * (1 - f(s, u))]);
            }
            const path = () => {
              lx.beginPath();
              pts.forEach((p, i) => i ? lx.lineTo(p[0], p[1]) : lx.moveTo(p[0], p[1]));
            };
            if (k === 0) {
              path();
              lx.lineTo(w, h - pb);
              lx.lineTo(pl, h - pb);
              const g = lx.createLinearGradient(0, pt, 0, h);
              g.addColorStop(0, 'rgba(61,139,255,.26)');
              g.addColorStop(1, 'rgba(61,139,255,0)');
              lx.fillStyle = g;
              lx.fill();
            }
            lx.lineJoin = 'round';
            lx.lineCap = 'round';
            lx.shadowColor = `rgb(${cols[k]})`;
            lx.shadowBlur = 14 * D;
            lx.strokeStyle = `rgba(${cols[k]},${k ? 0.8 : 1})`;
            lx.lineWidth = (k ? 1.6 : 2.4) * D;
            path();
            lx.stroke();
            lx.shadowBlur = 0;
            const e = pts[pts.length - 1], pu = 0.5 + 0.5 * Math.sin(TAU * u * 4);
            const gr = lx.createRadialGradient(e[0], e[1], 0, e[0], e[1], (8 + 6 * pu) * D);
            gr.addColorStop(0, `rgba(${cols[k]},.9)`);
            gr.addColorStop(1, `rgba(${cols[k]},0)`);
            lx.fillStyle = gr;
            lx.beginPath();
            lx.arc(e[0], e[1], (8 + 6 * pu) * D, 0, TAU);
            lx.fill();
          });
          const cx = pl + (w - pl) * ((u * 2) % 1);
          lx.strokeStyle = 'rgba(46,230,166,.25)';
          lx.lineWidth = D;
          lx.beginPath();
          lx.moveTo(cx, pt);
          lx.lineTo(cx, h - pb);
          lx.stroke();
        }

        const L = [3, 5, 4, 2], NP = [];
        function layout(w, h) {
          NP.length = 0;
          L.forEach((n, i) => {
            const col = [];
            for (let j = 0; j < n; j++) {
              col.push([w * (0.1 + 0.8 * i / (L.length - 1)), h * (0.15 + 0.7 * (n === 1 ? 0.5 : j / (n - 1)))]);
            }
            NP.push(col);
          });
        }

        function drawAI(u) {
          const w = ai.width, h = ai.height, D = AD;
          layout(w, h);
          ax.clearRect(0, 0, w, h);
          for (let i = 0; i < L.length - 1; i++) {
            NP[i].forEach((a, j) => NP[i + 1].forEach((b, m) => {
              const o = ((j * 7 + m * 3 + i * 5) % 10) / 10;
              const g = i / (L.length - 2);
              ax.strokeStyle = `rgba(${g > 0.5 ? '46,230,166' : '61,139,255'},.14)`;
              ax.lineWidth = D;
              ax.beginPath();
              ax.moveTo(a[0], a[1]);
              ax.lineTo(b[0], b[1]);
              ax.stroke();
              const p = (u * 2 + o) % 1, f = Math.sin(p * Math.PI);
              if ((j + m + i) % 2 === 0) {
                const x = a[0] + (b[0] - a[0]) * p, y = a[1] + (b[1] - a[1]) * p;
                const gr = ax.createRadialGradient(x, y, 0, x, y, 9 * D);
                const c = g > 0.5 ? '46,230,166' : '61,139,255';
                gr.addColorStop(0, `rgba(${c},${0.9 * f})`);
                gr.addColorStop(1, `rgba(${c},0)`);
                ax.fillStyle = gr;
                ax.beginPath();
                ax.arc(x, y, 9 * D, 0, TAU);
                ax.fill();
              }
            }));
          }
          NP.forEach((col, i) => col.forEach((p, j) => {
            const a = 0.5 + 0.5 * Math.sin(TAU * (u * 2 - i * 0.18 + j * 0.07)), c = i > 2 ? '46,230,166' : '61,139,255';
            const gl = ax.createRadialGradient(p[0], p[1], 0, p[0], p[1], 16 * D);
            gl.addColorStop(0, `rgba(${c},${0.15 + 0.4 * a})`);
            gl.addColorStop(1, `rgba(${c},0)`);
            ax.fillStyle = gl;
            ax.beginPath();
            ax.arc(p[0], p[1], 16 * D, 0, TAU);
            ax.fill();
            ax.fillStyle = `rgb(${c})`;
            ax.beginPath();
            ax.arc(p[0], p[1], 3.5 * D, 0, TAU);
            ax.fill();
          }));
        }

        function drawHeat(u) {
          depts.forEach((d, i) => {
            let s = 0;
            for (let j = 0; j < COLS; j++) {
              const base = [0.35, 0.5, 0.62, 0.3, 0.45, 0.4, 0.55, 0.25][i];
              const v = Math.min(1, Math.max(0, base + 0.34 * Math.sin(TAU * (u * 1 + i * 0.11 + j * 0.06)) + 0.12 * Math.sin(TAU * (u * 2 - j * 0.13 + i * 0.3))));
              const [r, g, b] = heatCol(v);
              cells[i][j].style.background = `rgba(${r},${g},${b},${0.35 + 0.5 * v})`;
              cells[i][j].style.boxShadow = v > 0.72 ? `0 0 10px rgba(${r},${g},${b},.55)` : 'none';
              s += v;
            }
            const avg = s / COLS;
            const rEl = document.getElementById(`wp-r${i}`);
            if (rEl) rEl.textContent = Math.round(avg * 100);
          });
        }

        function drawKpi(u) {
          const w = x => 0.5 + 0.5 * Math.sin(TAU * (u + x));
          const k1 = document.getElementById('wp-k1');
          const d1 = document.getElementById('wp-d1');
          if (k1) k1.textContent = (72 + 8 * w(0)).toFixed(1);
          if (d1) d1.innerHTML = `<span style="color:#2ee6a6">▲ ${(1 + 2 * w(0.1)).toFixed(1)}</span> <span style="color:#7f97bd">vs last week</span>`;
          const n = Math.round(2 + 4 * w(0.3));
          const k2 = document.getElementById('wp-k2');
          const d2 = document.getElementById('wp-d2');
          if (k2) k2.textContent = n;
          if (d2) d2.innerHTML = `<span style="color:${n > 4 ? '#ff5a6e' : '#ffb84a'}">${n > 4 ? 'Needs attention' : 'Monitoring'}</span>`;
          const k3 = document.getElementById('wp-k3');
          const d3 = document.getElementById('wp-d3');
          if (k3) k3.textContent = Math.round(64 + 10 * w(0.55)) + '%';
          if (d3) d3.innerHTML = `<span style="color:#3d8bff">Surveys, chat, 1:1s</span>`;
          const k4 = document.getElementById('wp-k4');
          const d4 = document.getElementById('wp-d4');
          if (k4) k4.textContent = (6 + 2.5 * w(0.8)).toFixed(1) + '%';
          if (d4) d4.innerHTML = `<span style="color:#7f97bd">Next 90 days</span>`;
        }

        let isSection4Visible = true;
        let loopRaf = null;

        try {
          const obs4 = new IntersectionObserver((entries) => {
            isSection4Visible = entries[0].isIntersecting;
            if (isSection4Visible && !loopRaf) {
              loopRaf = requestAnimationFrame(loop);
            }
          }, { threshold: 0.02 });
          obs4.observe(document.body);
        } catch(e) {}

        function loop(now) {
          if (!isSection4Visible) {
            loopRaf = null;
            return;
          }
          const u = ((now / 1000) % T) / T;
          drawLine(u);
          drawAI(u);
          drawHeat(u);
          drawKpi(u);
          loopRaf = requestAnimationFrame(loop);
        }
        loopRaf = requestAnimationFrame(loop);

        return () => {
          window.removeEventListener('resize', rs);
          if (loopRaf) cancelAnimationFrame(loopRaf);
        };
      }, []);

      // Scroll physics with Calibrated Timing Balance & Zero-Jank Throttling
      useEffect(() => {
        let parentWin, parentDoc, scroller;
        try {
          parentDoc = window.parent.document;
          parentWin = window.parent;
          scroller = parentDoc.querySelector('section.stMain') || 
                     parentDoc.querySelector('[data-testid="stMain"]') || 
                     parentDoc.querySelector('[data-testid="stAppViewContainer"]') || 
                     parentWin;
        } catch (e) {
          scroller = window;
          parentWin = window;
        }

        let targetP = 0;
        let currentP = 0;
        let lastReportedP = -1;
        let rafId = null;
        let scrollTicking = false;
        let hasExitedAbove = true;
        let hasExitedBelow = false;

        const checkInViewAndScroll = () => {
          if (!scrollTicking) {
            window.requestAnimationFrame(() => {
              try {
                const frame = window.frameElement;
                if (!frame) return;
                const rect = frame.getBoundingClientRect();
                const winH = parentWin.innerHeight || window.innerHeight;

                const isAbove = rect.top >= winH * 0.75;
                const isBelow = rect.bottom <= 100;
                const isInView = rect.top < winH * 0.75 && rect.bottom > 100;

                if (isAbove) {
                  hasExitedAbove = true;
                }
                if (isBelow) {
                  hasExitedBelow = true;
                }

                if (isInView && (hasExitedAbove || hasExitedBelow)) {
                  hasExitedAbove = false;
                  hasExitedBelow = false;
                  triggerTypewriter();
                }

                const startY = 200;
                const endY = 50;
                const raw = (startY - rect.top) / (startY - endY);
                targetP = Math.max(0, Math.min(1, raw));
                
                // Wake up tick animation loop only while actively moving
                if (!isTickingActive) {
                  isTickingActive = true;
                  rafId = requestAnimationFrame(tick);
                }
              } catch (err) {}
              scrollTicking = false;
            });
            scrollTicking = true;
          }
        };

        let isTickingActive = false;
        const tick = () => {
          currentP += (targetP - currentP) * 0.16;
          if (Math.abs(targetP - currentP) < 0.001) {
            currentP = targetP;
          }
          // Optimized render threshold: silky smooth 60fps without redundant React reconciliations
          if (Math.abs(currentP - lastReportedP) > 0.003) {
            lastReportedP = currentP;
            setProgress(currentP);
          }
          if (Math.abs(targetP - currentP) >= 0.001) {
            rafId = requestAnimationFrame(tick);
          } else {
            isTickingActive = false;
          }
        };

        const targetEl = (scroller && scroller.addEventListener) ? scroller : parentWin;
        if (targetEl && targetEl.addEventListener) {
          targetEl.addEventListener('scroll', checkInViewAndScroll, { passive: true });
        }
        window.addEventListener('resize', checkInViewAndScroll);
        checkInViewAndScroll();

        return () => {
          if (targetEl && targetEl.removeEventListener) {
            targetEl.removeEventListener('scroll', checkInViewAndScroll);
          }
          window.removeEventListener('resize', checkInViewAndScroll);
          if (rafId) cancelAnimationFrame(rafId);
          if (window._typewriterTimer) {
            clearInterval(window._typewriterTimer);
            window._typewriterTimer = null;
          }
        };
      }, []);

      // Dynamic Metamorphosis Opacities & Transforms (Hardware-accelerated)
      // DWELL ZONE: Excel layer stays 100% visible for the initial scroll segment
      const excelOpacity = progress < 0.22 ? 1 : Math.max(0, 1 - (progress - 0.22) * 1.6);

      // Text 1 (Traditional HR Headline + Typewriter) stays crystal clear during dwell, then cleanly dissolves before Bento arrives
      const text1Opacity = progress < 0.25 ? 1 : Math.max(0, 1 - (progress - 0.25) * 2.5);
      const text1Y = progress < 0.25 ? 0 : -(progress - 0.25) * 35;

      // Layer 2: Workforce Pulse Dashboard Loop gently emerges after Excel begins softening
      const pulseOpacity = progress < 0.2 ? 0 : Math.min(1, (progress - 0.2) * 1.5);

      // Layer 3: RetAIn Platform + 4 Bento Cards emerge after Traditional HR clears
      const bentoProgress = Math.min(1, Math.max(0, (progress - 0.45) / 0.55));
      const bentoOpacity = bentoProgress;
      const bentoY = (1 - bentoProgress) * 20;
      const bentoScale = 0.98 + bentoProgress * 0.02;

      return React.createElement('div', {
        className: 'relative w-full h-[780px] overflow-hidden bg-[#030712]'
      },
        // ====================================================================
        // BACKGROUND LAYER 1: 100% FULL-SCREEN 3D EXCEL SPREADSHEET LOOP (GPU-Accelerated)
        // ====================================================================
        React.createElement('div', {
          className: 'absolute inset-0 w-full h-full pointer-events-none will-change-transform',
          style: {
            opacity: excelOpacity,
            transform: 'translate3d(0, 0, 0)',
            display: excelOpacity <= 0 ? 'none' : 'block'
          }
        },
          React.createElement('div', { className: 'excel-stage' },
            React.createElement('div', { className: 'excel-sheet' },
              React.createElement('div', { id: 'excel-track-fullscreen', className: 'excel-track' })
            )
          ),
          React.createElement('div', { className: 'excel-dof' }),
          React.createElement('div', { className: 'excel-light' }),
          React.createElement('div', { className: 'excel-scan' })
        ),

        // ====================================================================
        // BACKGROUND LAYER 2: WORKFORCE PULSE DASHBOARD LOOP (LIVE CANVAS ENGINE)
        // ====================================================================
        React.createElement('div', {
          className: 'absolute inset-0 w-full h-full pointer-events-none will-change-transform',
          style: {
            opacity: pulseOpacity,
            display: pulseOpacity <= 0 ? 'none' : 'block'
          }
        },
          // Workforce Pulse DOM Structure
          React.createElement('div', { className: 'wp-app' },
            React.createElement('header', { className: 'wp-header' },
              React.createElement('h1', { className: 'wp-title' }, 'Workforce Pulse'),
              React.createElement('div', { className: 'wp-live' },
                React.createElement('span', { className: 'wp-dot' }),
                'Live · processing 48,210 signals'
              )
            ),
            React.createElement('section', { className: 'wp-kpis' },
              React.createElement('div', { className: 'wp-card' },
                React.createElement('small', null, 'Sentiment index'),
                React.createElement('b', { id: 'wp-k1' }, '72.4'),
                React.createElement('i', { id: 'wp-d1' })
              ),
              React.createElement('div', { className: 'wp-card' },
                React.createElement('small', null, 'Teams at risk'),
                React.createElement('b', { id: 'wp-k2' }, '3'),
                React.createElement('i', { id: 'wp-d2' })
              ),
              React.createElement('div', { className: 'wp-card' },
                React.createElement('small', null, 'Engagement'),
                React.createElement('b', { id: 'wp-k3' }, '68%'),
                React.createElement('i', { id: 'wp-d3' })
              ),
              React.createElement('div', { className: 'wp-card' },
                React.createElement('small', null, 'Attrition forecast'),
                React.createElement('b', { id: 'wp-k4' }, '7.1%'),
                React.createElement('i', { id: 'wp-d4' })
              )
            ),
            React.createElement('section', { className: 'wp-main' },
              React.createElement('div', { className: 'wp-card wp-line' },
                React.createElement('div', { className: 'wp-t' },
                  React.createElement('span', null, 'Sentiment trend'),
                  React.createElement('span', { className: 'wp-leg' },
                    React.createElement('span', null, React.createElement('em', { style: { background: '#3d8bff' } }), 'Company'),
                    React.createElement('span', null, React.createElement('em', { style: { background: '#2ee6a6' } }), 'Engineering'),
                    React.createElement('span', null, React.createElement('em', { style: { background: '#ffb84a' } }), 'Support')
                  )
                ),
                React.createElement('canvas', { id: 'wp-ln', className: 'wp-canvas' })
              ),
              React.createElement('div', { className: 'wp-card wp-heat' },
                React.createElement('div', { className: 'wp-t' },
                  React.createElement('span', null, 'Department risk'),
                  React.createElement('span', null, 'last 10 weeks')
                ),
                React.createElement('div', { id: 'wp-hm' }),
                React.createElement('div', { className: 'wp-scale' },
                  'Low',
                  React.createElement('div', null),
                  'High'
                )
              ),
              React.createElement('div', { className: 'wp-card wp-ai' },
                React.createElement('div', { className: 'wp-t' },
                  React.createElement('span', null, 'Signal processing'),
                  React.createElement('span', null, 'Surveys · Chat · HRIS')
                ),
                React.createElement('canvas', { id: 'wp-ai', className: 'wp-canvas' })
              )
            )
          ),
          // Dark moody overlay so Bento cards have 100% legibility while live ambient waves glow through
          React.createElement('div', {
            className: 'absolute inset-0 w-full h-full pointer-events-none',
            style: {
              background: 'radial-gradient(ellipse at 50% 50%, rgba(3, 7, 18, 0.60) 0%, rgba(3, 7, 18, 0.90) 100%)',
              backdropFilter: 'blur(1.5px)'
            }
          })
        ),

        // ====================================================================
        // FOREGROUND 1: TRADITIONAL HR HEADLINE + ACTIVE TYPEWRITER SUBTITLE
        // ====================================================================
        React.createElement('div', {
          className: 'absolute inset-0 z-20 w-full h-full flex flex-col justify-start items-center text-center pt-12 md:pt-16 lg:pt-20 px-6 pointer-events-none will-change-transform',
          style: {
            opacity: text1Opacity,
            transform: `translateY(${text1Y}px)`,
            display: text1Opacity <= 0 ? 'none' : 'flex'
          }
        },
          // Hero Headline on Top + Active Simultaneous Typewriter Subtitle
          React.createElement('div', { className: 'max-w-4xl' },
            React.createElement('h2', {
              className: 'text-3xl md:text-5xl lg:text-6xl font-black tracking-tight leading-tight mb-4',
              style: {
                fontFamily: 'var(--font-display)',
                letterSpacing: '-0.025em',
                background: 'linear-gradient(135deg, #FFFFFF 65%, #38BDF8 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                filter: 'drop-shadow(0 4px 16px rgba(0,0,0,0.95))'
              }
            }, 'Why Traditional HR Systems Fail'),
            React.createElement('div', {
              className: 'text-slate-200 text-lg md:text-2xl font-medium tracking-wide min-h-[44px] flex items-center justify-center drop-shadow-[0_2px_8px_rgba(0,0,0,0.95)]'
            },
              typedText,
              React.createElement('span', { className: 'typewriter-cursor' })
            )
          )
        ),

        // ====================================================================
        // FOREGROUND 2: RETAIN PLATFORM + 4 SEPARATELY PLACED BENTO CARDS
        // ====================================================================
        React.createElement('div', {
          className: 'absolute inset-0 z-20 w-full h-full flex flex-col justify-center p-6 md:p-10 will-change-transform',
          style: {
            opacity: bentoOpacity,
            transform: `translateY(${bentoY}px) scale(${bentoScale})`,
            pointerEvents: bentoProgress < 0.5 ? 'none' : 'auto',
            display: bentoOpacity <= 0 ? 'none' : 'flex'
          }
        },
          // Header: Proactive, Continuous & High-ROI
          React.createElement('div', {
            className: 'w-full max-w-7xl mx-auto flex items-center justify-between pb-4 md:pb-5 px-1 -mt-4 md:-mt-6'
          },
            React.createElement('h3', {
              className: 'text-3xl md:text-4xl lg:text-[2.35rem] font-extrabold tracking-tight',
              style: {
                fontFamily: 'var(--font-display)',
                letterSpacing: '-0.025em',
                lineHeight: '1.2',
                background: 'linear-gradient(135deg, #FFFFFF 65%, #38BDF8 100%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                filter: 'drop-shadow(0 2px 12px rgba(0,0,0,0.85))'
              }
            }, 'Proactive, Continuous & High-ROI')
          ),

          // 4 Proactive, Continuous & High-ROI Bento Capability Cards (2x2 Grid with generous column spacing)
          React.createElement('div', {
            className: 'w-full max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-7 my-2 px-1'
          },
            // Bento Card 1: Continuous NLP Mining
            React.createElement('div', {
              className: 'bento-card-interactive flex flex-row items-center justify-between p-5 md:p-6 w-full'
            },
              React.createElement('div', {
                className: 'flex flex-col justify-start h-full pt-4',
                style: { width: '62%', flexShrink: 0, paddingRight: '10px' }
              },
                React.createElement('h4', {
                  className: 'text-lg md:text-[1.14rem] font-bold text-white mb-2 whitespace-nowrap',
                  style: { fontFamily: 'var(--font-display)', letterSpacing: '-0.01em' }
                }, 'Continuous NLP Mining'),
                React.createElement('p', {
                  className: 'text-xs md:text-sm font-normal leading-relaxed truncate',
                  style: { color: '#E2E8F0' }
                }, 'Converts qualitative feedback into trend signals')
              ),
              React.createElement('div', {
                className: 'flex items-center justify-center flex-shrink-0',
                style: { width: '38%', height: '140px', boxSizing: 'border-box' }
              },
                React.createElement('div', {
                  style: { display: 'flex', flexDirection: 'column', gap: '8px', width: '100%', maxWidth: '140px' }
                },
                  React.createElement('div', { style: { display: 'flex', gap: '5px', alignItems: 'center' } },
                    React.createElement('div', { style: { height: '6px', width: '32px', borderRadius: '3px', background: 'rgba(255, 255, 255, 0.12)' } }),
                    React.createElement('div', { style: { height: '14px', width: '60px', borderRadius: '3px', background: 'rgba(56, 189, 248, 0.18)', border: '1px solid rgba(56, 189, 248, 0.35)' } }),
                    React.createElement('div', { style: { height: '6px', width: '20px', borderRadius: '3px', background: 'rgba(255, 255, 255, 0.08)' } })
                  ),
                  React.createElement('div', { style: { display: 'flex', gap: '5px', alignItems: 'center' } },
                    React.createElement('div', { style: { height: '14px', width: '48px', borderRadius: '3px', background: 'rgba(56, 189, 248, 0.18)', border: '1px solid rgba(56, 189, 248, 0.35)' } }),
                    React.createElement('div', { style: { height: '6px', width: '56px', borderRadius: '3px', background: 'rgba(255, 255, 255, 0.12)' } })
                  ),
                  React.createElement('div', { style: { marginTop: '4px' } },
                    React.createElement('span', {
                      style: {
                        display: 'inline-block',
                        fontSize: '10px',
                        fontFamily: 'var(--font-body)',
                        color: 'rgba(56, 189, 248, 0.85)',
                        border: '1px solid rgba(56, 189, 248, 0.35)',
                        borderRadius: '4px',
                        padding: '2px 7px',
                        letterSpacing: '0.03em'
                      }
                    }, 'comp drift')
                  )
                )
              )
            ),

            // Bento Card 2: Privacy-First Cohort Radar
            React.createElement('div', {
              className: 'bento-card-interactive flex flex-row items-center justify-between p-5 md:p-6 w-full'
            },
              React.createElement('div', {
                className: 'flex flex-col justify-start h-full pt-4',
                style: { width: '62%', flexShrink: 0, paddingRight: '10px' }
              },
                React.createElement('h4', {
                  className: 'text-lg md:text-[1.14rem] font-bold text-white mb-2 whitespace-nowrap',
                  style: { fontFamily: 'var(--font-display)', letterSpacing: '-0.01em' }
                }, 'Privacy-First Cohort Radar'),
                React.createElement('p', {
                  className: 'text-xs md:text-sm font-normal leading-relaxed truncate',
                  style: { color: '#E2E8F0' }
                }, 'Team-level early flight risk detection')
              ),
              React.createElement('div', {
                className: 'flex items-center justify-center flex-shrink-0',
                style: { width: '38%', height: '140px', boxSizing: 'border-box' }
              },
                React.createElement('div', {
                  style: {
                    display: 'grid',
                    gridTemplateColumns: 'repeat(5, 14px)',
                    gap: '4px'
                  }
                },
                  [
                    'cyan', 'cyan', 'cyan', 'amber', 'cyan',
                    'cyan', 'amber', 'cyan', 'cyan', 'red',
                    'cyan', 'cyan', 'cyan', 'cyan', 'cyan',
                    'cyan', 'red', 'cyan', 'amber', 'cyan'
                  ].map((type, idx) => {
                    let bg = 'rgba(56, 189, 248, 0.15)';
                    if (type === 'amber') bg = 'rgba(245, 158, 11, 0.60)';
                    if (type === 'red') bg = 'rgba(239, 68, 68, 0.60)';
                    return React.createElement('div', {
                      key: idx,
                      style: {
                        width: '14px',
                        height: '14px',
                        borderRadius: '3px',
                        background: bg
                      }
                    });
                  })
                )
              )
            ),

            // Bento Card 3: Pre-Emptive Micro-Pulses
            React.createElement('div', {
              className: 'bento-card-interactive flex flex-row items-center justify-between p-5 md:p-6 w-full'
            },
              React.createElement('div', {
                className: 'flex flex-col justify-start h-full pt-4',
                style: { width: '62%', flexShrink: 0, paddingRight: '10px' }
              },
                React.createElement('h4', {
                  className: 'text-lg md:text-[1.14rem] font-bold text-white mb-2 whitespace-nowrap',
                  style: { fontFamily: 'var(--font-display)', letterSpacing: '-0.01em' }
                }, 'Pre-Emptive Micro-Pulses'),
                React.createElement('p', {
                  className: 'text-xs md:text-sm font-normal leading-relaxed truncate',
                  style: { color: '#E2E8F0' }
                }, 'Non leading 2 question checks')
              ),
              React.createElement('div', {
                className: 'flex items-center justify-center flex-shrink-0',
                style: { width: '38%', height: '140px', boxSizing: 'border-box' }
              },
                React.createElement('div', {
                  style: { display: 'flex', flexDirection: 'column', width: '100%', maxWidth: '120px' }
                },
                  React.createElement('div', {
                    style: {
                      alignSelf: 'flex-start',
                      width: '94px',
                      height: '22px',
                      borderRadius: '7px 7px 7px 2px',
                      background: 'rgba(56, 189, 248, 0.12)',
                      border: '1px solid rgba(56, 189, 248, 0.22)',
                      display: 'flex',
                      alignItems: 'center',
                      padding: '0 8px'
                    }
                  },
                    React.createElement('div', { style: { height: '4px', width: '56px', borderRadius: '2px', background: 'rgba(56, 189, 248, 0.35)' } })
                  ),
                  React.createElement('div', {
                    style: {
                      alignSelf: 'flex-end',
                      width: '68px',
                      height: '20px',
                      marginTop: '6px',
                      borderRadius: '7px 7px 2px 7px',
                      background: 'rgba(56, 189, 248, 0.18)',
                      border: '1px solid rgba(56, 189, 248, 0.30)',
                      display: 'flex',
                      alignItems: 'center',
                      padding: '0 8px'
                    }
                  },
                    React.createElement('div', { style: { height: '4px', width: '38px', borderRadius: '2px', background: 'rgba(56, 189, 248, 0.45)' } })
                  ),
                  React.createElement('div', {
                    style: {
                      width: '100%',
                      height: '2px',
                      borderRadius: '1px',
                      background: 'rgba(255, 255, 255, 0.10)',
                      marginTop: '12px',
                      overflow: 'hidden',
                      position: 'relative'
                    }
                  },
                    React.createElement('div', {
                      style: { width: '40%', height: '100%', background: '#38bdf8', opacity: 0.65, borderRadius: '1px' }
                    })
                  )
                )
              )
            ),

            // Bento Card 4: Modeled Action Playbooks
            React.createElement('div', {
              className: 'bento-card-interactive flex flex-row items-center justify-between p-5 md:p-6 w-full'
            },
              React.createElement('div', {
                className: 'flex flex-col justify-start h-full pt-4',
                style: { width: '62%', flexShrink: 0, paddingRight: '10px' }
              },
                React.createElement('h4', {
                  className: 'text-lg md:text-[1.14rem] font-bold text-white mb-2 whitespace-nowrap',
                  style: { fontFamily: 'var(--font-display)', letterSpacing: '-0.01em' }
                }, 'Modeled Action Playbooks'),
                React.createElement('p', {
                  className: 'text-xs md:text-sm font-normal leading-relaxed truncate',
                  style: { color: '#E2E8F0' }
                }, 'Targeted, policy-aligned retention playbooks')
              ),
              React.createElement('div', {
                className: 'flex items-center justify-center flex-shrink-0',
                style: { width: '38%', height: '140px', boxSizing: 'border-box' }
              },
                React.createElement('div', {
                  style: { display: 'flex', flexDirection: 'column', gap: '9px', width: '100%', maxWidth: '125px' }
                },
                  React.createElement('div', { style: { display: 'flex', alignItems: 'center', gap: '7px' } },
                    React.createElement('div', {
                      style: {
                        width: '15px',
                        height: '15px',
                        borderRadius: '50%',
                        border: '1.5px solid rgba(56, 189, 248, 0.70)',
                        background: 'rgba(56, 189, 248, 0.14)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        flexShrink: 0
                      }
                    },
                      React.createElement('svg', {
                        width: '8', height: '8', viewBox: '0 0 10 10', fill: 'none'
                      },
                        React.createElement('path', {
                          d: 'M2 5.2L4.2 7.4L8.2 2.6',
                          stroke: '#38bdf8',
                          strokeWidth: '1.8',
                          strokeLinecap: 'round',
                          strokeLinejoin: 'round'
                        })
                      )
                    ),
                    React.createElement('div', { style: { height: '5px', width: '78px', borderRadius: '3px', background: 'rgba(255, 255, 255, 0.14)' } })
                  ),
                  React.createElement('div', { style: { display: 'flex', alignItems: 'center', gap: '7px' } },
                    React.createElement('div', {
                      style: {
                        width: '15px',
                        height: '15px',
                        borderRadius: '50%',
                        border: '1.5px solid rgba(56, 189, 248, 0.70)',
                        background: 'rgba(56, 189, 248, 0.14)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        flexShrink: 0
                      }
                    },
                      React.createElement('svg', {
                        width: '8', height: '8', viewBox: '0 0 10 10', fill: 'none'
                      },
                        React.createElement('path', {
                          d: 'M2 5.2L4.2 7.4L8.2 2.6',
                          stroke: '#38bdf8',
                          strokeWidth: '1.8',
                          strokeLinecap: 'round',
                          strokeLinejoin: 'round'
                        })
                      )
                    ),
                    React.createElement('div', { style: { height: '5px', width: '64px', borderRadius: '3px', background: 'rgba(255, 255, 255, 0.14)' } })
                  ),
                  React.createElement('div', { style: { display: 'flex', alignItems: 'center', gap: '7px' } },
                    React.createElement('div', {
                      style: {
                        width: '15px',
                        height: '15px',
                        borderRadius: '50%',
                        border: '1.5px solid rgba(255, 255, 255, 0.22)',
                        background: 'transparent',
                        flexShrink: 0
                      }
                    }),
                    React.createElement('div', { style: { height: '5px', width: '52px', borderRadius: '3px', background: 'rgba(255, 255, 255, 0.08)' } })
                  )
                )
              )
            )
          )
        )
      );
    }

    ReactDOM.createRoot(document.getElementById('transition-root')).render(React.createElement(TransitionComponent));
  </script>
</body>
</html>
"""

components.html(scroll_transition_html, height=780, scrolling=False)

# ==============================================================================
# SECTION 5: CONTACT & STAKEHOLDER DEMO INQUIRY
# ==============================================================================
st.markdown('<div id="contact"><span id="contact-section-anchor"></span></div>', unsafe_allow_html=True)

cont_left, cont_right = st.columns([1.08, 0.92], gap="large")

with cont_left:
    contact_left_html = """<div class="pilot-left-col">
<h2 style="font-size: 2.1rem; font-weight: 700; color: #FFFFFF; line-height: 1.22; letter-spacing: -0.01em; margin-bottom: 0.65rem; font-family: var(--font-display);">
How <span class="brand">Ret<span class="brand-ai">AI</span>n</span> Works in Real-World Deployment
</h2>
<p style="color: #94A3B8; font-size: 0.94rem; line-height: 1.6; margin-bottom: 1.4rem;">
Turn predictive telemetry into closed-loop enterprise retention workflows.
</p>

<!-- Vertical Deployment Pipeline -->
<div class="pipeline-container" style="display: flex; flex-direction: column; margin-bottom: 1.4rem;">
  <!-- Step 1: HRMS API SYNC -->
  <div class="pipeline-step pipeline-step-1" style="position: relative; padding-left: 28px; padding-bottom: 32px; background: transparent; border: none; border-radius: 0;">
    <div class="pipeline-line" style="position: absolute; left: 14px; top: 37px; bottom: -1px; width: 1px; background-color: rgba(56, 189, 248, 0.20);"></div>
    <div class="pipeline-node" style="position: absolute; left: 9.5px; top: 32px; width: 10px; height: 10px; border-radius: 50%; background-color: #38BDF8; z-index: 2;"></div>
    <div class="pipeline-header" style="display: flex; align-items: center; justify-content: space-between; height: 20px; margin-bottom: 6px; gap: 0.5rem;">
      <span class="pipeline-label" style="font-size: 0.74rem; font-weight: 600; color: #94A3B8; letter-spacing: 0.05em; text-transform: uppercase; font-family: inherit;">
        HRMS API SYNC
      </span>
    </div>
    <div class="pipeline-title" style="font-size: 1.02rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.35rem; line-height: 1.35;">
      Automated HRMS Bi-Directional Sync
    </div>
    <p class="pipeline-desc" style="color: #94A3B8; font-size: 0.87rem; line-height: 1.52; margin: 0;">
      Continuously pulls compensation bands, tenure milestones, and exit sentiment directly from your HRIS, eliminating manual CSV uploads and stale spreadsheets.
    </p>
  </div>

  <!-- Step 2: DISPATCH ENGINE -->
  <div class="pipeline-step pipeline-step-2" style="position: relative; padding-left: 28px; padding-bottom: 32px; background: transparent; border: none; border-radius: 0;">
    <div class="pipeline-line" style="position: absolute; left: 14px; top: 0; bottom: -1px; width: 1px; background-color: rgba(56, 189, 248, 0.20);"></div>
    <div class="pipeline-node" style="position: absolute; left: 9.5px; top: 32px; width: 10px; height: 10px; border-radius: 50%; background-color: #38BDF8; z-index: 2;"></div>
    <div class="pipeline-header" style="display: flex; align-items: center; justify-content: space-between; height: 20px; margin-bottom: 6px; gap: 0.5rem;">
      <span class="pipeline-label" style="font-size: 0.74rem; font-weight: 600; color: #94A3B8; letter-spacing: 0.05em; text-transform: uppercase; font-family: inherit;">
        DISPATCH ENGINE
      </span>
    </div>
    <div class="pipeline-title" style="font-size: 1.02rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.35rem; line-height: 1.35;">
      Autonomous Micro-Pulse Dispatch
    </div>
    <p class="pipeline-desc" style="color: #94A3B8; font-size: 0.87rem; line-height: 1.52; margin: 0;">
      Triggers targeted, two-question pulses via Slack, Teams, or email the moment flight velocity spikes in an at-risk cohort.
    </p>
  </div>

  <!-- Step 3: POLICY RAG ENGINE -->
  <div class="pipeline-step pipeline-step-3" style="position: relative; padding-left: 28px; padding-bottom: 32px; background: transparent; border: none; border-radius: 0;">
    <div class="pipeline-line" style="position: absolute; left: 14px; top: 0; bottom: -1px; width: 1px; background-color: rgba(56, 189, 248, 0.20);"></div>
    <div class="pipeline-node" style="position: absolute; left: 9.5px; top: 32px; width: 10px; height: 10px; border-radius: 50%; background-color: #38BDF8; z-index: 2;"></div>
    <div class="pipeline-header" style="display: flex; align-items: center; justify-content: space-between; height: 20px; margin-bottom: 6px; gap: 0.5rem;">
      <span class="pipeline-label" style="font-size: 0.74rem; font-weight: 600; color: #94A3B8; letter-spacing: 0.05em; text-transform: uppercase; font-family: inherit;">
        POLICY RAG ENGINE
      </span>
    </div>
    <div class="pipeline-title" style="font-size: 1.02rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.35rem; line-height: 1.35;">
      Policy-Grounded Action Playbooks
    </div>
    <p class="pipeline-desc" style="color: #94A3B8; font-size: 0.87rem; line-height: 1.52; margin: 0;">
      Grounds recommendations in your company handbooks and SHRM standards via RAG, generating compliant, hallucination-free retention roadmaps.
    </p>
  </div>

  <!-- Step 4: PRIVACY & TRUST -->
  <div class="pipeline-step pipeline-step-4" style="position: relative; padding-left: 28px; padding-bottom: 0; background: transparent; border: none; border-radius: 0;">
    <div class="pipeline-line" style="position: absolute; left: 14px; top: 0; height: 37px; width: 1px; background-color: rgba(56, 189, 248, 0.20);"></div>
    <div class="pipeline-node pipeline-node-end" style="position: absolute; left: 9.5px; top: 32px; width: 10px; height: 10px; border-radius: 50%; background-color: #34D399; z-index: 2;"></div>
    <div class="pipeline-header" style="display: flex; align-items: center; justify-content: space-between; height: 20px; margin-bottom: 6px; gap: 0.5rem;">
      <span class="pipeline-label" style="font-size: 0.74rem; font-weight: 600; color: #94A3B8; letter-spacing: 0.05em; text-transform: uppercase; font-family: inherit;">
        PRIVACY &amp; TRUST
      </span>
    </div>
    <div class="pipeline-title" style="font-size: 1.02rem; font-weight: 700; color: #F8FAFC; margin-bottom: 0.35rem; line-height: 1.35;">
      The 5-Person Anti-Retaliation Shield
    </div>
    <p class="pipeline-desc" style="color: #94A3B8; font-size: 0.87rem; line-height: 1.52; margin: 0;">
      Never scores or reports on individuals; all outputs are aggregated at cohort level with a minimum of 5 responses. Individual-level text (exit notes, retros) is processed only to extract thematic clusters and is not accessible to managers.
    </p>
  </div>
</div>

</div>"""
    st.markdown(contact_left_html, unsafe_allow_html=True)

with cont_right:
    st.markdown("""<div class="pilot-right-col">
<h2 style="font-size: 2.1rem; font-weight: 700; color: #FFFFFF; line-height: 1.22; letter-spacing: -0.01em; margin-bottom: 0.65rem; font-family: var(--font-display);">
Request Stakeholder Demo
</h2>
<p style="color: #94A3B8; font-size: 0.94rem; line-height: 1.6; margin-bottom: 1.4rem;">
Get a tailored briefing on your organization's attrition risk profile and discuss pilot deployment.
</p>
</div>""", unsafe_allow_html=True)

    with st.form("homepage_demo_form"):
        name = st.text_input("Full Name", placeholder="Sarah Jenkins")
        email = st.text_input("Work Email", placeholder="s.jenkins@enterprise.com")
        role = st.selectbox("Organizational Focus", [
            "Human Resources / People Operations",
            "Executive Leadership (C-Suite / VP)",
            "Department Head / Engineering Director",
            "Academic Evaluator / Researcher"
        ])
        notes = st.text_area("Workforce Scale & Inquiries", placeholder="Tell us about your team size, recent attrition trends, or integration questions...")
        submit = st.form_submit_button("Request Enterprise Access", type="primary")

        if submit:
            st.toast("Inquiry registered! A RetAIn talent specialist will contact you shortly.", icon="✅")
