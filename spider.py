#coding:utf-8
import requests
from bs4 import BeautifulSoup
import dbaction
import time

reshtml = ''
try:
	reshtml = requests.get('http://www.cankaoxiaoxi.com/')
except Exception as err:
	print(err)
	print('请求出现异常，请检查网址是否正确')
	exit()

if reshtml == '':
	print('请求不到任何数据，请检查网址是否正确')
else:
	bsObj=BeautifulSoup(reshtml.text,"lxml")    #将html对象转化为BeautifulSoup对象  
	ulList=bsObj.findAll("ul",{"class":"yaowen"})   #找到所有ul 

	if ulList:
		for ul in ulList:  
		    uls = ul.findAll('li')
		    for lis in uls:
		    	newsd= dbaction.selectDBdata('spidernews','sort_num')
		    	if len(newsd) <= 0:
		    		newssortnum = 0
		    	else:	
		    		newssortnum = newsd[0][0] + 10

		    	title = lis.find('a').attrs['title']
		    	if title == '':
		    		title = lis.find('a').text
		    	title = title.replace('"',"“")
		    	title = title.replace("'","‘")
		    	link = lis.find('a').attrs['href']
		    	create_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		    	sources = '参考消息'
		    	data = {"title":title,"link":link,"create_at":create_at,"sources":sources,"sort_num":newssortnum,"update_at":create_at}
		    	#判断去重
		    	whereconditions = 'title = "'+title+'" and link="'+link+'"'
		    	hasnewsd = dbaction.selectDBdata('spidernews','*',whereconditions)
		    	if hasnewsd:
		    		continue
		    	else:
		    		dbaction.insertDBdata(data,'spidernews')

print('done!')    	
    
