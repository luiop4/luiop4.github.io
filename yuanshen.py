#文件最后修改 2023/4/10
#抽奖规则仅仅加入了10抽必出紫，和用比较粗暴直接的方法实现的出金保底
#至于区分大保底和小保底还没有实现，且出金后抽奖次数并不会重置
#这个程序只是闲时写着玩的
from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import random

count = 0     #抽奖次数初始值

data1 = ['弹弓','鸦羽弓','以理服人','飞天御剑','黎明神剑','神射手之誓','冷刃','旅行剑','翠玉法球','黑缨枪','沐浴龙血的剑','讨龙英雄潭','铁鹰阔剑'] #三星
data2 =['西风猎弓','西风长枪','暗巷的酒与诗','钟剑','祭礼剑'] #四星
data3 =['神里凌华','提哪里'] #五星
str7 = ['(三星)','(四星)','(五星)']
#奖池设置（data1,data2,data3列表）
gl =['2','2','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'
    ,'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
#概率设置（2为五星，1为四星，0为三星)

a = open('number.txt','w')
a.write('0')
a.close()
#创建文件用于实时刷新抽奖次数来计算小保底



def dy():
    text.insert(END, "********抽取十次********\n")  # 在文本框显示结果
    cqsc()

def cqsc():
    a = 1
    while a <= 10:
        cjs = open('number.txt', 'r')
        fz = cjs.read()
        yip = int(fz)
        cjs.close()
        hu = open('number.txt', 'w')
        jg = yip + 1
        loi = str(jg)
        hu.write(loi)
        hu.close()
        # 文件读取写入操作,用于抽奖统计次数刷新
        Label(xx, text=jg).grid(row=4, column=1)
        # 打印抽奖次数
        global star
        # 声明全局变量
        zh = int(random.choice(gl))
        if jg % 10 == 0:
            zh = 1
        if jg % 10 > 7:
            zh = int(random.randint(0, 2))
        if zh == 0:      # 判断抽奖结果
            sx = int(random.randint(0, 12))    #随机从三星角色池中抽取
            star = data1[sx]
            xj = str7[0]
        elif zh == 1:
            sx = int(random.randint(0, 4))    #随机从四星角色吃中抽取
            star = data2[sx]
            xj = str7[1]
        elif zh == 2:
            sx = int(random.randint(0, 1))      #随机从5星角色池中抽取，up=50%
            star = data3[sx]
            xj = str7[2]
        text.insert(END, star + xj + "\n")
        a += 1
def cyc():
    cjs = open('number.txt','r')
    fz = cjs.read()
    yip = int(fz)
    cjs.close()
    hu = open('number.txt','w')
    jg = yip+1
    loi = str(jg)
    hu.write(loi)
    hu.close()
    #文件读取写入操作,用于抽奖统计次数刷新
    Label(xx, text=jg).grid(row=4, column=1)
    #打印抽奖次数
    global star
    zh = int(random.choice(gl))
    if jg % 10 == 0:
        zh = 1
    if zh == 0:
        sx = int(random.randint(0,12))
        star = data1[sx]
        xj = str7[0]
    elif zh == 1:
        sx = int(random.randint(0, 4))
        star = data2[sx]
        xj = str7[1]
    elif zh == 2:
        sx = int(random.randint(0, 1))
        star = data3[sx]
        xj = str7[2]
    # 判断抽奖结果
    text.insert(END,"********抽取一次********\n")
    text.insert(END,star+xj+"\n")
    # 在文本框显示结果


def noce():
    text.insert(END, "读取卡池列表.....\n")
    text.update_idletasks()
    zjm.after(800)
    text.insert(END, "********卡池列表v1.02********\n")
    for list in data3:
        text.insert(END, list + "(五星)\n")
    for list in data2:
        text.insert(END, list + "(四星)\n")
    for list in data1:
        text.insert(END, list + "(三星)\n")


zjm = Tk()
zjm.title('米忽悠抽卡模拟 ')
zjm.geometry('550x350+300+200')
# 标签
rz = Frame(zjm)
rz.grid(row=0,column=0,pady=3,padx=5)
bq = Label(rz,text="当前卡池:神里凌华",foreground="red").grid(row=0,column=0)
yu = Frame(zjm)
yu.grid(row=1,column=0,pady=3,padx=5)
text = scrolledtext.ScrolledText(yu,width=40,height=24)
text.pack()
text.insert(END,"********开发版V1.03********\n")
a = 5
text.insert(END,"构建与读取数据文件....\n")
text.insert(END,"完成....\n")
xx =Frame(zjm)
xx.grid(row=1,column=1)
kacx = Label(xx,text="抽卡选项").grid(row=0,column=0)
an1 = Button(xx,text="查看卡池列表",command=noce)
an1.grid(row=1,column=0,pady=3)
an2 = Button(xx,text="来一发",command=cyc)
an2.grid(row=2,column=0,pady=3)
an3 = Button(xx,text="来10发",command=dy)
an3.grid(row=3,column=0)
cjcs = Label(xx,text="抽奖次数:").grid(row=4,column=0)
# ui界面实现
zjm.mainloop()