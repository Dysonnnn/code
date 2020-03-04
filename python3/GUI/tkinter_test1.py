# -*- coding:utf-8 -*-
# python3
# print("111\n" * 6)
# from  tkinter import *

'''
2020.02.29

使用python3进行编程
使用tkinter模块进行图形界面设计
参考内容在最后的附录
功能：
界面内容从上到下：
1. 用户名和密码输入框，用户名明文输入，密码密文输入；
单独的输入框、文本框，在输入框内容输入内容，
2. 点击按钮“insert to text point”，可以实现将输入框的内容输入到文本框的鼠标位置处（如鼠标不在文本框内，则默认从头开始输入）；点击按钮“insert to text end ”，类似上面的按钮，不同的是新增内容是增加到文本的末尾；
3. 点击按钮“click me”，会显示一个弹窗；
4. 点击按钮“click me?” 会在粉色图框内显示“you click me”文字，再次点击，文字消失；
5. 下拉窗口，相关功能没写。

'''

import tkinter as tk
import tkinter.messagebox as messagebox

window = tk.Tk()
#设置窗体名称
window.title('My GUI window')

winWidth = 600
winHeight = 400
# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
  
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)

# 设置窗口初始位置在屏幕居中  width x height + x_offset + y_offset
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口图标
# window.iconbitmap("./image/icon.ico")

def helloCallBack():
	print("open windows")
	messagebox.showinfo("hello Python", "Hello Runoob") # windows msg, content

# 设置一个框架, 框架内的组件不需要pack(),框架要pack()
# 框架内组件设置位置 .grid(row = 行数， column = 列数)
myFrame = tk.Frame(window)
myFrame.place(rely=.5, relx=0.5, x=-100, y=-100)
print(myFrame.place_info())

# Label 显示一个文本或图象。
# 参数： Label(myFrame, text = 'Label', bg = 'orange', font = ('Arial', 15), width = 10, height = 2)
myVar = tk.StringVar()
myLabel0 = tk.Label(myFrame, text = 'username',font = ('Arial', 12), width = 10, height = 2).grid(row = 0)
# myLabel1.pack()

myLabel1 = tk.Label(myFrame, text = 'password',font = ('Arial', 12), width = 10, height = 2).grid(row = 1)
# myLabel2.pack()

myEntry1 = tk.Entry(myFrame, show = None, font=('Arial', 12)).grid(row = 0, column = 1)
# myEntry1.pack()

myEntry2 = tk.Entry(myFrame, show = '*', font=('Arial', 12)).grid(row = 1, column = 1)
# myEntry2.pack()

myFrame.pack()

# 在鼠标焦点处输入内容
def insert_point(_Text, _Entry):
	try:
		var = _Entry.get()
		print("get msg: " + var)
		_Text.insert('insert', var)
	except:
		print("get nothing")

# 在文本框内容最后接着插入输入内容
def insert_end(_Text, _Entry):
	try:
		var = _Entry.get()
		print("get msg: " + var)
		_Text.insert('end', var)
	except:
		print("get nothing")


on_click = False
def	click_callback():
	global on_click
	if on_click == False:
		on_click = True
		myVar.set("you click me")
	else:
		on_click = False
		myVar.set('')

myEntry3 = tk.Entry(window, show = None, font=('Arial', 12))
myEntry3.pack()
myText = tk.Text(window, height = 3)
myText.pack()


btn1 = tk.Button(window, text = "click me", command = helloCallBack)
btn1.pack()


btn2 = tk.Button(window, text = "insert to text point", command = lambda : insert_point(myText, myEntry3))
btn2.pack()

btn3 = tk.Button(window, text = "insert to text end" , command = lambda : insert_end(myText, myEntry3))
btn3.pack()

myLabel3 = tk.Label(window, textvariable = myVar, bg = 'pink', font = ('Arial', 15), width = 10, height = 2)
myLabel3.pack()

btn4 = tk.Button(window, text = "click me? ", font=('Arial', 10), width=10, height=1, command = click_callback)
btn4.pack()


myVar_listbox = tk.StringVar()
myVar_listbox.set((1, 2, 3, 4))
# 列表
myListBox = tk.Listbox(window, listvariable = myVar_listbox)
myListBox.pack()


# 将小部件放置到主窗口中

# 运行界面   进入消息循环
window.mainloop()



'''
附录：

主要内容参考 菜鸟教程、 https://blog.csdn.net/ahilll/article/details/81531587 、    

----------------------------------
 但如果 command 函数需要参数该怎么办呢，很简单，使用lambda， from https://blog.csdn.net/weixin_38428980/article/details/81225731

import Tkinter
 
def handler(a, b, c):
    # 事件处理函数
    print "handler", a, b, c
 
 
if __name__=='__main__':
    root = Tkinter.Tk()
    # 通过中介函数handlerAdapotor进行command设置
    btn = Tkinter.Button(text=u'按钮', command=lambda : handler(a=1, b=2, c=3))
    btn.pack()
    root.mainloop()
----------------------------------


设置窗口位置：

Python Tkinter Place布局管理器及用法
https://www.cnblogs.com/jsdd/articles/11482023.html

x：指定组件的 X 坐标。x 为 0 代表位于最左边。
y：指定组件的 Y 坐标。y 为 0 代表位于最右边。
# 设置窗口的大小和位置
# width x height + x_offset + y_offset
root.geometry("250x250+30+30") 



Tkinter 之Place布局
https://www.cnblogs.com/yang-2018/p/11792068.html

x	指定该组件的水平偏移位置（像素），如同时指定了 relx 选项，优先实现 relx 选项
y	指定该组件的垂直偏移位置（像素），如同时指定了 rely 选项，优先实现 rely 选项

# 获取屏幕分辨率
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
  
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)

# 设置窗口初始位置在屏幕居中
window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# 设置窗口图标
window.iconbitmap("./image/icon.ico")
# 设置窗口宽高固定
window.resizable(0, 0)

frame = tk.Frame(window)
frame.place(rely=.5, relx=0.5, x=-100, y=-100)
# 返回参数信息
print(frame.place_info())
  
tk.Label(frame, text="用户名").grid(row=0) # 第一行
tk.Label(frame, text="密码").grid(row=1)  # 第二行

---------------------------------
Tkinter（八）—— frame框架
https://blog.csdn.net/qq_39326657/article/details/81735636?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

# 定义一个大的frame，定义在window上
frm = tk.Frame(window)
frm.pack()

# 定义两个小的frame，放在大的frame上，分别放在左边和右边
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side = 'left')
frm_r.pack(side = 'right')

# 定义三个label，两个放在左框架，一个放在右框架
tk.Label(frm_l,text = '左框架上',bg = 'blue',width = 20).pack()
tk.Label(frm_l,text = '左框架下',bg = 'blue',width = 20).pack()
tk.Label(frm_r,text = '右框架上',bg = 'green',width = 20).pack()

————————————————
版权声明：本文为CSDN博主「Dance At Bougival」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_39326657/article/details/81735636
'''