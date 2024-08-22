__author__="zhao"

import tkinter as tk
import random
import threading
import time
def dow():
    window = tk.Tk()
    width=window.winfo_screenwidth()
    height=window.winfo_screenheight()
    a=random.randrange(0,width)
    b=random.randrange(0,height)
    window.title('宝贝')
    window.geometry("200x50"+"+"+str(a)+"+"+str(b))
    tk.Label(window,
        text='一周年快乐！',    # 标签的文字
        bg='yellow',     # 背景颜色
        font=('楷体', 17),     # 字体和字体大小
        width=15, height=2  # 标签长宽
        ).pack()    # 固定窗口位置
    window.mainloop()
#更多python代码看主页
threads = []
for i in range(100):#需要的弹框数量
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()

   


