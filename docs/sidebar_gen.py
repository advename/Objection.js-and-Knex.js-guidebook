import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

sidebar_file = open('_sidebar.md', 'w')

for file in files:
	if ".md" in file and not "_sidebar" in file and not "README" in file:
		name = file.split(".md")
		name = name[0].replace("_", " ")
		sidebar_file.write( f"* [{name}]({file})\n" )

sidebar_file.close()