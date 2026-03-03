"""
convert_pdfs.py
===============
Converts all PDFs in the repo root to text files in the sources/ directory.
Run from the repo root or from sources/:
    python sources/convert_pdfs.py
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = SCRIPT_DIR

PDF_MAP = {
    "Wilkins-translation.pdf": "wilkins_translation.txt",
    "Riemann_zeta_function.pdf": "riemann_zeta_function_reference.txt",
    "riemann (1).pdf": "riemann_original_notes.txt",
    "Riemann.pdf": "riemann_full.txt",
}


def convert_with_pdfminer(pdf_path, txt_path):
    from pdfminer.high_level import extract_text
    print(f"  [pdfminer] {os.path.basename(pdf_path)} -> {os.path.basename(txt_path)}")
    text = extract_text(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  Done. ({len(text):,} chars)")


def convert_with_pypdf(pdf_path, txt_path):
    from pypdf import PdfReader
    print(f"  [pypdf] {os.path.basename(pdf_path)} -> {os.path.basename(txt_path)}")
    reader = PdfReader(pdf_path)
    pages = []
    for i, page in enumerate(reader.pages):
        t = page.extract_text()
        if t:
            pages.append(f"--- Page {i+1} ---\n{t}")
    text = "\n\n".join(pages)
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  Done. ({len(text):,} chars, {len(reader.pages)} pages)")


def try_import_pdfminer():
    try:
        import pdfminer
        return True
    except ImportError:
        return False


def try_import_pypdf():
    try:
        import pypdf
        return True
    except ImportError:
        return False


def main():
    has_pdfminer = try_import_pdfminer()
    has_pypdf = try_import_pypdf()

    if not has_pdfminer and not has_pypdf:
        print("ERROR: No PDF library found. Install one:")
        print("  pip install pdfminer.six")
        print("  pip install pypdf")
        sys.exit(1)

    print(f"PDF library: {'pdfminer' if has_pdfminer else 'pypdf'}")
    print(f"Repo root:   {REPO_ROOT}")
    print(f"Output dir:  {OUTPUT_DIR}")
    print()

    for pdf_name, txt_name in PDF_MAP.items():
        pdf_path = os.path.join(REPO_ROOT, pdf_name)
        txt_path = os.path.join(OUTPUT_DIR, txt_name)

        if not os.path.exists(pdf_path):
            print(f"  SKIP: {pdf_name} not found")
            continue

        if os.path.exists(txt_path):
            print(f"  SKIP: {txt_name} already exists (delete to re-convert)")
            continue

        try:
            if has_pdfminer:
                convert_with_pdfminer(pdf_path, txt_path)
            else:
                convert_with_pypdf(pdf_path, txt_path)
        except Exception as e:
            print(f"  ERROR converting {pdf_name}: {e}")
            if has_pdfminer and has_pypdf:
                print("  Trying pypdf as fallback...")
                try:
                    convert_with_pypdf(pdf_path, txt_path)
                except Exception as e2:
                    print(f"  FAILED with pypdf too: {e2}")

    print("\nAll done.")


if __name__ == "__main__":
    main()
