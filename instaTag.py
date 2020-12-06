import json
import requests
from bs4 import BeautifulSoup
import re
import os
import urllib
import time
#-------------
#CONFIGURATION
#-------------
tag='chulilla'
mypath = '/home/carlos/testeo/insta/subir/scrape-instagram'
myurl='https://chulilla.com/'
folder='/images/'
e_folder='insta/'
image_size=4
"""
You can add the variableimage_text to the html and display it
"""
#-------------
r = requests.get('https://www.instagram.com/explore/tags/'+tag+'/')
soup = BeautifulSoup(r.text, 'html.parser')
script = soup.find('script', text=lambda t: t.startswith('window._sharedData'))
page_json = script.string.split(' = ', 1)[1].rstrip(';')
#print(page_json)
data = json.loads(page_json)
contenido=''
contador=0
cHtml='<div class="flicontainer"><div class="fligrid">'
for post in data['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
	image_src = post['node']['thumbnail_resources'][image_size]['src']
	image_text=post['node']['edge_media_to_caption']['edges'][0]['node']['text']
	print(image_src)
	urllib.urlretrieve(image_src, mypath+folder+tag+str(contador)+".jpg")	
	contenido=contenido+image_src+"\n"
	cHtml=cHtml+'<div class="flimg"><img src="'+myurl+e_folder+tag+str(contador)+'.jpg'+'" alt="" class="responsive-image"></div>'
	contador=contador+1
	time.sleep(2)
cHtml=cHtml+'</div></div>'
f = open(mypath+folder+tag+'.html','w+')
f.write(cHtml)
f.close
