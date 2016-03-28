import math
class client:

	def count_age(age1,age2,mmage):
		dage=abs(age1-age2)/mmage
		return dage

	def count_slavery(slavery1,slavery2,mmslavery):
		dslavery=abs(slavery1-slavery2)/mmslavery
		return dslavery
		
	def distance(dage,dslavery):
		dis=math.sqrt(dage**2+dslavery**2)
		return "%.3f"%dis
if __name__ == '__main__':
	try:
		f=open('client.txt','r')
		for line in f:
			l=list(line)
			c=int(l[0]+l[1]+l[2])
			t=int(l[4]+l[5]+l[6]+l[7]+l[8]+l[9])
			print("客户的购买次数为:",c)
			print("客户的消费总额为:",t)
			l1=[2.0,1800.0,9.5]
			l2=[5.0,4900.0,9.0]
			l3=[8.0,7500.0,8.8]
			l4=[15.0,10000.0,8.5]
			l5=[20.0,13000,8.0]
			l6=[50.0,22000.0,7.8]
			l7=[70.0,40000.0,7.5]
			l8=[98.0,49890.0,7.2]
			l9=[120.0,59980.0,7.0]
			l10=[150.0,82000.0,6.8]
			maxage=max(l1[0],l2[0],l3[0],l4[0],l5[0],l6[0],l7[0],l8[0],l9[0],l10[0])
			minage=min(l1[0],l2[0],l3[0],l4[0],l5[0],l6[0],l7[0],l8[0],l9[0],l10[0])
			maxslavery=max(l1[1],l2[1],l3[1],l4[1],l5[1],l6[1],l7[1],l8[1],l9[1],l10[1])
			minslavery=min(l1[1],l2[1],l3[1],l4[1],l5[1],l6[1],l7[1],l8[1],l9[1],l10[1])
			if c>maxage:
				print("购买次数超出已有客户最大值，使用该值计算！")
				maxage=c  
			elif c<minage:
				print("购买次数超出已有客户最小值，使用该值计算！")
				minage=c
			if t>maxslavery:
				print("消费总额超出已有客户最大值，使用该值计算！")
				maxslavery=t
			elif t<minslavery:
				print("消费总额超出已有客户最小值，使用该值计算！")
				minslavery=t

			mmage=maxage-minage
			mmslavery=maxslavery-minslavery
			dc1=client.count_age(l1[0],c,mmage)
			dt1=client.count_slavery(l1[1],t,mmslavery)
			d11=client.distance(dc1,dt1)
			dc2=client.count_age(l2[0],c,mmage)
			dt2=client.count_slavery(l2[1],t,mmslavery)
			d22=client.distance(dc2,dt2)
			dc3=client.count_age(l3[0],c,mmage)
			dt3=client.count_slavery(l3[1],t,mmslavery)
			d33=client.distance(dc3,dt3)
			dc4=client.count_age(l4[0],c,mmage)
			dt4=client.count_slavery(l4[1],t,mmslavery)
			d44=client.distance(dc4,dt4)
			dc5=client.count_age(l5[0],c,mmage)
			dt5=client.count_slavery(l5[1],t,mmslavery)
			d55=client.distance(dc5,dt5)
			dc6=client.count_age(l6[0],c,mmage)
			dt6=client.count_slavery(l6[1],t,mmslavery)
			d66=client.distance(dc6,dt6)
			dc7=client.count_age(l7[0],c,mmage)
			dt7=client.count_slavery(l7[1],t,mmslavery)
			d77=client.distance(dc7,dt7)
			dc8=client.count_age(l8[0],c,mmage)
			dt8=client.count_slavery(l8[1],t,mmslavery)
			d88=client.distance(dc8,dt8)
			dc9=client.count_age(l9[0],c,mmage)
			dt9=client.count_slavery(l9[1],t,mmslavery)
			d99=client.distance(dc9,dt9)
			dc10=client.count_age(l10[0],c,mmage)
			dt10=client.count_slavery(l10[1],t,mmslavery)
			d10=client.distance(dc10,dt10)
			print("输入客户与1-10号客户的距离分别为：\n",d11,d22,d33,d44,d55,d66,d77,d88,d99,d10)
			mindis=min(d11,d22,d33,d44,d55,d66,d77,d88,d99,d10)
			if mindis==d11:
				print("该客户和客户1的消费习惯最接近，推荐折扣：",l1[2],'\n')
			elif mindis==d22:
				print("该客户和客户2的消费习惯最接近，推荐折扣：",l2[2],'\n')
			elif mindis==d33:
				print("该客户和客户3的消费习惯最接近，推荐折扣：",l3[2],'\n')
			elif mindis==d44:
				print("该客户和客户4的消费习惯最接近，推荐折扣：",l4[2],'\n')
			elif mindis==d55:
				print("该客户和客户5的消费习惯最接近，推荐折扣：",l5[2],'\n')
			elif mindis==d66:
				print("该客户和客户6的消费习惯最接近，推荐折扣：",l6[2],'\n')
			elif mindis==d77:
				print("该客户和客户7的消费习惯最接近，推荐折扣：",l7[2],'\n')
			elif mindis==d88:
				print("该客户和客户8的消费习惯最接近，推荐折扣：",l8[2],'\n')
			elif mindis==d99:
				print("该客户和客户9的消费习惯最接近，推荐折扣：",l9[2],'\n')
			elif mindis==d10:
				print("该客户和客户10的消费习惯最接近，推荐折扣：",l10[2],'\n')

			
			if float(mindis)>0.9:
				listback=[]
				listback.append(11)
				listback.append(c)
				listback.append(t)
				print('备用用户',listback)
	except Exception as e:
		print(e)




