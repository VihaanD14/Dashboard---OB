import os

keywords = ['mobley', 'vroom', 'differential privacy', '0.75x', '0.75', 'cost-of-turnover', 'cost of turnover', 'reaching full penalty', '60-90 days', 'privacy and anti-differencing', 'section 4']
for root, dirs, files in os.walk('.'):
    if any(p in root for p in ['.git', '__pycache__', '.playwright-mcp', '.streamlit']):
        continue
    for file in files:
        if file.endswith(('.py', '.html', '.md', '.json', '.txt', '.csv')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    for idx, line in enumerate(lines):
                        for kw in keywords:
                            if kw in line.lower():
                                print(f"{path}:{idx+1} [{kw}]: {line.strip()[:100]}")
            except Exception as e:
                pass
