import jieba
txt = input("请输入中文")
ls = jieba.lcut(txt)
print("{:.1f}".format(len(txt)/len(ls)))
