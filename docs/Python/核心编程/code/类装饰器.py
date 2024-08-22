
class Decorator():
    def __init__(self,func) -> None:
        print('装饰成功')
        self.__func = func # 双下划线隐藏函数
    # 让对象变成可调用对象，可调用对象可以当成函数使用
    def __call__(self, *args, **kwds):
        print('正在进行装饰')
        self.__func()
@Decorator
def show():
    print('被装饰函数')
show()