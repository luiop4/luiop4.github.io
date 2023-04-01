import sys
import you_get
import time
from tkinter import *
from tkinter.ttk import *


text = Text
def qkrz():
    rz4 = Label(ck1, text="                                    ")
    rz4.grid(row=6, column=1)
    rz5 = Label(ck1, text="                                                    ")
    rz5.grid(row=7, column=1)
    rz6 = Label(ck1, text="                                                   ")
    rz6.grid(row=8, column=1)
def xz():
    kh = Label(ck1,text="解析视频地址...")
    kh.grid(row=6,column=1)
    t = Label(ck1, text="准备下载...")
    t.grid(row=7, column=1)
    a = srk1.get()
    b = srk2.get()
    d = srk3.get()
    sys.argv = ['you-get', '-o',b,'-c',d,a]
    you_get.main()
    rz3=Label(ck1,text="下载完毕。")
    rz3.grid(row=8,column=1)
    tx = Label(ck1, text="建议清空日志后继续下载", font=("楷书"), fg="green")
    tx.grid(row=8, column=0)
ck1 = Tk()
ck1.title('视频下载工具')
ck1.geometry('420x340+500+500')
tc1 = Label(ck1,text="在下方输入视频地址与",font=("楷书"))
tc1.grid(row=0,column=0)
tc5 = Label(ck1,text="视频保存地址即可开始下载！",font=("楷书"))
tc5.grid(row=0,column=1)
tc2 = Label(ck1,text="网址：",font=("楷书,20"))
tc2.grid(row=1,column=0)
srk1 = Entry(ck1)
srk1.grid(row=1,column=1)
tc3 = Label(ck1,text="保存路径",font=("楷书,20"))
tc3.grid(row=2,column=0)
srk2 = Entry(ck1)
srk2.grid(row=2,column=1)
tc4 = Label(ck1,text="加载cookies文件（用\n于下载vip视频，不\n可留空,不加载请填no）",font=("楷书"))
tc4.grid(row=3,column=0)
srk3 = Entry(ck1)
srk3.grid(row=3,column=1)
an1 = Button(ck1,text="开始下载",command=xz)
an1.grid(row=4,column=1)
k = Label(ck1,text="**********************************")
k.grid(row=5,column=0)
k1 = Label(ck1,text="*****************************************")
k1.grid(row=5,column=1)
XS = Label(ck1,text="运行日志：",font=("楷书",15))
XS.grid(row=6,column=0)
qk = Button(ck1,text="清空日志",command=qkrz)
qk.grid(row=7,column=0)
tx = Label(ck1,text="重要：仅支持加载.txt与.sqlite格\n式的cookies文件；不支持下载\n腾讯视频的视频，其他的可正常\n下载（如爱奇艺.)")
tx.grid(row=9,column=0)
yu = Label(ck1,text="进度条可能会卡住\n请耐心等待,未响应是正常现象\n下载进度见终端，等待ui界面提示下载\n完成才可打开视频")
yu.grid(row=9,column=1)

ck1.mainloop()
