import json
import requests
from bs4 import BeautifulSoup
import re
import os
import urllib
import time

tag='chulilla'
mypath = 'chulilla.com/insta/'
myurl='https://chulilla.com/'

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
	image_src = post['node']['thumbnail_resources'][1]['src']
	print(image_src)
	#urllib.request.urlretrieve(image_src, os.path.basename(image_src))
	#urllib.request.urlretrieve(image_src, my_path+"chulilla-"+str(contador)+".jpg")
	urllib.urlretrieve(image_src, mypath+"/images/"+tag+str(contador)+".jpg")	
	contenido=contenido+image_src+"\n"
	cHtml=cHtml+'<div class="flimg"><img src="'+myurl+'/images/'+tag+str(contador)+'.jpg'+'" alt="" class="responsive-image"></div>'
	contador=contador+1
	time.sleep(2)
cHtml=cHtml+'</div></div>'
f = open(mypath+tag+'.html','w+')
f.write(cHtml)
f.close
