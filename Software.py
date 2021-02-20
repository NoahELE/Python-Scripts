import os

software_installation_locations = ['F:', 'C:\\Users\\63599\\desktop']

software_list = []

for software_installation_location in software_installation_locations:
	for file in os.listdir(software_installation_location):
		if file in ['$RECYCLE.BIN', '63599', 'WindowsApps', 'WpSystem', 'WUDownloadCache', 'desktop.ini']:
			continue
		elif file[-4:0] == '.lnk':
			file = os.path.splittext(file)[0]
		software_list.append(file)

text = '\n'.join(software_list)

with open('D:\\Backup\\software_backup_list.txt', 'w', encoding = 'UTF-8') as f:
	f.write(text)
