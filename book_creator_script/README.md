# PDF Book from Markdown
Converts a bunch of markdown files made for a programming book into a pdf.
Uses prism syntax highlighting and a modified version of github stylesheet.

### Requirements:
You need to install:
- https://wkhtmltopdf.org/
- https://pandoc.org/installing.html
- LaTeX (See https://tug.org/mactex/ on OS X, https://miktex.org/ on Windows, or install the texlive package on Linux.
- Python

### How to use
1. Install pdfkit `pip install pdfkit`
2. Place all your files in the root directory
3. Edit the metadata.yaml file
4. Make sure they are alphabetically sorted (0-9, then A - z)
5. Run `python create_book.py`
6. Enjoy