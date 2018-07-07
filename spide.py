#!-*- coding:utf-8 -*-
import requests
import re
import time
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url='http://www.rosimm8.com/rosimm/'
#f=open('down.txt','w')
a=requests.Session()
os.mkdir('img')
os.chdir('img')

def page(uu):
	con=a.get(uu).content

	res=re.findall('<span class=pageinfo><strong>\xe5\x85\xb1(.*)\xe9\xa1\xb5: </strong></span>',con)
	if res==[]:
		return 0
	return int(res[0])


def save(x):
	con=a.get(x)
	con.encoding='utf-8'
	con=con.text
	#print x
	res=re.findall(r'<img src="/uploads/allimg/(.*?)" />',con)
	title=re.findall('.html">(.*)</a>',con)
	#print title
	#print title[0]
	#title[0]=title[0].decode('gbk','ignore').encode('utf-8')
	#title[0]=title[0].encode('utf-8')
	#print title[0]
	nn=0
	for p in res:
		nn+=1
		wr='http://www.rosimm8.com/uploads/allimg/'+p
		print wr
		img=a.get(wr).content
		with open(title[0]+'_'+str(nn)+'.jpg','wb') as f:
			f.write(img)
		#time.sleep(0.1)

cc=0
for i in range(416,2518):  #(416,2518):
	if i%10==0:
		print i
	#print i
	urla=url+str(i)+'.html'
	#print urla 
	num=page(urla)
	#print num
	print urla
	save(urla)
	cc+=1
	for j in range(2,num+1):
		urlb=url+str(i)+'_'+str(j)+'.html'
		print urlb
		save(urlb)
		cc+=1
print cc
#f.close()



