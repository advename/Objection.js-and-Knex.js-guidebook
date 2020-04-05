import os
from os.path import isfile, join
from os import listdir
import subprocess

book_name_md = "book.md"
book_name_pdf = "book.pdf"

if os.path.exists(book_name_md):
    os.remove(book_name_md)

files = [f for f in listdir(".") if isfile(join(".", f))]

markdown_text = ""

for i, file in enumerate(files):
    # 3. Only use markdown file
    if ".md" in file:
        #4. Read the file
        with open(file, 'r', encoding="utf8") as file:
            markdown_text += file.read() + "\n\\newpage\n"

markdown_text = markdown_text.replace("\n## ", "\n\\newpage\n## ")

book_markdown = open(book_name_md, 'wb')
book_markdown.write(markdown_text.encode("utf8"))
book_markdown.close()
# Run create
if os.path.exists(book_name_pdf):
    os.remove(book_name_pdf)
command = f"pandoc {book_name_md} -s -o {book_name_pdf} --css=pandoc.css -t html5 --lua-filter=pagebreak.lua"
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
