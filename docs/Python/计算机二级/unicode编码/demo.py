n = eval(input("请输入一个9800-9811之间的正整数"))
print("{:+^11}".format(chr(n-1)+chr(n)+chr(n+1)))
