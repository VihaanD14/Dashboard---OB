import streamlit as st
import streamlit.components.v1 as components

def render_top_navbar(active_page="overview"):
    """
    Renders a naked, horizontal top navbar matching the NEONE aesthetic.
    On the public landing page (Overview), displays public SaaS navigation with
    high-velocity kinetic smooth scrolling for anchor links.
    Inside the enterprise portal, displays the analytical modules.
    """
    is_portal = active_page in ["dashboard", "exit", "survey", "risk", "recommendations", "tracker", "settings"]

    if not is_portal:
        # Public SaaS Homepage Navigation (Refined Floating Glass Pill)
        home_active = 'active' if active_page == 'overview' else ''
        why_active = 'active' if active_page == 'why-us' else ''
        contact_active = 'active' if active_page == 'contact' else ''
        dash_active = 'active' if active_page == 'dashboard' else ''

        nav_html = f"""<div class="naked-nav-container">
<div class="naked-nav-inner">
<!-- Far Left: Logo -->
<div class="naked-nav-brand">
<a href="/" target="_self" id="nav-brand-link" class="naked-brand-link">
<svg class="brand-logo-icon" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M16 52V12H36C43.732 12 50 18.268 50 26C50 33.732 43.732 40 36 40H16" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 40L50 52" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/><path d="M36 12L45 6M36 40L45 46M16 12L10 6M16 52L10 58" stroke="currentColor" stroke-width="3.5" stroke-linecap="round"/></svg>
<span class="brand">Ret<span class="brand-ai">AI</span>n</span>
</a>
</div>
<!-- Center: Floating Glass Pill with Sliding Active Highlight -->
<div class="naked-nav-links">
<div class="nav-sliding-indicator" id="nav-sliding-indicator"></div>
<a href="/" target="_self" id="nav-home-link" class="naked-nav-link {home_active}">Home</a>
<a href="/#why-retain" target="_self" id="nav-why-link" class="naked-nav-link {why_active}">Why&nbsp;<span class="brand">Ret<span class="brand-ai">AI</span>n</span></a>
<a href="/#contact" target="_self" id="nav-contact-link" class="naked-nav-link {contact_active}">Contact us</a>
<a href="/Enterprise_Dashboard" target="_self" class="naked-nav-link {dash_active}">
<span class="nav-live-dot"></span>Dashboard
</a>
</div>
<!-- Far Right: Plain Sign in + Solid Book a demo button -->
<div class="naked-nav-cta">
<a href="/Enterprise_Dashboard" target="_self" class="naked-signin-text">Sign in</a>
<a href="/#contact" target="_self" id="nav-book-demo-btn" class="naked-book-demo-btn">Book a demo</a>
</div>
</div>
</div>"""

        st.markdown(nav_html, unsafe_allow_html=True)

        # High-Velocity Kinetic Smooth Scroll Controller & Sliding Tab / Scroll Watcher
        scroll_script = """
        <script>
        (function() {
            function initNavbarControllers() {
                try {
                    const parentDoc = window.parent.document;
                    const parentWin = window.parent;
                    if (!parentDoc || !parentWin) return;

                    function getScroller() {
                        return parentDoc.querySelector('section.stMain') || 
                               parentDoc.querySelector('[data-testid="stMain"]') || 
                               parentDoc.querySelector('[data-testid="stAppViewContainer"]') || 
                               parentWin;
                    }

                    function fastGlideTo(targetEl, duration = 380, offset = 85) {
                        const scroller = getScroller();
                        if (targetEl) {
                            try {
                                targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
                            } catch (e) {}
                        }
                        const isWin = scroller === parentWin;
                        const currentY = isWin ? (parentWin.scrollY || parentWin.pageYOffset || 0) : scroller.scrollTop;
                        
                        let targetY = 0;
                        if (targetEl) {
                            const rect = targetEl.getBoundingClientRect();
                            targetY = Math.max(0, currentY + rect.top - offset);
                        }
                        
                        const distance = targetY - currentY;
                        if (Math.abs(distance) < 5) return;
                        
                        const startTime = performance.now();

                        function easeOutQuart(t) {
                            return 1 - (--t) * t * t * t;
                        }

                        function step(now) {
                            const elapsed = now - startTime;
                            const progress = Math.min(elapsed / duration, 1);
                            const ease = easeOutQuart(progress);
                            const nextY = currentY + distance * ease;

                            if (isWin) {
                                parentWin.scrollTo(0, nextY);
                            } else {
                                scroller.scrollTop = nextY;
                            }

                            if (progress < 1) {
                                parentWin.requestAnimationFrame(step);
                            }
                        }
                        parentWin.requestAnimationFrame(step);
                    }

                    // --- Scroll Watcher (> 24px) for Sticky Pill State ---
                    function setupScrollWatcher() {
                        const nav = parentDoc.querySelector('.naked-nav-container');
                        if (!nav) return;

                        function onScroll() {
                            const scroller = getScroller();
                            const isWin = scroller === parentWin;
                            const mainEl = parentDoc.querySelector('section.stMain');
                            const currentY = isWin 
                                ? (parentWin.scrollY || parentWin.pageYOffset || 0) 
                                : Math.max(scroller.scrollTop || 0, mainEl ? mainEl.scrollTop : 0);
                            if (currentY > 24) {
                                nav.classList.add('nav-scrolled');
                            } else {
                                nav.classList.remove('nav-scrolled');
                            }
                        }

                        parentWin.removeEventListener('scroll', onScroll, true);
                        parentWin.addEventListener('scroll', onScroll, { capture: true, passive: true });
                        const scroller = getScroller();
                        if (scroller && scroller !== parentWin) {
                            scroller.removeEventListener('scroll', onScroll, true);
                            scroller.addEventListener('scroll', onScroll, { capture: true, passive: true });
                        }
                        onScroll();
                    }
                    setupScrollWatcher();

                    // --- Smooth Sliding Highlight for Navbar Links ---
                    function setupSlidingHighlight() {
                        const pill = parentDoc.querySelector('.naked-nav-links');
                        const indicator = parentDoc.querySelector('#nav-sliding-indicator');
                        if (!pill || !indicator) return;

                        const links = Array.from(pill.querySelectorAll('.naked-nav-link'));
                        if (!links.length) return;

                        function getActiveLink() {
                            return pill.querySelector('.naked-nav-link.active') || links[0];
                        }

                        function positionIndicator(target) {
                            if (!target) return;
                            const pillRect = pill.getBoundingClientRect();
                            const targetRect = target.getBoundingClientRect();

                            const left = targetRect.left - pillRect.left;
                            const top = targetRect.top - pillRect.top;
                            const width = targetRect.width;
                            const height = targetRect.height;

                            indicator.style.width = width + 'px';
                            indicator.style.height = height + 'px';
                            indicator.style.transform = `translate3d(${left}px, ${top}px, 0)`;
                            indicator.style.opacity = '1';
                        }

                        // Position initially
                        positionIndicator(getActiveLink());

                        // Bind hover & click events
                        links.forEach(link => {
                            if (link.dataset.slideBound) return;
                            link.dataset.slideBound = "true";

                            link.addEventListener('mouseenter', () => {
                                positionIndicator(link);
                            });

                            link.addEventListener('click', () => {
                                links.forEach(l => l.classList.remove('active'));
                                link.classList.add('active');
                                positionIndicator(link);
                            });
                        });

                        if (!pill.dataset.slideBound) {
                            pill.dataset.slideBound = "true";
                            pill.addEventListener('mouseleave', () => {
                                positionIndicator(getActiveLink());
                            });
                        }

                        parentWin.addEventListener('resize', () => {
                            positionIndicator(getActiveLink());
                        });
                    }
                    setupSlidingHighlight();
                    setTimeout(setupSlidingHighlight, 100);
                    setTimeout(setupSlidingHighlight, 350);

                    // Attach fast smooth scroll to "Why RetAIn"
                    const whyLink = parentDoc.querySelector('#nav-why-link') || 
                                    parentDoc.querySelector('a[href="/#why-retain"]') || 
                                    parentDoc.querySelector('a[href="#why-retain"]');
                    if (whyLink && !whyLink.dataset.fastScrollBound) {
                        whyLink.dataset.fastScrollBound = "true";
                        whyLink.addEventListener('click', function(e) {
                            const target = parentDoc.getElementById('why-retain') || parentDoc.getElementById('why-us');
                            if (target) {
                                e.preventDefault();
                                fastGlideTo(target, 380, 85);
                                if (parentWin.history && parentWin.history.pushState) {
                                    parentWin.history.pushState(null, null, '#why-retain');
                                }
                            } else {
                                parentWin.location.href = '/#why-retain';
                            }
                        });
                    }

                    // Attach fast smooth scroll to "Contact us"
                    const contactLink = parentDoc.querySelector('#nav-contact-link') || 
                                        parentDoc.querySelector('a[href="/#contact"]') || 
                                        parentDoc.querySelector('a[href="#contact"]');
                    if (contactLink && !contactLink.dataset.fastScrollBound) {
                        contactLink.dataset.fastScrollBound = "true";
                        contactLink.addEventListener('click', function(e) {
                            const target = parentDoc.getElementById('contact');
                            if (target) {
                                e.preventDefault();
                                fastGlideTo(target, 380, 85);
                                if (parentWin.history && parentWin.history.pushState) {
                                    parentWin.history.pushState(null, null, '#contact');
                                }
                            } else {
                                parentWin.location.href = '/#contact';
                            }
                        });
                    }

                    // Attach fast smooth scroll to "Book a demo" button
                    const demoBtn = parentDoc.querySelector('#nav-book-demo-btn');
                    if (demoBtn && !demoBtn.dataset.fastScrollBound) {
                        demoBtn.dataset.fastScrollBound = "true";
                        demoBtn.addEventListener('click', function(e) {
                            const target = parentDoc.getElementById('contact');
                            if (target) {
                                e.preventDefault();
                                fastGlideTo(target, 380, 85);
                                if (parentWin.history && parentWin.history.pushState) {
                                    parentWin.history.pushState(null, null, '#contact');
                                }
                            } else {
                                parentWin.location.href = '/#contact';
                            }
                        });
                    }

                    // Attach to Home / Brand Logo (Scroll to Top)
                    const homeLinks = parentDoc.querySelectorAll('#nav-home-link, #nav-brand-link');
                    homeLinks.forEach(link => {
                        if (link && !link.dataset.fastScrollBound) {
                            link.dataset.fastScrollBound = "true";
                            link.addEventListener('click', function(e) {
                                const path = parentWin.location.pathname;
                                if (path === '/' || path === '') {
                                    e.preventDefault();
                                    fastGlideTo(null, 320, 0);
                                    if (parentWin.history && parentWin.history.pushState) {
                                        parentWin.history.pushState(null, null, ' ');
                                    }
                                }
                            });
                        }
                    });

                    // Auto-glide on page load if hash exists
                    function checkAndGlideHash() {
                        const hash = parentWin.location.hash;
                        if (hash === '#why-retain' || hash === '#why-us') {
                            const target = parentDoc.getElementById('why-retain') || parentDoc.getElementById('why-us');
                            if (target) fastGlideTo(target, 380, 85);
                        } else if (hash === '#contact') {
                            const target = parentDoc.getElementById('contact');
                            if (target) fastGlideTo(target, 380, 85);
                        }
                    }
                    setTimeout(checkAndGlideHash, 180);
                    setTimeout(checkAndGlideHash, 480);
                    parentWin.addEventListener('hashchange', checkAndGlideHash);
                } catch (err) {
                    // Silently fall back to standard browser navigation
                }
            }

            // Execute on load and after dynamic Streamlit renders
            initNavbarControllers();
            setTimeout(initNavbarControllers, 200);
            setTimeout(initNavbarControllers, 600);
            setTimeout(initNavbarControllers, 1200);
        })();
        </script>
        """
        components.html(scroll_script, height=0)

    else:
        # Enterprise Client Portal Navigation
        portal_pages = [
            {"id": "home", "label": "← Home", "url": "/"},
            {"id": "dashboard", "label": "Overview", "url": "/Enterprise_Dashboard"},
            {"id": "exit", "label": "Exit Analyzer", "url": "/Exit_Analyzer"},
            {"id": "survey", "label": "Survey Engine", "url": "/Survey_Engine"},
            {"id": "risk", "label": "Risk Matrix", "url": "/Risk_Scoring"},
            {"id": "recommendations", "label": "Recommendations", "url": "/Recommendations"},
            {"id": "tracker", "label": "Tracker", "url": "/Intervention_Tracker"},
            {"id": "settings", "label": "Settings", "url": "/Settings"}
        ]

        links_html = ""
        for p in portal_pages:
            is_active = "active" if p["id"] == active_page else ""
            links_html += f'<a href="{p["url"]}" target="_self" class="naked-nav-link {is_active}">{p["label"]}</a>'

        nav_html = f"""<div class="naked-nav-container">
<div class="naked-nav-inner">
<div class="naked-nav-brand">
<a href="/Enterprise_Dashboard" target="_self" class="brand-title">
<svg class="brand-logo-icon" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M16 52V12H36C43.732 12 50 18.268 50 26C50 33.732 43.732 40 36 40H16" stroke="currentColor" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 40L50 52" stroke="currentColor" stroke-width="4.5" stroke-linecap="round"/><path d="M36 12L45 6M36 40L45 46M16 12L10 6M16 52L10 58" stroke="currentColor" stroke-width="3.5" stroke-linecap="round"/></svg>
<span class="brand">Ret<span class="brand-ai">AI</span>n</span>
</a>
</div>
<nav class="naked-nav-links">
{links_html}
</nav>
<div class="naked-nav-cta"></div>
</div>
</div>"""

        st.markdown(nav_html, unsafe_allow_html=True)

    # Instantaneous Tab Switching Visual Feedback & Kinetic Top Loader
    feedback_script = """
    <script>
    (function() {
        function setupNavFeedback() {
            try {
                const parentDoc = window.parent.document;
                if (!parentDoc) return;

                // Ensure global top loading bar exists in parent DOM
                let bar = parentDoc.getElementById('nav-loading-bar');
                if (!bar) {
                    bar = parentDoc.createElement('div');
                    bar.id = 'nav-loading-bar';
                    parentDoc.body.appendChild(bar);
                } else {
                    // Reset on fresh page load
                    bar.style.transition = 'none';
                    bar.style.opacity = '0';
                    bar.style.width = '0%';
                }

                // Bind click to nav links and sign-in pills
                const links = parentDoc.querySelectorAll('.naked-nav-link, .naked-signin-pill, .brand-title, .naked-brand-link');
                links.forEach(function(l) {
                    if (l.dataset.fastNavBound) return;
                    l.dataset.fastNavBound = "true";

                    l.addEventListener('click', function(e) {
                        const href = l.getAttribute('href');
                        if (!href) return;

                        // Don't trigger route loading bar for on-page hash anchors
                        const isAnchorOnHome = (href.startsWith('#') || href.startsWith('/#')) && 
                            (window.parent.location.pathname === '/' || window.parent.location.pathname === '');
                        if (isAnchorOnHome) return;

                        // Trigger top progress scanline
                        if (bar) {
                            bar.style.transition = 'none';
                            bar.style.width = '15%';
                            bar.style.opacity = '1';
                            void bar.offsetWidth; // force browser layout recalculation
                            bar.style.transition = 'width 1.2s cubic-bezier(0.1, 0.7, 0.1, 1)';
                            bar.style.width = '88%';
                        }

                        // Immediate visual feedback on clicked tab
                        const navContainer = l.closest('.naked-nav-links') || l.parentElement;
                        if (navContainer) {
                            navContainer.querySelectorAll('.naked-nav-link').forEach(function(item) {
                                item.classList.remove('active');
                            });
                        }
                        l.classList.add('nav-active-pending');
                    });
                });
            } catch(err) {}
        }

        setupNavFeedback();
        setTimeout(setupNavFeedback, 150);
        setTimeout(setupNavFeedback, 500);
    })();
    </script>
    """
    components.html(feedback_script, height=0)
