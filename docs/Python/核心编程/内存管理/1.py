import sys
a = [] #第一次
b = a #第二次
def get_count(a): # 临时引用第三次
    return sys.getrefcount(a)# 临时引用第四次
print(get_count(a))
print(sys.getrefcount(a))# 临时引用第三次
del b# 清除第二次的引用
print(sys.getrefcount(a))
a = [1,2,3] #重新赋值
print(sys.getrefcount(a)) 