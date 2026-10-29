import os

with open('Dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read().replace('\r\n', '\n')

old_bento = """          // 4 Separately Placed Bento Capability Cards (2x2 Grid)
          React.createElement('div', {
            className: 'w-full max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-4 my-2'
          },
            // Bento Card 1: Continuous NLP Mining
            React.createElement('div', {
              className: 'bento-card-interactive p-5 md:p-6 flex flex-col justify-between'
            },
              React.createElement('div', null,
                React.createElement('div', { className: 'flex items-center gap-2 text-[11px] font-mono tracking-wider text-slate-400 uppercase mb-2.5' },
                  React.createElement('span', { className: 'text-sky-400 font-semibold' }, '01'),
                  React.createElement('span', { className: 'text-slate-600' }, '/'),
                  React.createElement('span', null, 'Qualitative Mining')
                ),
                React.createElement('h4', { className: 'text-lg md:text-xl font-bold text-white mb-1.5 tracking-tight' }, 'Continuous NLP Mining'),
                React.createElement('p', { className: 'text-sm text-slate-300 leading-relaxed font-light' },
                  'Converts raw qualitative feedback into trend signals'
                )
              ),
              React.createElement('div', {
                className: 'pt-3.5 mt-4 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono tracking-tight'
              },
                React.createElement('div', { className: 'flex items-center gap-2' },
                  React.createElement('span', { className: 'w-1.5 h-1.5 rounded-full bg-sky-400 shadow-[0_0_6px_#38bdf8]' }),
                  React.createElement('span', { className: 'text-sky-300 font-medium' }, 'Signal Velocity')
                ),
                React.createElement('span', { className: 'text-slate-400' }, 'Real-time NLP Stream')
              )
            ),

            // Bento Card 2: Privacy-First Cohort Radar
            React.createElement('div', {
              className: 'bento-card-interactive p-5 md:p-6 flex flex-col justify-between'
            },
              React.createElement('div', null,
                React.createElement('div', { className: 'flex items-center gap-2 text-[11px] font-mono tracking-wider text-slate-400 uppercase mb-2.5' },
                  React.createElement('span', { className: 'text-sky-400 font-semibold' }, '02'),
                  React.createElement('span', { className: 'text-slate-600' }, '/'),
                  React.createElement('span', null, 'Cohort Risk Engine')
                ),
                React.createElement('h4', { className: 'text-lg md:text-xl font-bold text-white mb-1.5 tracking-tight' }, 'Privacy-First Cohort Radar'),
                React.createElement('p', { className: 'text-sm text-slate-300 leading-relaxed font-light' },
                  'Team-level early flight risk detection'
                )
              ),
              React.createElement('div', {
                className: 'pt-3.5 mt-4 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono tracking-tight'
              },
                React.createElement('div', { className: 'flex items-center gap-2' },
                  React.createElement('span', { className: 'w-1.5 h-1.5 rounded-full bg-emerald-400 shadow-[0_0_6px_#34d399]' }),
                  React.createElement('span', { className: 'text-emerald-300 font-medium' }, '5+ Staff Guard')
                ),
                React.createElement('span', { className: 'text-slate-400' }, 'Zero Individual PII Tracking')
              )
            ),

            // Bento Card 3: Pre-Emptive Micro-Pulses
            React.createElement('div', {
              className: 'bento-card-interactive p-5 md:p-6 flex flex-col justify-between'
            },
              React.createElement('div', null,
                React.createElement('div', { className: 'flex items-center gap-2 text-[11px] font-mono tracking-wider text-slate-400 uppercase mb-2.5' },
                  React.createElement('span', { className: 'text-sky-400 font-semibold' }, '03'),
                  React.createElement('span', { className: 'text-slate-600' }, '/'),
                  React.createElement('span', null, 'Pulse Velocity')
                ),
                React.createElement('h4', { className: 'text-lg md:text-xl font-bold text-white mb-1.5 tracking-tight' }, 'Pre-Emptive Micro-Pulses'),
                React.createElement('p', { className: 'text-sm text-slate-300 leading-relaxed font-light' },
                  'Non leading 2 question checks'
                )
              ),
              React.createElement('div', {
                className: 'pt-3.5 mt-4 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono tracking-tight'
              },
                React.createElement('div', { className: 'flex items-center gap-2' },
                  React.createElement('span', { className: 'w-1.5 h-1.5 rounded-full bg-sky-400 shadow-[0_0_6px_#38bdf8]' }),
                  React.createElement('span', { className: 'text-sky-300 font-medium' }, '< 45 Seconds')
                ),
                React.createElement('span', { className: 'text-slate-400' }, '94% Minimal Friction')
              )
            ),

            // Bento Card 4: Modeled Action Playbooks
            React.createElement('div', {
              className: 'bento-card-interactive p-5 md:p-6 flex flex-col justify-between'
            },
              React.createElement('div', null,
                React.createElement('div', { className: 'flex items-center gap-2 text-[11px] font-mono tracking-wider text-slate-400 uppercase mb-2.5' },
                  React.createElement('span', { className: 'text-sky-400 font-semibold' }, '04'),
                  React.createElement('span', { className: 'text-slate-600' }, '/'),
                  React.createElement('span', null, 'Retention Engine')
                ),
                React.createElement('h4', { className: 'text-lg md:text-xl font-bold text-white mb-1.5 tracking-tight' }, 'Modeled Action Playbooks'),
                React.createElement('p', { className: 'text-sm text-slate-300 leading-relaxed font-light' },
                  'Targeted, policy-aligned interventions mapped to company guidelines.'
                )
              ),
              React.createElement('div', {
                className: 'pt-3.5 mt-4 border-t border-white/[0.06] flex items-center justify-between text-[11px] font-mono tracking-tight'
              },
                React.createElement('div', { className: 'flex items-center gap-2' },
                  React.createElement('span', { className: 'w-1.5 h-1.5 rounded-full bg-emerald-400 shadow-[0_0_6px_#34d399]' }),
                  React.createElement('span', { className: 'text-emerald-300 font-medium' }, 'SHRM Aligned')
                ),
                React.createElement('span', { className: 'text-slate-400' }, 'Policy-Mapped Interventions')
              )
            )
          )"""

new_bento = """          // 4 Clean Human-Crafted Bento Capability Cards (2x2 Grid)
          React.createElement('div', {
            className: 'w-full max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-4 my-2'
          },
            // Bento Card 1: Continuous NLP Mining
            React.createElement('div', {
              className: 'bento-card-interactive p-6 md:p-8 flex flex-col justify-center'
            },
              React.createElement('h4', { className: 'text-xl md:text-2xl font-bold text-white mb-2.5 tracking-tight' }, 'Continuous NLP Mining'),
              React.createElement('p', { className: 'text-sm md:text-base text-slate-300 leading-relaxed font-normal' },
                'Converts raw qualitative feedback into trend signals'
              )
            ),

            // Bento Card 2: Privacy-First Cohort Radar
            React.createElement('div', {
              className: 'bento-card-interactive p-6 md:p-8 flex flex-col justify-center'
            },
              React.createElement('h4', { className: 'text-xl md:text-2xl font-bold text-white mb-2.5 tracking-tight' }, 'Privacy-First Cohort Radar'),
              React.createElement('p', { className: 'text-sm md:text-base text-slate-300 leading-relaxed font-normal' },
                'Team-level early flight risk detection'
              )
            ),

            // Bento Card 3: Pre-Emptive Micro-Pulses
            React.createElement('div', {
              className: 'bento-card-interactive p-6 md:p-8 flex flex-col justify-center'
            },
              React.createElement('h4', { className: 'text-xl md:text-2xl font-bold text-white mb-2.5 tracking-tight' }, 'Pre-Emptive Micro-Pulses'),
              React.createElement('p', { className: 'text-sm md:text-base text-slate-300 leading-relaxed font-normal' },
                'Non leading 2 question checks'
              )
            ),

            // Bento Card 4: Modeled Action Playbooks
            React.createElement('div', {
              className: 'bento-card-interactive p-6 md:p-8 flex flex-col justify-center'
            },
              React.createElement('h4', { className: 'text-xl md:text-2xl font-bold text-white mb-2.5 tracking-tight' }, 'Modeled Action Playbooks'),
              React.createElement('p', { className: 'text-sm md:text-base text-slate-300 leading-relaxed font-normal' },
                'Targeted, policy-aligned interventions mapped to company guidelines.'
              )
            )
          )"""

old_gateway_card = """<!-- Interactive Demonstration Gateway Card -->
<div class="pilot-gateway-card">
  <div style="font-size: 0.92rem; color: #E2E8F0; line-height: 1.5; margin-bottom: 0.85rem; font-weight: 500;">
    Evaluate our active demonstration environment with pre-loaded enterprise scenarios:
  </div>
  <a href="/Enterprise_Dashboard" target="_self" class="neone-pill-btn" style="display: inline-flex; align-items: center; gap: 0.5rem; text-decoration: none;">
    Launch Enterprise Portal &rarr;
  </a>
</div>
</div>"""

new_gateway_card = """</div>"""

assert old_bento in content, "old_bento not found in Dashboard.py"
assert old_gateway_card in content, "old_gateway_card not found in Dashboard.py"

content = content.replace(old_bento, new_bento).replace(old_gateway_card, new_gateway_card)

with open('Dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Dashboard.py and app.py successfully")
