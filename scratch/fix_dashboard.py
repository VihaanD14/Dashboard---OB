with open('Dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace lines 2196 to 2208
target = """    ReactDOM.createRoot(document.getElementById('transition-root')).render(React.createElement(TransitionComponent));
  </script>
</body>
</html>
\\\"\\\"\\\"

components.html(scroll_transition_html, height=780, scrolling=False)
  </script>
</body>
</html>
\"\"\"

components.html(scroll_transition_html, height=590, scrolling=False)"""

replacement = """    ReactDOM.createRoot(document.getElementById('transition-root')).render(React.createElement(TransitionComponent));
  </script>
</body>
</html>
\"\"\"

components.html(scroll_transition_html, height=780, scrolling=False)"""

content = content.replace(target, replacement)

with open('Dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced tail successfully!")
