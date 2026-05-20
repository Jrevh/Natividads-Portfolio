from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = 'Integer eu ante ornare amet commetus vestibulum blandit integer in curae ac faucibus integer non. Adipiscing cubilia elementum integer. Integer eu ante ornare amet commetus.'
new = 'Selected academic and applied IT projects covering systems design, project management, and cybersecurity audit — with downloadable PDF reports available for each major deliverable.'
print('count before:', text.count(old))
text = text.replace(old, new)
print('count after:', text.count(old))
path.write_text(text, encoding='utf-8')
print('replaced paragraph')
