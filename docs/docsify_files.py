import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

sidebar_file = open('_sidebar.md', 'w')

for file in files:
	if ".md" in file and not "_sidebar" in file:
		file_cleaned = file.replace(" ", "_")
		os.rename(file, file_cleaned)

sidebar_file.close()