def func_out():
    num = 10
    def func_inner():
        # num = 20  # 定义内部函数局部变量并非修改外部函数变量
        nonlocal num
        num+=1
        print("修改后num：",num)
    print("修改前num：",num)
    return func_inner
new_func = func_out()
new_func()