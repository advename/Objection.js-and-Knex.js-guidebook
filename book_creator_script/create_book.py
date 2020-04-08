import os
from os.path import isfile, join
from os import listdir
import subprocess
import re

src_folder = "./src"

book_name_md = "book.md"
book_name_html = "book.html"
book_name_pdf = "book.pdf"

if os.path.exists(book_name_md):
    os.remove(book_name_md)

files = [f for f in listdir(".") if isfile(join(".", f))]

markdown_text = "\n\n\\newpage\n"  # start with new page because of Table of contents
markdown_files = []

# Add only markdown files to the list
for file in files:
    if ".md" in file:
        markdown_files.append(file)

# Put them together and add \newpage to the end except last page
for i, file in enumerate(markdown_files):
    with open(file, 'r', encoding="utf8") as file:
        markdown_text += file.read()
        if not i == len(markdown_files) - 1:
            markdown_text += "\n\n\\newpage\n"

# Add new pages after each h1 and h2
markdown_text = markdown_text.replace("\n## ", "\n\n\\newpage\n## ")

# Make sure there is an empty new line before each list
markdown_text_array = markdown_text.splitlines()
for i, line in enumerate(markdown_text_array):
    if line:
        if line[0] == "-":
            if not markdown_text_array[i - 1][0] == "-":
                markdown_text_array[i] = f"\n{line}"
markdown_text = "\n".join(markdown_text_array)

book_markdown = open(book_name_md, 'wb')
book_markdown.write(markdown_text.encode("utf8"))
book_markdown.close()

# --lua-filter=pagebreak.lua is needed to use page breaks
# -f commonmark is needed to correctly convert lists
command = f"pandoc {book_name_md} -s -o {book_name_html} --css={src_folder}/pandoc.css -t html5 --lua-filter={src_folder}/pagebreak.lua metadata.yaml --table-of-contents --lua-filter={src_folder}/syntax_code_fix.lua --css={src_folder}/prism.css "
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# Edit html to work with prism
with open(book_name_html, 'r', encoding="utf8") as file:
    html_text = file.read()
html_text = html_text.replace(
    "<body>", '<body class="line-numbers"/>')  # add line number
wr = open(book_name_html, 'w', encoding="utf8")
wr.write(html_text)

# Remove pdf if already exists
if os.path.exists(book_name_pdf):
    os.remove(book_name_pdf)

import pdfkit
options = {
    'page-size': 'A4',
    'margin-top': '15mm',
    'margin-right': '15mm',
    'margin-bottom': '15mm',
    'margin-left': '15mm',
    'encoding': "UTF-8",
    'custom-header': [('Accept-Encoding', 'gzip')],
    'no-outline': None,
    'title': 'Objection.js and Knex.js Guidebook',
    'footer-right': '[page]',
    'header-right': '[section]',
    'header-spacing': '5',
    'footer-spacing': '5',
    'header-line': '',
    'header-font-name': 'Source Sans Pro,Helvetica Neue,Arial,sans-serif',
    'footer-font-name': 'Source Sans Pro,Helvetica Neue,Arial,sans-serif',
}

pdfkit.from_file(book_name_html, book_name_pdf, options=options)

# Delete temp book.md
# if os.path.exists(book_name_md):
#     os.remove(book_name_md)