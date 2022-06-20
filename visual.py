from datetime import datetime
from tkinter import *
import psutil
import sys
from TSP_solve.TSP_ACO import TSP_ACO
from TSP_solve.TSP_GA import TSP_GA
from TSP_solve.TSP_PSO import TSP_PSO
sys.setrecursionlimit(10000)
from TSP_solve.utils import global_value
global_value._init()

def tick():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    clock.config(text=now)
    clock.after(200, tick)

def device():
    memory_use_percent = str(psutil.virtual_memory().percent)+' %'
    hardware.config(text="内存占用率："+memory_use_percent)
    hardware.after(200, device)

def running_time():
    time = global_value.get_value('runtime') #if torch.cuda.is_available() else 'cpu'
    alltime.config(text="运行时长："+str(time)+" s")
    alltime.after(200, running_time)

def route_length():
    length = global_value.get_value('length') #if torch.cuda.is_available() else 'cpu'
    all_lenth.config(text="最短长度："+str(length))
    all_lenth.after(200, route_length)

def getEntry():
    string = entry.get() # 获取Entry的内容
    global_value.set_value('iter',int(string))

def clear():
    entry.delete(0,'end') # 删除清空Entry控件的内容
    
if __name__ == "__main__":
    #? inital 
    root = Tk()  # 父容器 
    root.geometry('800x400')  # 宽x高+偏移量
    root.title('祖国那么大，我想去看看')

    frame1 = Frame(root, bd=4)
    frame1.pack(side=TOP)
    #? show time
    clock = Label(frame1, font=("none", 20, "bold"), bg="#FFFFFF", fg="#000000", bd=5, relief="ridge")
    clock.grid(row=0, column=0)
    clock.pack(side=TOP)
    tick()

    frame2 = Frame(root, bd=4)
    frame2.pack(side=TOP)
    hardware = Label(frame2, font=("none", 20, "bold"), bg="#FFFFFF", fg="#000000", bd=5, relief="ridge")
    hardware.grid(row=1, column=0)
    device()

    frame3 = Frame(root, bd=4)
    frame3.pack(side=BOTTOM)
    alltime = Label(frame3, font=("none", 20, "bold"), bg="#FFFFFF", fg="#000000", bd=5, relief="ridge")
    alltime.grid(row=0, column=0)
    running_time()

    frame4 = Frame(root, bd=4)
    frame4.pack(side=BOTTOM)
    all_lenth = Label(frame3, font=("none", 20, "bold"), bg="#FFFFFF", fg="#000000", bd=5, relief="ridge")
    all_lenth.grid(row=1, column=0)
    route_length()

    label = Label(root,text='请输入迭代次数',font=("none", 15, "bold"),height=1)
    label.pack(side=LEFT)
    entry = Entry(root,font=("none", 15, "bold"))
    entry.pack(side=LEFT) 
    button01 = Button(root,text='确定',font=("none", 15, "bold"),command=getEntry).place(x=500, y=180)
    button02 = Button(root,text='清空',font=("none", 15, "bold"), command=clear).place(x=600, y=180)

    #? 选择算法
    BBestFirst = Button(root, text="GA", font=("none", 15, "bold"), width=10, command=TSP_GA).place(x=30, y=230)
    BBestSecond = Button(root, text="ACO", font=("none", 15, "bold"), width=10, command=TSP_ACO).place(x=330, y=230)
    BBestThird = Button(root, text="PSO", font=("none", 15, "bold"),  width=10, command=TSP_PSO).place(x=630, y=230)

    root.mainloop()

    """打包为exe: 单个py文件 https://blog.csdn.net/yql_617540298/article/details/112441159
                  多个py文件相互依赖https://blog.csdn.net/weixin_43502949/article/details/101057825,
                  && https://blog.csdn.net/qq_45193872/article/details/123563085
    #step1: pyinstaller -F visual.py
    #step2: pyinstaller visual.spec
    #注：之前这个文件下导入了matplotlib库，会报错，替换掉以后就可以了
    """