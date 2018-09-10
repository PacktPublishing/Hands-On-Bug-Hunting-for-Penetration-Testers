#!/usr/bin/env python2.7

import os, sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
directory = sys.argv[2]

os.makedirs(directory)

def download_script(uri):
	address = url + uri if uri[0] == '/' else uri
	filename = address[address.rfind("/")+1:address.rfind("js")+2] 
	req = requests.get(url)
	with open(directory + '/' + filename, 'wb') as file:
		file.write(req.content)

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for script in soup.find_all('script'):
    if script.get('src'): download_script(script.get('src'))
