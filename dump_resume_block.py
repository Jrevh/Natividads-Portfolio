from pathlib import Path
text = Path('index.html').read_text(encoding='utf-8')
start = text.find('<!-- Resume -->')
if start == -1:
    raise SystemExit('Resume marker not found')
end = text.find('<!-- Four -->', start)
print('START', start)
print('END', end)
print(repr(text[start-40:end+20]))
