# import libraries
import urllib
import os
import re
from bs4 import BeautifulSoup

page = urllib.request.urlopen('http://www.simonstalenhag.se/')
soup = BeautifulSoup(page, 'html.parser')

for a in soup.find_all('a'):
	case = str(a.get('href'))
	match = re.search('bilderbig', case)
	if match:
		image = 'http://www.simonstalenhag.se/' + a.get('href')
		if os.path.isfile(os.path.basename(image)) == False:
			try:
				urllib.request.urlretrieve(image, os.path.basename('/images/' + image))
				print(image)
			except:
	   			pass