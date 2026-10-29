import os

with open('Dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read().replace('\r\n', '\n')

old_cards_code = """          // 4 Proactive, Continuous & High-ROI Bento Capability Cards (2x2 Grid)
          React.createElement('div', {
            className: 'w-full max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-4 my-2'
          },
            // Bento Card 1: Continuous NLP Mining
            React.createElement('div', {
              className: 'bento-card-interactive flex flex-row items-center justify-between p-5 md:p-6 w-full'
            },
              React.createElement('div', {
                className: 'flex flex-col justify-center h-full',
                style: { width: '56%', flexShrink: 0 }
              },
                React.createElement('h4', { className: 'text-lg md:text-xl font-bold text-white mb-1.5 tracking-tight' }, 'Continuous NLP Mining'),
                React.createElement('p', {
                  className: 'text-xs md:text-sm font-normal leading-relaxed',
                  style: { color: '#E2E8F0', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }
                }, 'Converts raw qualitative feedback into trend signals')
              ),
              React.createElement('div', {
                className: 'flex items-center justify-center flex-shrink-0',
                style: { width: '40%', height: '140px', boxSizing: 'border-box' }
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
                        fontFamily: "'JetBrains Mono', monospace",
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
                className: 'flex flex-col justify-center h-full',
                style: { width: '56%', flexShrink: 0 }
              },
                React.createElement('h4', { className: 'text-lg md:text-xl font-bold text-white mb-1.5 tracking-tight' }, 'Privacy-First Cohort Radar'),
                React.createElement('p', {
                  className: 'text-xs md:text-sm font-normal leading-relaxed',
                  style: { color: '#E2E8F0', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }
                }, 'Team-level early flight risk detection')
              ),
              React.createElement('div', {
                className: 'flex items-center justify-center flex-shrink-0',
                style: { width: '40%', height: '140px', boxSizing: 'border-box' }
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
                className: 'flex flex-col justify-center h-full',
                style: { width: '56%', flexShrink: 0 }
              },
                React.createElement('h4', { className: 'text-lg md:text-xl font-bold text-white mb-1.5 tracking-tight' }, 'Pre-Emptive Micro-Pulses'),
                React.createElement('p', {
                  className: 'text-xs md:text-sm font-normal leading-relaxed',
                  style: { color: '#E2E8F0', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }
                }, 'Non leading 2 question checks')
              ),
              React.createElement('div', {
                className: 'flex items-center justify-center flex-shrink-0',
                style: { width: '40%', height: '140px', boxSizing: 'border-box' }
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
                className: 'flex flex-col justify-center h-full',
                style: { width: '56%', flexShrink: 0 }
              },
                React.createElement('h4', { className: 'text-lg md:text-xl font-bold text-white mb-1.5 tracking-tight' }, 'Modeled Action Playbooks'),
                React.createElement('p', {
                  className: 'text-xs md:text-sm font-normal leading-relaxed',
                  style: { color: '#E2E8F0', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }
                }, 'Targeted, policy-aligned interventions mapped to guidelines.')
              ),
              React.createElement('div', {
                className: 'flex items-center justify-center flex-shrink-0',
                style: { width: '40%', height: '140px', boxSizing: 'border-box' }
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
          )"""

new_cards_code = """          // 4 Proactive, Continuous & High-ROI Bento Capability Cards (2x2 Grid)
          React.createElement('div', {
            className: 'w-full max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-4 my-2'
          },
            // Bento Card 1: Continuous NLP Mining
            React.createElement('div', {
              className: 'bento-card-interactive flex flex-row items-center justify-between p-5 md:p-6 w-full'
            },
              React.createElement('div', {
                className: 'flex flex-col justify-start h-full pt-4',
                style: { width: '62%', flexShrink: 0, paddingRight: '10px' }
              },
                React.createElement('h4', { className: 'text-lg md:text-[1.14rem] font-bold text-white mb-2 tracking-tight whitespace-nowrap' }, 'Continuous NLP Mining'),
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
                        fontFamily: "'JetBrains Mono', monospace",
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
                React.createElement('h4', { className: 'text-lg md:text-[1.14rem] font-bold text-white mb-2 tracking-tight whitespace-nowrap' }, 'Privacy-First Cohort Radar'),
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
                React.createElement('h4', { className: 'text-lg md:text-[1.14rem] font-bold text-white mb-2 tracking-tight whitespace-nowrap' }, 'Pre-Emptive Micro-Pulses'),
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
                React.createElement('h4', { className: 'text-lg md:text-[1.14rem] font-bold text-white mb-2 tracking-tight whitespace-nowrap' }, 'Modeled Action Playbooks'),
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
          )"""

assert old_cards_code in content, "old_cards_code not found in Dashboard.py"
content = content.replace(old_cards_code, new_cards_code)

with open('Dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Dashboard.py and app.py successfully with perfect Bento alignment")
