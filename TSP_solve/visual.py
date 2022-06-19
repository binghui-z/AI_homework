from datetime import datetime
from time import strftime, time
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
# from tkinter import tk
import sys
from TSP_solve.TSP_ACO import TSP_ACO
from TSP_solve.TSP_GA import TSP_GA
from TSP_solve.TSP_PSO import TSP_PSO
from PIL import Image, ImageTk
# import torch
sys.setrecursionlimit(10000)
import time
from utils import run_time

def tick():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    clock.config(text=now)
    clock.after(200, tick)

def device():
    txt = 'cuda'# if torch.cuda.is_available() else 'cpu'
    hardware.config(text="当前设备为："+txt)
    hardware.after(200, device)

def running_time():
    time = run_time.get_value('runtime') #if torch.cuda.is_available() else 'cpu'
    alltime.config(text="运行时长："+str(time)+" s")
    alltime.after(200, running_time)

if __name__ == "__main__":
    #? inital 
    root = Tk()  # 父容器 
    root.geometry('900x400')  # 宽x高+偏移量
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

    #? 选择算法
    BBestFirst = Button(root, text="GA", width=10, height=2, command=TSP_GA).place(x=30, y=200)
    BBestSecond = Button(root, text="ACO",  width=10, height=2, command=TSP_ACO).place(x=330, y=200)
    BBestThird = Button(root, text="PSO",  width=10, height=2, command=TSP_PSO).place(x=630, y=200)


    root.mainloop()

    # plt.ioff()
    # plt.show()
