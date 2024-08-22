
__author__="阿杰"

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
    window.title('佳')
    window.geometry("200x50"+"+"+str(a)+"+"+str(b))
    tk.Label(window,
        text=' 国庆节要开开心心的喔 ',    # 标签的文字
        bg='MediumSpringGreen',     # 背景颜色
        font=('楷体', 12),     # 字体和字体大小
        width=100, height=10  # 标签长宽
        ).pack()    # 固定窗口位置
    window.mainloop()
threads = []
for i in range(200):#需要的弹框数量
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()

   


