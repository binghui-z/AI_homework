import networkx as nx
import matplotlib.pyplot as plt
# from tkinter import *
import tkinter
from tkinter import ttk
import sys
from TSP_solve.TSP_ACO import TSP_ACO
from TSP_solve.TSP_GA import TSP_GA
from TSP_solve.TSP_PSO import TSP_PSO
from PIL import Image, ImageTk
sys.setrecursionlimit(10000)


top = tkinter.Tk()  # 父容器  #! Tkinter, python GUI 接口
top.geometry('500x300+500+300')  # 宽x高+偏移量
top.title('Romania Problems')
#Figure_2.png

# img = Image.open('Figure_2.png')  # 打开图片
# photo = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开
# label_img = tkinter.Label(top, image = photo)
# label_img.pack()

BBestFirst = tkinter.Button(top, text="GA", command=TSP_GA).place(x=30, y=100)
BBestSecond = tkinter.Button(top, text="ACO", command=TSP_ACO).place(x=30, y=150)
BBestThird = tkinter.Button(top, text="PSO", command=TSP_PSO).place(x=30, y=200)


top.mainloop()

plt.ioff()
plt.show()
