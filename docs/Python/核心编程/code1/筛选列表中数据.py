from random import randint
data = [randint(-10,10) for _ in range(10)]
# res = []
# for x in data:
#     if x>=0:
#         res.append(x)
# print(res)
# data1 = data.copy()
# for x in data1:
#     if x<0:
#         data.remove(x)
# print(data)
# data = [x for x in data if x>=0]
data = list(filter(lambda x:x>=0,data))
print(data)