# Python基础复习

> 二刷python基础，学完python基础的朋友一起来加深记忆吧！让你在后续写代码少出bug

## 运算符

### //

> `//` 运算符是 Python 中的整数除法运算符。它会返回除法运算后的商的整数部分，即向下取整。例如，`5 // 2` 的结果是 `2`，而不是 `2.5`。这个运算符在需要得到整数结果而不需要小数部分时非常有用。如果想要得到除法运算的浮点数结果，可以使用单斜杠 `/` 运算符。

## 转义符

> 1. \n: 换行
> 2. \t：水平制表符
> 3. \r：覆盖(后面出现的字符覆盖前面的)
> 4. \b：删除(删除\b前一个字符，相当于键盘上的backspace)
> 5. \: 使两个反斜线表示一个\   (==输出上面的转义符也可以在前面多加一个\  例如`print(“\\n”)`$\Rightarrow$\\n)

### 示例

#### 取消`“”`转义

```python
print("你好\"小杰\"")#想要原样输出带引号的小杰就必须在每个引号前加\或者把外面的引号改成单引号
```

#### 取消其他转义

==统一在字符串前加r可取消整句转义==

```python
print(r"你好\n小杰\n今天有没有加油啊？")
```

上句全被原样输出$\rightarrow$你好\n小杰\n今天有没有加油啊？

## not/and/or逻辑运算符优先级

==not>and>or==

## 交换两个变量的值

```python
# 交换
# 法一：中间变量
a = "hello"
b = "world"
c = a
a = b 
b = c
print(a,b)
# 法二：python可直接这样操作
a,b = b,a
print(a,b)
```

## 回文及切片

```python
a = "山西运煤煤运西山"
b = a[::-1]#切片将a从后往前取 切片:[开始:结尾:步长]列表也可以采用这种方法！
if a==b:
    print(f"{a}是回文")
```

## 字符串的常用操作方法

### find

> 作用：查找元素位置
>
> 第一个参数：要查找的字符串片段
>
> 第二个参数：要查找的起始点
>
> 如果查找的字符串片段有多个则返回第一个的下标
>
> 找不到就返回-1

```python
a = "wdfuiewcuhwfwwdw"
print(a.find("w",2,7))
```

### count

> 统计字符串片段在字符串中出现的次数
>
> 找不到返回零
>
> 参数和find同

```python
a = "wdfuiewcuhwfwwdw"
print(a.count("w",2,7))
```

### replace

> 作用：替换指定的字符串片段
>
> 参数一：要替换的字符串片段
>
> 参数二：替换之后的字符串片段
>
> 参数三：替换的次数，从前往后替换(默认替换所有的)

```python
a = "wdfuiewcuhwfwwdw"
print(a.replace("w","c",2))
```

### upper()&lower()

==字符串转大写和小写的方法==

### split&strip

#### split

==分割字符串的方法==

```python
a = "fwefc,12,123,dew,12w,wdc"
print(a.split(","))#有逗号的地方进行分割得到列表,后面的数字表示切几刀，默认全切
```

#### strip

==去除字符串首尾空格（中间的空格去不掉）==

### len()

==统计字符串/列表长度==

## 列表的常用操作方法

### del

```python
a = [1,2,1]
del a #可以删除整个列表
del a[1]#也可以删除列表中的某个元素
```

### append

==为列表添加元素,一次性全部塞进去==

### insert

> 作用：向指定位置插入元素
>
> 第一个参数：插入的位置
>
> 第二个参数：插入的内容

```python
li = [1,2,3,4]
li.insert(2,9)
print(li)
```

### clear

==清除列表中的数据==

### remove

* ==有重复元素时只移除第一个==
* 参数为元素

### pop

+ 默认移除最后一个
+ 参数为下标

### index

* 第一个参数为元素
* 第二，三个参数为起始和结束位置
* 作用：获取元素下标

### reverse

==作用：逆向排序==

```python
a = ["py","c","go"]
a.reverse()
print(a)
```

### extend

* 在原列表下追加数据
* 注意：extend函数和列表的加法的结果是一样的，但是extend函数会将另一个列表并入当前列表(不会占用新的内存空间)，而加法是返回新的列表(会占用新的内存空间)

```python
a = [1,2,3]
a.extend([4,5,6])
print(a)
```

### sort

* 用于将列表进行排序

* 根据ASCII码的大小规则/数字大小进行排序

* 同类型的数据才能进行排序

  ```python
  a = [7,8,3,5]
  a.sort(reverse=True)#将a逆向排序
  print(a)
  ```

  

### count

```python
a = [1,2,3,4,7,2,2,2]
num = a.count(2)
print(num)
```

## 元组

* len
* max/min   #根据ASCII码表找出最大和最小
* ==元组里面只有一条数据的时候必须在后面加一个`,`例如：元组`c = (10,)`
* 数据不可变

## 集合

* 大括号声明时，不能直接放入列表和字典

* 可用于列表/元组/字典键的去重

  ```python
  a = [1,1,2,2,3,3]
  a = list(set(a))
  print(a)#实现列表去重
  ```

  ### 方法

  #### add

  ==作用：添加元素==

  #### update

  ==作用：将集合合并==

  ```python
  a = {1,2,3,4,5}
  b = {"g","c","h"}
  a.add(8)
  a.update(b)
  print(a)
  ```

  #### remove

  > 作用：删除集合中的元素，如果有直接删除，没有会报错

  #### pop

  > 作用：随机删除集合中的元素，如果集合中没有元素会报错

#### discard

> 作用：删除集合中的元素，如果有直接删除，没有不会做任何操作

### 交并集

```python
s1 = {1,2,3,5}
s2 = {12,2,3,1}
s3 = s1 & s2#取交集
s4 = s1 | s2#取并集
print(s3,s4)
```

## 字典

### 增删改查

```python
dic = {"名字":"织梦","年龄":18}#定义字典
dic["技能"] = "python"#增
del dic["名字"]#删
dic["名字"] = "zz"#改
print(dic["名字"])#查
```

### get&keys

```py
dic = {"名字":"织梦","年龄":18}#定义字典
print(dic.get("名字"))#获取指定键的值
print(dic.keys())#获取所有键
```

### items&values

```python
dic = {"名字":"织梦","年龄":18}#定义字典
print(dic.items())#获取所有键值对,对字典遍历的时候会用到这种方法
print(dic.values())#获取所有值
```

### clear&copy

* clear：清空字典

* copy：复制字典

  

### pop&popitem

```python
dic = {"名字":"织梦","年龄":18}#定义字典
r = dic.pop("名字")#移除指定键，返回值为值
print(r,dic)
d = dic.popitem()#删除字典中最后一项，并以元组的形式返回该项所对应的键和值
```

### setdefault

```python
dic = {"名字":"织梦","年龄":18}#定义字典
dic.setdefault("名字","python")#键无则增，有键则忽略
print(dic)
```

### update

```python
dic = {"名字":"织梦","年龄":18}#定义字典
dic2 = {"名字":"知梦","擅长":"python"}
dic.update(dic2)#原字典有相应键则改，无则增
print(dic)
```

## 判断

### in&not in

* 判段字符是否在字符串/元组/列表/字典中
* 判断是否在字典中时只能判断相应键是否在字典中

```python
dic = {"名字":"织梦","年龄":18}
print("名字"in dic)
```

### is&is not

> * 数字/字符串/元组都是不可变的数据类型，若表面一样，则完全一样
> * 列表/字典/集合都是可变的数据类型，若表面一样，其实不是同一个对象

### 提取嵌套列表中的元素

```python
a = [1,2,3,[4,5,6],[7,8,9]]
for i in a:
    if isinstance(i,list):
        for x in i:
            print(x)
```

## 函数相关

### 可变参数

* `*args`和`**kwargs`类型分别为元组和字典

  ```python
  def test(*args,**kwargs):
      print(args,kwargs)
  test(12,x=123)
  ```

  

### 解包

```python
def test(*args):
	print(args)
test(*(1,2,3))#解包
a,b,c = (1,2,3)#元组的解包
```

### 参数顺序

```python
def test(a,name="小杰",*args,**kwargs):
    pass
```

### 内置函数

#### del

* del删除的是变量

* del语句作用在变量上，而不是数据对象上。

#### print

1. 可指定file=f，输出到文件里

2. sep = ‘-’,以‘-分割’

   ```python
   f = open('test.txt',mode='w')
   print('a','b','c',sep='-',file=f)
   ```

   

#### isinstance

1. isinstance(object,class)
2. 返回值是bool值

#### range()

1. 返回一个整数序列的可迭代对象

#### len()

内置函数与对象的成员方法/函数

```python
str = 'abc'
print('')
```



## 程序编码规范

