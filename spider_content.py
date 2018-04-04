#coding:utf-8
import requests
from bs4 import BeautifulSoup
import dbaction
import time
import re
import os
from os import path
import urllib
import random

spidernumspertime = 50	#单次采集数量
issaveimg2local = 1		#是否保存图片到本地
localservername = 'http://localpythonspider.com' 
wherestr = " spider_status = 1"
spidernewslist = dbaction.selectDBdata('spidernews','id,link',wherestr,'id desc',spidernumspertime)
currentdirname = os.path.dirname(__file__)

def filter_tags(htmlstr):
	re_script=re.compile('<s*script[^>]*>[^<]*<s*/s*scripts*>',re.I)#Script
	re_style=re.compile('style="(.*?)"')#style
	re_a=re.compile('<a.*?>')
	re_ae=re.compile('</a>')
	re_class = re.compile('class="(.*?)"')
	re_id = re.compile('id="(.*?)"')
	re_br=re.compile('<brs*?/?>')#处理换行
	re_comment=re.compile('<!--[^>]*-->')#HTML注释
	s=re_script.sub('',htmlstr) #去掉SCRIPT
	s=re_style.sub('',s)#去掉style
	s=re_a.sub('',s)
	s=re_ae.sub('',s)
	s=re_class.sub('',s)
	s=re_id.sub('',s)
	s=re_br.sub('n',s)#将br转换为换行
	s=re_comment.sub('',s)#去掉HTML注释
	return s

def mkdir(pathname):
	pathname=pathname.strip() # 去除左右两边的空格
	pathname=pathname.rstrip("\\") # 去除尾部 \符号
	if not os.path.exists(pathname):
		os.makedirs(pathname)


def spider_content(linkurl):
    reshtml = requests.get(linkurl)
    bsObj=BeautifulSoup(reshtml.text,"lxml")    #将html对象转化为BeautifulSoup对象
    content=bsObj.findAll("div",{"id":"ctrlfscont"})

    if issaveimg2local == 1:
    	piclists = content[0].findAll('img') #获取所有图片

    	for picturehtml in piclists:
    		picurl = picturehtml.attrs['src'] #替换图片 -_-!!!! TODO
    		pictype = os.path.splitext(picurl)[1]
    		saveuploadpaths = "/uploads/"+time.strftime("%Y%m%d", time.localtime())+"/"
    		newimgname = time.strftime("%m%d%H%M%S", time.localtime())+str(random.randint(1000,9999))+pictype
    		pathdirname = currentdirname+saveuploadpaths
    		pathname = pathdirname+newimgname
    		mkdir(pathdirname)
    		try:
    			urllib.request.urlretrieve(picurl,pathname)
    			serveruploadpath = localservername+saveuploadpaths+newimgname
    			content[0] = str(content[0]).replace(picurl,serveruploadpath)
    		except Exception as err:
    			print(err)
    			continue

    return filter_tags(str(content[0]))


if spidernewslist:
	for news in spidernewslist:
		html = requests.get(news[1])
		bsObj=BeautifulSoup(html.text,"lxml")
		contentbox=bsObj.findAll("div",{"class":"inner"})
		pagelist=contentbox[0].findAll("div",{"class":"page"})
		contentstr = spider_content(news[1])

		if pagelist:
			pagelilist = pagelist[0].findAll('li')

			for pgli in pagelilist:
				if pgli.text.isdigit():
					if pgli.text == '1':
						continue
					else:
						otherlinks = pgli.find('a').attrs['href']
						contentstr = contentstr + '<p>=================================</p>'
						contentstr = contentstr + spider_content(otherlinks)
				else:
					continue

		contentstr = contentstr.replace('"',"“")
		contentstr = contentstr.replace("'","‘")
		update_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		if contentstr == '':
			tmpupdated = {"id":news[0],"contents":contentstr,"update_at":update_at,"spider_status":3}
		else:
			tmpupdated = {"id":news[0],"contents":contentstr,"update_at":update_at,"spider_status":2}
		
		dbaction.updateDBdata(tmpupdated,'spidernews')


print('done!')    	
    
