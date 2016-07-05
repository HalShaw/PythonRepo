#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import urllib.request
import re
import json
import random
import socket
import io
import pymysql
import pymysql.cursors
import multiprocessing
import threading
from datetime import datetime
from time import clock
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class Jokes(object):
	def createTable(self):
		conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='',db='client',charset="utf8")#连接数据库client
		cur = conn.cursor()
		cur.execute("DROP TABLE IF EXISTS joke")
		cur.execute("CREATE TABLE joke(title varchar(250) not null,content varchar(255) not null) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
		conn.close()

	def getContent(self,data):
		content=re.findall(r'"text":"(.*?)"', data,re.S)
		title=re.findall(r'"title":"(.*?)"',data,re.S)
		time=re.findall(r'"ct":"(.*?)"', data,re.S)
		removeTab=re.compile('\t|\r|\n|</p>|<p>|<br />')
		try:
			conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='自己的密码',db='client',charset="utf8")#连接数据库client
			cur = conn.cursor()
			for i in range(len(content)):
				#print('标题：'+title[i].replace(r'\r','').replace(r'\n','').replace(r'\t','').strip(),'\n',re.sub(removeTab,'',content[i]).replace(r'\r','').replace(r'\n','').replace(r'\t','').strip(),'\n\n')
				tit=title[i].replace(r'\r','').replace(r'\n','').replace(r'\t','').strip()
				cont=re.sub(removeTab,'',content[i]).replace(r'\r','').replace(r'\n','').replace(r'\t','').replace('\t','').strip()
				if title[i]==None or content[i]==None:
					pass
				else:
					cur.execute("INSERT INTO joke(title,content)values('%s','%s')"%(tit,cont))
			cur.execute("SELECT* from joke")
			conn.commit()
			result=cur.fetchall()
			print(result)	
		except Exception as e:
			conn.rollback()
			pass
		conn.close()

	def spider(self):
		try:
			for i in random.sample(range(2400),2):#可以设置爬取数量
				page='page='+str(i)
				full_url='http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?'+page
				req = urllib.request.Request(full_url)
				req.add_header("apikey", "自己的秘钥")
				resp = urllib.request.urlopen(req,timeout=5)
				data= resp.read().decode('utf-8')
				self.getContent(data)
		except socket.error as e:
			pass

	def main(self):
		#process=threading.Thread(target = self.spider)
		process=multiprocessing.Process(target = self.spider)
		process.start()
		process.join()


if __name__ == '__main__':
	start=clock()
	joke=Jokes()
	joke.createTable()
	joke.main()
	finish=clock()
	print(finish-start)#运行时间


