#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys,socket

BUF_SIZE=1024 #设置缓冲区大小
server_addr=("127.0.0.1",8080) #Ip地址和端口号确定地址 
try:
	server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建一个新的socket对象，socket.AF_INET表示ipv4通信，socket.SOCK_STREAM表示TCP通信
except scoket.error as msg:
	print("创建套接字失败："+str(msg[0])+"message:"+msg[1])
	sys.exit()
print("创建成功！")
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #设置地址复用
try:
	server.bind(server_addr) #绑定地址
except scoket.error as msg:
	print("绑定失败："+str(msg[0])+"message:"+msg[1])
	sys.exit()
print("绑定成功！")
server.listen(5) #最大监听数为5
print("scoket listening")
while True:
	client,client_addr=server.accept() #接收TCP连接，并返回新的套接字和地址，阻塞函数
	print('Connected by',client_addr)
	while True:
		data=client.recv(BUF_SIZE) #从客户端接收数据
		print(data)
		client.sendall(data) #发送数据到客户端
server.close() #关闭socket
