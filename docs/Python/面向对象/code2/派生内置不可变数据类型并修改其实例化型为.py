# 想自定义一种新类型的元组，对传入的可迭代对象，只保留其中int类型且值大于0的元素
class IntTuple(tuple):
    def __new__(cls,iterable):
        g = (x for x in iterable if isinstance(x,int) and x>0)
        return super(IntTuple,cls).__new__(cls,g)

t = IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)