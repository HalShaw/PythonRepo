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
        f=open('hang.txt','r')
        for line in f:
            l=list(line)
            cho=l[0]+l[1]+l[2]
            num_in=int(l[4]+l[5]+l[6])
            date_in=l[8]+l[9]+l[10]+l[11]+l[12]+l[13]+l[14]+l[15]
            while True:
                if (' 眼镜'in cho)==True:
                    g=num_in
                    d1=date_in
                    print("眼镜的需求数量:",g)
                    print("眼镜的完成日期：",d1)
                    dm=glass.changestr2date(d1)
                    break
                elif (cho==' 镜框')==True:
                    g=num_in
                    d11=date_in
                    print("眼镜的需求数量:",g)
                    print("眼镜的完成日期：",d11)
                    dc=glass.changestr2date(d11)
                    dm=dc+timedelta(days=1)
                    break
                elif cho=='父螺钉':
                    g3=num_in
                    d22=date_in
                    print("父螺钉的需求数量:",g3)
                    print("父螺钉的完成日期：",d22)
                    g=math.ceil(g3*0.9/2)
                    dc=glass.changestr2date(d22)
                    dm=dc+timedelta(days=1)
                    break
                elif cho=='子螺钉':
                    g4=num_in
                    d3=date_in
                    print("子螺钉的需求数量:",g4)
                    print("子螺钉的完成日期：",d3)
                    g=math.ceil((g4+60)*0.9/4)
                    dc=glass.changestr2date(d3)
                    dm=dc+timedelta(days=3)
                    break
                elif cho==' 镜架':
                    g5=num_in
                    d4=date_in
                    print("镜架的需求数量:",g5)
                    print("镜架的完成日期：",d4)
                    g=g5
                    dc=glass.changestr2date(d4)
                    dm=dc+timedelta(days=3)
                    break
                elif cho==' 镜腿':
                    g6=num_in
                    d5=date_in
                    print("镜腿的需求数量:",g6)
                    print("镜腿的完成日期：",d5)
                    g=math.ceil((g6+30)/2)
                    dc=glass.changestr2date(d5)
                    dm=dc+timedelta(days=3)
                    break
                elif cho==' 鼻托':
                    g7=num_in
                    d6=date_in
                    print("鼻托的需求数量:",g7)
                    print("鼻托的完成日期：",d6)
                    g=math.ceil(g7/2)
                    dc=glass.changestr2date(d6)
                    dm=dc+timedelta(days=3)
                    break
                elif cho==' 镜片':
                    g8=num_in
                    d7=date_in
                    print("镜片的需求数量:",g8)
                    print("镜片的完成日期：",d7)
                    g=math.ceil(g8/2)
                    dc=glass.changestr2date(d7)
                    dm=dc+timedelta(days=1)
                    break
                else:
                    print("输入错误！请按照提示输入！-_-")
                    break
            f1=gla.num1(g)
            f2=gkuang.num2(g)
            d=glass.donedate(dm)
            d2=glass.xiadate(d)
            g1=gla.xdate1(d2)
            g2=gla.ddate1(d)
            m1=gkuang.xdate2(d2)
            m2=gkuang.ddate2(d2)
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
            print(y)
        f.close()          
    except Exception as e:
        print(e)
        