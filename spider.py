# -*-coding:utf-8-*-

import urllib.request
import re
import sqlite3
import time
import random
import threading
import multiprocessing
import urllib.error
import sys
import socket
import io
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')#解决GBK编码错误问题

class Article(object):
	def __init__(self):
		self.url="http://wallstreetcn.com/"
		self.removeP=re.compile('</p>')#用来提取正文内容
		self.removeRight=re.compile('class=".*?"|align=".*?"|>')
		self.removeStrong=re.compile("<strong>|</strong>")
		self.removeAddr=re.compile('<a.*?>|</a>')
		self.replaceBR=re.compile('<br><br>|<br>|</br>')
		self.removeImg=re.compile('<img.*?>| {1,7}|&.*?;')
		self.removeExtraTag=re.compile('<.*?>|style=".*?"|value=".*?"')
		self.removeNoneLine=re.compile('\n+')

	def get_content(self,article):
		#使用正则表达式匹配出标题、作者、日期、内容、第一张大图的url、评论数
		title = re.findall(r'<h1 class="article-title">(.*?)</h1>',article,re.S)

		author=re.search(r'<span class="item author">(.*?)target="_blank">(.*?)</a>(.*?)</span>',article,re.S)
		
		post_at=re.findall(r'<span class="item time">(.*?)</span>',article,re.S)
		time=post_at[0]
		year=time[:4]
		month=time[5:7]
		day=time[8:10]
		hour=time[12:]#对有中文时间格式处理，返回值为datetime格式

		p_content=re.findall(r'<p(.*?)</p>',article,re.S)#正文内容有多种类型，分别匹配
		span_content=re.findall(r'<span>(.*?)</span>',article,re.S)
		if p_content==None:
			content=span_content
		else:
			content=p_content

		str_data=''.join(content[:-4])
		removed_p=re.sub(self.removeP,'\n',str_data)
		removed_strong=re.sub(self.removeStrong,'',removed_p)
		removed_addr=re.sub(self.removeAddr,'',removed_strong)
		removed_br=re.sub(self.replaceBR,'\n',removed_addr)
		removed_img=re.sub(self.removeImg,'',removed_br)
		removed_tag=re.sub(self.removeExtraTag,'',removed_img)
		removed_right=re.sub(self.removeRight,'',removed_tag)
		content=re.sub(self.removeNoneLine,'\n',removed_right)


		img_1=re.search(r'<img alt="(.*?)" src="(.*?!article\.foil)" (.*?)',article,re.M|re.I)#处理文章第一张大图片的url
		img_2=re.search(r'<img src="(.*?!article\.foil)" alt="(.*?)" (.*?)',article,re.M|re.I)
		if img_1!=None :
			img=img_1.group(2)
		elif img_2!=None:
			img=img_2.group(1)
		else:
			img=None

		comment_count=re.findall(r'<span class="wscn-cm-counter">(.*?)</span>',article,re.S)
		
		try:

			if img==None and comment_count==None:#有可能文章没有图片和评论，考虑以下几种情况
				return str(title[0]),str(author.group(2)),datetime.strptime(year+'-'+month+'-'+day+' '+hour,'%Y-%m-%d %H:%M:%S'),''.join(content),None,0
			elif img!=None and comment_count==None:
				return str(title[0]),str(author.group(2)),datetime.strptime(year+'-'+month+'-'+day+' '+hour,'%Y-%m-%d %H:%M:%S'),''.join(content),str(img),0
			elif img==None and comment_count!=None:
				return str(title[0]),str(author.group(2)),datetime.strptime(year+'-'+month+'-'+day+' '+hour,'%Y-%m-%d %H:%M:%S'),''.join(content),None,int(comment_count[0])
			else:
				return str(title[0]),str(author.group(2)),datetime.strptime(year+'-'+month+'-'+day+' '+hour,'%Y-%m-%d %H:%M:%S'),''.join(content),str(img),int(comment_count[0])
		except Exception as e:
			pass

	def create_table(self):
		conn=sqlite3.connect('article.db')
		#如果不存在一个art表，新建一个art表
		conn.execute("CREATE TABLE IF NOT EXISTS art(title varchar(80) PRIMARY KEY not null, author varchar(10),post_at TEXT not null,content varchar(255) not null,img varchar(20) ,comment_count integer);")
		conn.close()

	def save_content(self,title,author,post_at,content,img,comment_count):
		#连接并保存到数据库
		conn=sqlite3.connect('article.db')
		conn.execute("INSERT INTO art (title,author,post_at,content,img,comment_count)values(?,?,?,?,?,?)",(title,author,post_at,content,img,comment_count))
		result=conn.execute("SELECT * FROM art")
		return list(result)
		conn.close()

	def spider(self):
		cou=1
		#for i in range(1999,20002):#顺序生成URL
		for i in random.sample(range(19,247271),10000):#随机生成url，数字可以任意
			try:
				try:
					full_url=self.url+'node'+'/'+str(i)#URL格式
					page = urllib.request.urlopen(full_url,timeout=5)#设置请求时间限制
					pages= page.read().decode('utf-8','ignore')
					lst=self.get_content(pages)
					#self.save_content(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5])#不打印出结果
					print(self.save_content(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5]))#打印出结果
					print('Downloaded Successfully...\n')
					cou+=1
					time.sleep(1)
					if cou>3:#控制爬取300篇文章
						sys.exit()
					else:
						continue
				except Exception as e:
					pass
			except socket.error as e:
				pass#可以不打印出错误
	
				
	def main(self):
		#多线程和多进程爬取
		my_thread = threading.Thread(target = self.spider)#多线程
		#my_thread = multiprocessing.Process(target = self.spider)#多进程
		my_thread.start()
		my_thread.join()

	

if __name__ == '__main__':
	a=Article()#实例化
	a.create_table()
	a.main()






