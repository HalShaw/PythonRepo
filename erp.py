from datetime import datetime,timedelta
from prettytable import PrettyTable
import re,math,pdb,sys
class glass:
	def __init__(self,glasses,gframe,luoding,gjia,gleg,nrise,gpian):
		self.glasses=glasses
		self.gframe=gframe
		self.luoding=luoding
		self.gjia=gjia
		self.gleg=gleg
		self.nrise=nrise
		self.gpian=gpian
	def xiadate(ddr):
		global XD
		XD=ddr-timedelta(days=1)
		return XD

	def donedate(dd):
		global DDR
		DDR=dd
		#DDR=datetime.strptime(dd, "%Y%m%d")
		return DDR

	def changestr2date(change):
		str2date=datetime.strptime(change, "%Y%m%d")
		return str2date

	def luoding_num(x,y):
		if x<-2:
			y=x+y
			z=0
			return y,z
		elif x>=0:
			return y,x

class gla(glass):
	def __init__(self,glasses,gframe,luoding,gpian):
		super().__init__(glasses,gframe,luoding,gpian)
		glass.__init__(self)
	def num1(glasses):
		gframe=1*glasses
		luoding=math.ceil(2*glasses/0.9)
		gpian=2*glasses
		return gframe,luoding,gpian
		
	def xdate1(glassesx):
		glassesx=XD
		gframex=glassesx-timedelta(days=2)
		luodingx=glassesx-timedelta(days=11)
		gpianx=glassesx-timedelta(days=21)
		return glassesx.strftime("%Y-%m-%d"),gframex.strftime("%Y-%m-%d"),luodingx.strftime("%Y-%m-%d"),gpianx.strftime("%Y-%m-%d")
	def ddate1(glassesd):
		glassesd=DDR
		gframed=glassesd-timedelta(days=1)
		luodingd=glassesd-timedelta(days=1)
		gpiand=glassesd-timedelta(days=1)
		return glassesd.strftime("%Y-%m-%d"),gframed.strftime("%Y-%m-%d"),luodingd.strftime("%Y-%m-%d"),gpiand.strftime("%Y-%m-%d")

class gkuang(glass):
	def __init__(self,gframe,luoding,gjia,gleg,nrise):
		super().__init__(gframe,luoding,gjia,gleg,nrise)
	def num2(gframe):
		luoding=math.ceil((4*gframe)/0.9-60)
		gjia=1*gframe
		gleg=2*gframe-30
		nrise=2*gframe
		return luoding,gjia,gleg,nrise
	def xdate2(gframex):
		gframex=XD-timedelta(days=2)
		luodingx=gframex-timedelta(days=11)
		gjiax=gframex-timedelta(days=21)
		glegx=gframex-timedelta(days=11)
		nrisex=gframex-timedelta(days=19)
		return luodingx.strftime("%Y-%m-%d"),gjiax.strftime("%Y-%m-%d"),glegx.strftime("%Y-%m-%d"),nrisex.strftime("%Y-%m-%d")
	def ddate2(gframed):
		gframed=XD
		luodingd=gframed-timedelta(days=2)
		gjiad=gframed-timedelta(days=2)
		glegd=gframed-timedelta(days=2)
		nrised=gframed-timedelta(days=2)
		return luodingd.strftime("%Y-%m-%d"),gjiad.strftime("%Y-%m-%d"),glegd.strftime("%Y-%m-%d"),nrised.strftime("%Y-%m-%d")



if __name__=="__main__":
	try:	
		while True:
			cho=input("请选择需要输入的需求数量（眼镜，镜框，父螺钉，子螺钉，镜架，镜腿，鼻托，镜片）:\n")
			if cho=='眼镜':
				g=int(input("请输入眼镜的需求数量:"))
				d1=input("请输入眼镜的完成日期:")
				dm=glass.changestr2date(d1)
				break
			elif cho=='镜框':
				g=int(input("请输入镜框的需求数量:"))
				d11=input("请输入镜框的完成日期:")
				dc=glass.changestr2date(d11)
				dm=dc+timedelta(days=1)
				break
			elif cho=='父螺钉':
				g3=int(input("请输入父螺钉的需求数量:"))
				d22=input("请输入父螺钉的完成日期:")
				g=math.ceil((g3+60)*0.9/2)
				dc=glass.changestr2date(d22)
				dm=dc+timedelta(days=1)
				break
			elif cho=='子螺钉':
				g4=int(input("请输入子螺钉的需求数量:"))
				d3=input("请输入子螺钉的完成日期:")
				g=math.ceil(g4*0.9/4)
				dc=glass.changestr2date(d3)
				dm=dc+timedelta(days=3)
				break
			elif cho=='镜架':
				g5=int(input("请输入镜架的需求数量:"))
				d4=input("请输入镜架的完成日期:")
				g=g5
				dc=glass.changestr2date(d4)
				dm=dc+timedelta(days=3)
				break
			elif cho=='镜腿':
				g6=int(input("请输入镜腿的需求数量:"))
				d5=input("请输入镜腿的完成日期:")
				g=g=math.ceil((g6+30)/2)
				dc=glass.changestr2date(d5)
				dm=dc+timedelta(days=3)
				break
			elif cho=='鼻托':
				g7=int(input("请输入鼻托的需求数量:"))
				d6=input("请输入鼻托的完成日期:")
				g=math.ceil(g7/2)
				dc=glass.changestr2date(d6)
				dm=dc+timedelta(days=3)
				break
			elif cho=='镜片':
				g8=int(input("请输入镜片的需求数量:"))
				d7=input("请输入镜片的完成日期:")
				g=math.ceil(g8/2)
				dc=glass.changestr2date(d7)
				dm=dc+timedelta(days=1)
				break
			else:
				print("输入错误！请按照提示输入！-_-")
				continue

		f1=gla.num1(g)
		f2=gkuang.num2(g)
		print("镜框,螺钉,镜片的需求数量:",f1)
		print("螺钉,镜架,镜腿,鼻托的需求数量:",f2)
		d=glass.donedate(dm)
		d2=glass.xiadate(d)
		g1=gla.xdate1(d2)
		g2=gla.ddate1(d)
		print("眼镜下达日期：",g1[0])
		print("眼镜完成日期：",g2[0])
		print("眼镜,镜框,螺钉,镜片的下达日期：",g1)
		print("眼镜,镜框,螺钉,镜片的完成日期：",g2)
		m1=gkuang.xdate2(d2)
		m2=gkuang.ddate2(d2)
		print("螺钉,镜架,镜腿,鼻托的下达日期：",m1)
		print("螺钉,镜架,镜腿,鼻托的完成日期：",m2)
		
		l1=list(f1)
		l2=list(f2)
		l5=list(g1)
		l6=list(g2)
		l7=list(m1)
		l8=list(m2)
		a=glass.luoding_num(f2[0],f1[1])
		y=PrettyTable(["调配方式", "物料号", "物料名称", "需求数量","日程下达日期","日程完成日期"])
		y.align["调配方式"]="2"
		y.padding_width = 1
		y.add_row(["生产","20000","眼镜",g,g1[0],g2[0]])
		y.add_row(["采购","20100","镜框",l1[0],g1[1],g2[1]])
		y.add_row(["采购","20099","螺钉",a[0],g1[2],g2[2]])
		y.add_row(["采购","20099","螺钉",a[1],m1[0],m2[0]])
		y.add_row(["采购","20110","镜架",f1[0],m1[1],m2[1]])
		y.add_row(["采购","20120","镜腿",f2[2],m1[2],m2[2]])
		y.add_row(["采购","20130","鼻托",f2[3],m1[3],m2[3]])
		y.add_row(["采购","20300","镜片",f1[2],g1[3],g2[3]])

		try:
			while True:
				choice=input('请选择需要输出的表格(选项为眼镜，镜框，父螺钉，子螺钉，镜架，镜腿，鼻托，镜片，所有,退出):')
				if choice=='眼镜':
					print(y[0])
				elif choice=='镜框':
					print(y[1])
				elif choice=='父螺钉':
					print(y[2])
				elif choice=='子螺钉':
					print(y[3])
				elif choice=='镜架':
					print(y[4])
				elif choice=='镜腿':
					print(y[5])
				elif choice=='鼻托':
					print(y[6])
				elif choice=='镜片':
					print(y[7])
				elif choice=='所有':
					print(y)
				elif choice=='退出':
					sys.exit()
				else:
					print("输入错误！请按照提示输入！-_-")
				continue
		except Exception as e:
			print("输入错误！请按照提示输入！-_-")
			
	except Exception as e:
		print("输入错误！请分别输入一个整数和一个日期字符串，形如100,20160313(或201634)(-_-)")