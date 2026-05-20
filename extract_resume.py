from pathlib import Path
import sys

path = Path(r'c:\Users\FF\Downloads\New folder\Projects\Rresume.docx')
try:
    import docx
except Exception as e:
    print('IMPORT_ERROR', e)
    sys.exit(1)

doc = docx.Document(path)
for i, p in enumerate(doc.paragraphs, 1):
    text = p.text.strip()
    if text:
        print(f'{i}: {text}')
