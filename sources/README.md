# Source Documents

Original PDFs and their converted/annotated text versions.

## PDFs in Repo Root

| File | Description |
|------|-------------|
| `Riemann.pdf` | Full Riemann 1859 paper (German original + supplementary material, ~16MB) |
| `Riemann_zeta_function.pdf` | Reference overview of the zeta function (~1.7MB) |
| `Wilkins-translation.pdf` | D.R. Wilkins English translation of Riemann's 1859 paper (~120KB) |
| `riemann (1).pdf` | Additional Riemann paper (~160KB) |

## Converting PDFs to Text

### Option A: Python (pdfminer)
```powershell
pip install pdfminer.six
python -c "
from pdfminer.high_level import extract_text
text = extract_text('../Wilkins-translation.pdf')
with open('wilkins_translation.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print('Done')
"
```

### Option B: Python (pypdf)
```powershell
pip install pypdf
python -c "
from pypdf import PdfReader
reader = PdfReader('../Wilkins-translation.pdf')
text = '\n'.join(p.extract_text() for p in reader.pages)
with open('wilkins_translation.txt', 'w', encoding='utf-8') as f:
    f.write(text)
"
```

### Option C: Bulk convert all PDFs
```powershell
pip install pdfminer.six
python sources/convert_pdfs.py
```

See `convert_pdfs.py` in this folder.

## Converted Files (populated after conversion)

| File | Source PDF |
|------|-----------|
| `wilkins_translation.txt` | `Wilkins-translation.pdf` — Riemann 1859 (English) |
| `riemann_zeta_function_reference.txt` | `Riemann_zeta_function.pdf` |
| `riemann_original_notes.txt` | `riemann (1).pdf` |
| `riemann_full.txt` | `Riemann.pdf` (large) |
