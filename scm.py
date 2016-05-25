import math,pymysql
import pymysql.cursors
def access_mysql():
		conn = pymysql.connect(host='localhost', port=3306,user='root',passwd='NmGJWRb9W5J9AFzH',db='client')#连接数据库client
		cur = conn.cursor() #游标实例化
		#cur.execute("INSERT into data values(160,800000,5.0)")
		cur.execute("SELECT * FROM price") #执行选择语句，从表price里读出所有数据，表price存储价格和需求数量
		rs=cur.fetchall()#读取出来的所有值给rs，其数据类型为tuple
		print(rs)

		cur.execute("SELECT count(*) FROM price")#读入数据所有行数
		count=cur.fetchall()#赋值给count，此时count类型还是tuple
		c=count[0][0] #取出行数的值
		print(c)

		cur.execute("SELECT * FROM cost")
		rs2=cur.fetchall()
		print(rs2)

		cur.execute("SELECT count(*) FROM cost")
		count=cur.fetchall()
		c2=count[0][0]
		print(c2)
		
		return rs,c,rs2,c2
		cur.close()
		conn.close()

def judge_eoq(q,small_num,large_num):
	if small_num<q<large_num:
		return q
	else:
		return small_num

if __name__ == '__main__':
	try:
		rs,count,rs2,count2=access_mysql()
		print(rs,count,rs2,count2)
		'''s=float(input("请输入订货成本S:"))
		r=float(input("请输入年预测需求R:"))
		k=float(input("请输入年持有成本率K:"))'''
		b=[]
		for i2 in range(count2):
			s=rs2[i2][0]
			r=rs2[i2][1]
			k=rs2[i2][2]
			print("输入的订货成本S,年预测需求R,年持有成本率K分别为:",s,r,k,'\n')
			a=[]
			for i in range(count):
				c=rs[i][0]
				snum=rs[i][1]
				lnum=rs[i][2]
				q=math.ceil(math.sqrt(2*r*s/(k*c)))
				print("对应的EOQ分别为:",q,'\n')
				eoq=judge_eoq(q,snum,lnum)
				TAIC=math.ceil((r*c)+(eoq/2*k*c) +(r/eoq*s))
				a.append(TAIC)
			b.append(a)
		for i,item in enumerate(b):
			min_item=min(item)
			if min_item==item[0]:
				print("TAIC计算结果为",item,'\n',"最小TAIC为:",item[0],"所以选择第1组",rs[0],'\n')
			elif min_item==item[1]:
				print("TAIC计算结果为",item,'\n',"最小TAIC为:",item[1],"所以选择第2组",rs[1],'\n')
			else:
				print("TAIC计算结果为",item,'\n',"最小TAIC为:",item[2],"所以选择第3组",rs[2],'\n')
	except Exception as e:
		print(e)