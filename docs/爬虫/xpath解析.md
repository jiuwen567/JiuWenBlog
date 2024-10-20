# Xpath解析

## xpath表达式

### 需要（pip install ==lxml==）库

> xpath表达式是用来获取目标html节点下的指定资源的定位语法，xpath表达式主要由路径表达式+谓语+通配符

###  路径表达式

| //   | 从当前节点选取子孙节点 |
| :--- | ---------------------: |
| /    |   从当前节点选取子节点 |
| .    |           选取当前结点 |
| …    |   选取当前节点的父节点 |
| @    |               选取属性 |

### 谓语

> 获取从指定排名的兄弟节点或者指定属性的节点（需要与@通配符一起使用）

| [order]        | 兄弟节点索引                          |
| -------------- | ------------------------------------- |
| [last()]       | 最后一个兄弟节点                      |
| [last()-order] | 倒数第几个兄弟节点order为自定义的数字 |
| [@class="dxd"] | 指定class属性为dxd的节点              |

### 通配符

| @      | 获取节点下的属性值 |
| ------ | ------------------ |
| @href  | 获取图片链接       |
| text() | 获取节点的文字内容 |

### 引用

```python
from lxml import etree#加载xpath第三方库
```

### 遇到tbody的情况如何处理:

这是网页的规范性问题，可以直接跳过，我们定位路径的时候可以==直接忽略==这个点

### 总结

==//==表示所有位置

==*==表示所有元素

文本值：//*[text()=‘文本值’]

contains:模糊查询    //*[contains(@herf,’baidu’)]

starts-with():以xxx开始==适用id变化==

### 实战--搜房网--拿到每个省份及城市和城市链接

> [](https://esf.fang.com/newsecond/esfcities.aspx)

```python
import requests
from lxml import etree
url = "https://esf.fang.com/newsecond/esfcities.aspx"
res = requests.get(url=url)
html = etree.HTML(res.text)# xpath解析的对象是html节点===》字符串的响应报文转化为html对象
details = html.xpath('.//*[@class="outCont"]/*/*')#拿到每一个li节点
items = []
for everyli in details:
    province = everyli.xpath("./strong/text()")
    city =everyli.xpath("./a/text()")
    cityUrl = everyli.xpath("./a/@href")
    item = {
            'province':province,
            'city':city,
            'cityUrl':cityUrl
        }
    items.append(item)
items
```

### 实战--北京新房房源--相关信息

```python
import requests
from lxml import etree
url = "https://newhouse.fang.com/house/s/?from=db"
res = requests.get(url=url)
html = etree.HTML(res.text)
details = html.xpath('.//*[@class="nl_con clearfix"]/*/*')
items = [] 
for li in details:
    house_name = li.xpath('.//*[@class="nlcd_name"]/a/text()')
    house_url = li.xpath('.//*[@class="nlcd_name"]/a/@href')
    house_type = li.xpath('.//*[@class="house_type clearfix"]/a/text()')#.//*[@class="nl_con clearfix"]/*/*//*[@class="house_type clearfix"]/a/text()
    house_area = li.xpath('.//*[@class="address"]/a/text()')#.//*[@class="nl_con clearfix"]/*/*//*[@class="address"]/a/text()
    housex_price = li.xpath('.//*[@class="nhouse_price"]//text()')#.//*[@class="nl_con clearfix"]/*/*//*[@class="nhouse_price"]//text()
    house_price = [x.strip() for x in housex_price if x.strip()!='']
    phone = li.xpath('.//*[@class="tel"]//text()')#.//*[@class="nl_con clearfix"]/*/*//*[@class="tel"]//text()
    phone_change = [x.strip() for x in phone if x.strip()!='']#如果不加if则列表中会得到空元素
    item ={
        "house_name":house_name[0].strip("\n\t"),
        "house_url":house_url[0],
        "house_type":house_type,
        "house_price":house_price,
        "phone":phone_change
    }
    items.append(item)
items
```

### 小tip--删除列表中的空元素，\n \t \r元素

* ```python
  list_eg = ['',' ','hello','\n','world','\t']
  print(list_eg)
  ```

* 输出如下

* ```python
  ['', ' ', 'hello', '\n', 'world', '\t']
  ```

* 加上列表推导式后

  ```python
  list_eg = ['',' ','hello','\n','world','\t']
  list_eg_change = [x.strip() for x in list_eg if x.strip()!='']
  print(list_eg_change)
  ```

  + 输出如下

  + ```python
    ['hello', 'world']
    ```
  
  + 列表推导式解释如下

  + ```python
    list_eg = ['',' ','hello','\n','world','\t']
    list_eg_change = []
    for i in list_eg:
        if i.strip() !='':
            i = i.strip()
            list_eg_change.append(i)
    print(list_eg_change)
    ```
  
  + 步骤是：
    1、遍历列表`list_eg`，每个元素进行 `i.strip()` 删除字符左右的空格。
    2、如果`i.strip()` 不等于空值，则将`i.strip()`赋值给`i`。
    3、列表`list_eg_change.append()`得到想要的数据。
  
  列表推导式的语法格式如下：

  ```python
  [表达式 for 迭代变量 in 可迭代对象 [if 条件表达式] ]#此格式中，[if 条件表达式] 不是必须的，可以使用，也可以省略。
  ```
  
  

