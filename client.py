#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys,socket
BUF_SIZE=1024 #设置缓冲区大小
Server_addr=('127.0.0.1',8880)  #Ip地址和端口号确定地址 
try:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #创建一个新的socket对象，socket.AF_INET表示ipv4通信，socket.SOCK_STREAM表示TCP通信
except socket.error as msg:
	print("创建套接字失败："+str(msg[0])+"message:"+msg[1])
	sys.exit()  #sys.exit(n) 退出程序引发SystemExit异常
client.connect(Server_addr)  #根据IP地址连接服务端
while True:
	data=input("Please input some string:")  #输入数据
	if not data:
		print("Input can't be empty,please input again.")
		continue
		client.sendall(data)  #发送所有数据到服务端
		data=client.recv(BUF_SIZE)  #从服务端接收数据
		print(data)
	client.close()  #关闭socket
