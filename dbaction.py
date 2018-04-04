import pymysql  #导入 pymysql

def connectDBhandle():
	db = pymysql.connect(host="localhost",user="root",password="root",db="test",port=3306,charset="utf8")
	return db 

#查询数据库  
def selectDBdata(tabname='students',field = '*',where = '',order='id desc',limitnum = 1):  
	# 使用cursor()方法获取操作游标
	db =  connectDBhandle() 
	cur = db.cursor()  
	if where == '':
		sql = "select "+field+" from "+tabname+" order by "+ order +" limit "+ str(limitnum)   #1.查询操作 
	else:
		sql = "select "+field+" from "+tabname+" where "+ where +" order by "+ order+" limit " + str(limitnum)  #1.查询操作 

	try: 
	    cur.execute(sql)    		#执行sql语句  
	    results = cur.fetchall()    #获取查询的所有记录  
	    return results
	except Exception as e:  
	    raise e  
	finally:  
	    db.close()  #关闭连接 

#写入数据库 需要传写入数据,表名
def insertDBdata(data,tabname='students'):
	db =  connectDBhandle()
	# 使用cursor()方法获取操作游标 
	cur = db.cursor()  
	  
	sql_insert ='insert into '+tabname+'(%s) values(%s)'  
	columstr = ''
	for key in data.keys():
		columstr = columstr  + key + ','
	columstr = columstr.rstrip(',')	

	columvalstr = ''
	for val in data.values():
		columvalstr = columvalstr + '"' + str(val) + '",'
	columvalstr = columvalstr.rstrip(',')
	try:
	    cur.execute(sql_insert % (columstr,columvalstr))  
	    #提交  
	    db.commit()
	except Exception as e:
	    #错误回滚
	    print(e)
	    db.rollback()   
	finally:  
	    db.close()  

#更新数据库 需要传更新id,表名
def updateDBdata(data,tabname='students'):
	db =  connectDBhandle()
	# 使用cursor()方法获取操作游标  
	cur = db.cursor()  
	  
	sql_update ='update '+ tabname +' set %s where id = %d' 

	updatestr = ''

	for key in data.keys():
		if key == 'id':
			continue
		updatestr = updatestr + key + '="' + str(data[key]) + '",'
	updatestr = updatestr.rstrip(',')

	try:  
	    cur.execute(sql_update % (updatestr,data['id']))  #像sql语句传递参数  
	    #提交  
	    db.commit()  
	except Exception as e:  
	    #错误回滚  
	    db.rollback()
	finally:  
	    db.close() 

#删除数据库 需要传删除id,表名
def deleteDBdata(data,tabname='students'):
	db =  connectDBhandle()
	# 使用cursor()方法获取操作游标  
	cur = db.cursor()  
	  
	sql_delete ="delete from "+tabname+" where id = %d"  
	  
	try:  
	    cur.execute(sql_delete % (data['id']))  #像sql语句传递参数  
	    #提交  
	    db.commit()  
	except Exception as e:  
	    #错误回滚  
	    db.rollback()   
	finally:  
	    db.close() 


# selectDBdata()
# insertDBdata({'name':'tom','age':15})
# updateDBdata({'name':'tom1','age':18,'id':3})
# deleteDBdata({'id':5})