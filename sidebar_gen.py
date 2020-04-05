import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

sidebar_file = open('_sidebar.md', 'w')

for file in files:
	if ".md" in file:
		name = file.split(".md")
		file = file.replace(" ", "%20")
		sidebar_file.write( f"* [{name[0]}]({file})\n" )

sidebar_file.close()