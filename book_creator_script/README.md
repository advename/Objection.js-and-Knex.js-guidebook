# Guide

To create a pdf, epub or whatever out of the markdown files, copy and paste the `create_book.py`, `pandoc.css` and `pagebreak.lua` file in a directory with all the markdown files.

Then run `python create_book.py` which generates a book.pdf out of all markdown files.

#### Requirements

These tools need to be installed.

- Pandoc
- Python
- Latex
- wkhtmltopdf -> replaced with python venv and `pip install pdfkit` which is a python library to use wkhtmltopf. Whats missing now is to figure out how to start page count after page xx