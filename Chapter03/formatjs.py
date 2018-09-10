#!/usr/bin/env python2.7

import sys, json
from tabulate import tabulate

data = json.load(sys.stdin)

rows = []

def format_bug(vulnerability):
	row = [
		vulnerability['severity'],
		vulnerability.get('identifiers').get('summary', 'N/A') if vulnerability.get('identifiers', False) else 'N/A',
		vulnerability['file'] + "\n" + vulnerability.get('info', ['N/A'])[0]
	]
	return row

for item in data:
	for vulnerability in item['results'][0]['vulnerabilities']:
		vulnerability['file'] = item.get('file', 'N/A')
		row = format_bug(vulnerability)
		rows.append(row)

rows = sorted(rows, key=lambda x: x[0])

print(
"""
     ,--. ,---.   ,-----.                        
     |  |'   .-'  |  |) /_ ,--.,--. ,---.  ,---. 
,--. |  |`.  `-.  |  .-.  \|  ||  || .-. |(  .-' 
|  '-'  /.-'    | |  '--' /'  ''  '' '-' '.-'  `)
 `-----' `-----'  `------'  `----' .`-  / `----' 
                                   `---'         	
""")
print tabulate(rows, headers=['Severity', 'Summary', 'Info & File'])
