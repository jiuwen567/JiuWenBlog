# selenium

## 简介

- selenium
  - 是一种浏览器自动化的工具，所谓的自动化是指，我们可以通过代码的形式制定一系列的行为动作，然后执行代码，这些动作就会同步触发在浏览器中
  
  - 便捷获取网站中动态加载的数据，模拟登录
  
  - 基于浏览器自动化的一个模块
  
  - *好处：*
  
    *可以节约时间节约脑力，不需要花时间去找到真正的网址*
  
    * 坏处：效率低下

## 下载驱动

> 驱动路径：https://registry.npmmirror.com/binary.html?path=chromedriver/
>
> 将驱动复制到谷歌安装路径
>
> ![image-20230220154125510](https://typora567.oss-cn-chengdu.aliyuncs.com/temp_picture/image-20230220154125510.png)

* chrome://version/查看谷歌版本等相关信息
* 注意以下信息
* ![image-20230220153551322](https://typora567.oss-cn-chengdu.aliyuncs.com/temp_picture/image-20230220153551322.png)

* 谷歌浏览器添加至环境变量

## python操作selenium

1. `pip install selenium==4.2.0`—> selenium中的webdriver存在被识别的指纹
2. 用undetected_chromedriver代替selenium解决浏览器打不开网页`pip install undetected_chromedriver`–->参考[(24条消息) 用undetected_chromedriver代替selenium解决浏览器打不开网页_Scott0902的博客-CSDN博客](https://blog.csdn.net/Scott0902/article/details/127024380)
3. *文档：*

   *https://selenium-python-zh.readthedocs.io/en/latest/*

4. [基于Python的Selenium详细教程_selenium python_Smile丶Life丶的博客-CSDN博客](https://blog.csdn.net/qq_43125235/article/details/125601564)

### driver的配置文件

```py
import undetected_chromedriver as webdriver#加载驱动
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50'
}
url = "http://http.tiqu.letecs.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&pack=276876&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"
ip = requests.get(url=url,headers=headers).text
ip = ip.strip('\r\n')
ip
# 加载谷歌配置项目
option = webdriver.ChromeOptions()
# 配置项1：代理
option.add_argument(f'--proxy-server={ip}')
# 配置项2：缓存目录(手动打开的浏览器需要关闭)此项配置利于保存缓存信息如登录请求等
option.add_argument(r'--user-data-dir=C:\Users\SOIDE\AppData\Local\Google\Chrome\User Data')#不需要default,记得取消转义，
# option.add_argument('--profile-directory=default')
driver = webdriver.Chrome(options=option)
driver.get('https://www.douban.com/')
```

### **浏览器创建**

- Selenium支持非常多的浏览器，如Chrome、Firefox、Edge等.另外，也支持无界面浏览器。

- ```python
  from selenium import webdriver
    
  browser = webdriver.Chrome()
  browser = webdriver.Firefox()
  browser = webdriver.Edge()
  browser = webdriver.PhantomJS()
  browser = webdriver.Safari()
  ```

### **元素定位**

- webdriver 提供了一系列的元素定位方法，常用的有以下几种：
- ·from selenium.webdriver.common.by import By
- 元素定位方法包含了2个系列：
  - `find_element()`系列：用于定位单个的页面元素。
  - `find_elements()`系列：用于定位一组页面元素，获取到的是一组列表。

#### 1、通过标签`id`属性定位

- `find_element(By.ID,'XX')`id定位，根据元素的id属性值定位，最为方便且唯一，但有可能不存在，也可能动态生成。

- ```python
  import time
  # 导入selenium包
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  # 打开指定（Firefox）浏览器
  browser = webdriver.Firefox()
  # 指定加载页面
  browser.get("http://www.csdn.net")
  # 通过id属性获取搜索输入框
  input_text = browser.find_element(By.ID, "toolbar-search-input")
  # 向搜索输入框内输入selenium
  input_text.send_keys("selenium")
  # 设置停留五秒后执行下一步
  time.sleep(5)
  # 关闭浏览器
  browser.quit()### 2、通过标签`name`属性定位
  ```

  - `find_element(By.NAME,'xx')`name定位，根据元素的name属性值定位，定位到的标签不一定是唯一的。

#### 2、通过标签`name`属性定位

- `find_element(By.NAME,'xx')`name定位，根据元素的name属性值定位，定位到的标签不一定是唯一的。

- ```python
  import time
  # 导入selenium包
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  # 启动并打开指定页面
  browser = webdriver.Firefox()
  browser.get("http://www.baidu.com/")
  # 通过name属性选择文本框元素，并设置内容
  browser.find_element(By.NAME,'wd').send_keys("selenium")
  # 通过通过ID属性获取“百度一下”按钮，并执行点击操作
  browser.find_element(By.ID,"su").click()
  # 停留五秒后关闭浏览器
  time.sleep(5)
  browser.quit()
  ```

#### 3、通过标签`class`属性定位

- `find_element_by(By.CLASS_NAME,'xx')`class定位，根据元素的class属性值定位，但可能受JS影响动态变化。定位到的标签不一定是唯一的。

#### 4、通过标签`tag`定位

- `find_element(By.TAG_NAME,'xx')`tag name定位，根据元素的标签名定位，定位到的标签不一定是唯一的。

##### 5、通过link定位

* link表示包含有属性href的标签元素，如:<a href="https://www.csdn.net">linktext</a>可以通过LINK＿TEXT进行定位。
  find_element(By.LINK_TEXT,'XX')根据链接文本全匹配进行精确定位。
  find_element(By.PARTIAL_LINK_TEXT,'XX')根据链接文本模糊匹配进行定位。

  1. `By.LINK_TEXT`精确定位

     ```python
     import time
     # 导入selenium包
     from selenium import webdriver
     from selenium.webdriver.common.by import By
     # 启动并打开指定页面
     browser = webdriver.Firefox()
     browser.get("http://www.csdn.net")
     # 选择<a href="https://blog.csdn.net/nav/back-end">Python</a>标签,执行点击操作
     browser.find_element(By.LINK_TEXT, "Python").click()
     # 停留三秒后关闭浏览器
     time.sleep(3)
     browser.quit()
     ```

     

2. `By.PARTIAL_LINK_TEXT`模糊定位

   ```python
   import time
   # 导入selenium包
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   # 启动并打开指定页面
   browser = webdriver.Firefox()
   browser.get("http://www.csdn.net")
   # 选择<a href="href="https://blog.csdn.net/nav/ai">人工智能</a>标签,执行点击操作
   browser.find_element(By.PARTIAL_LINK_TEXT, "人工").click()
   # 停留五秒后关闭浏览器
   time.sleep(3)
   browser.quit()
   ```

### 节点交互

- Selenium可以驱动浏览器来执行一些操作，也就是说可以让浏览器模拟执行一些动作。比较常见的用法有：输入文字时用`send_keys()`方法，清空文字时用`clear()`方法，点击按钮时用`click()`方法。

### 执行js

对于某些操作，Selenium API并没有提供。比如，下拉进度条，它可以直接模拟运行JavaScript，此时使用`execute_script()`方法即可实现。

```python
from selenium import webdriver
from time import sleep
#1.创建一个浏览器对象,executable_path指定当前浏览器的驱动程序
#注意：我当前是mac系统，驱动程序也是mac版本的，如果是window系统注意更换驱动
bro = webdriver.Chrome(executable_path='./chromedriver')
#2.浏览器的请求发送
bro.get('https://www.jd.com/')
#3.标签定位:调用find系列的函数进行标签定位
search_box = bro.find_element_by_xpath('//*[@id="key"]')
#4.节点交互
search_box.send_keys('mac pro m1')#向指定标签中录入内容
sleep(2)
btn = bro.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn.click() #点击按钮
sleep(2)
#js注入
bro.execute_script('document.documentElement.scrollTo(0,2000)')
sleep(5)
#关闭浏览器
bro.quit()
```

- 思考：在爬虫中为什么需要使用selenium？selenium和爬虫之间的关联是什么？

  - 便捷的爬取动态加载数据（可见即可得）

    - ```python
      #获取前5页的企业名称
      from selenium import webdriver
      import time
      from lxml import etree
      
      bro = webdriver.Chrome(executable_path='./chromedriver')
      url = 'http://scxk.nmpa.gov.cn:81/xk/'
      bro.get(url=url)
      time.sleep(1)
      #获取页面源码数据(page_source)
      page_text = bro.page_source
      #将前5页的页面源码数据存储到该列表中
      all_page_text_list = [page_text]
      for i in range(4):
          #点击下一页
          next_page_btn = bro.find_element_by_xpath('//*[@id="pageIto_next"]')
          next_page_btn.click()
          time.sleep(1)
          all_page_text_list.append(bro.page_source)
      
      for page_text in all_page_text_list:
          #解析数据
          tree = etree.HTML(page_text)
          li_list = tree.xpath('//*[@id="gzlist"]/li')
          for li in li_list:
              title = li.xpath('./dl/@title')[0]
              print(title)
      
      time.sleep(2)
      bro.quit()
      ```

  - 便捷实现模拟登录

    - 后面在说

### 获取页面源码数据

通过`page_source`属性可以获取网页的源代码，接着就可以使用解析库（如正则表达式、Beautiful Soup、pyquery等）来提取信息了。

### 前进和后退

```python
#模拟浏览器的前进后退
from selenium import webdriver
import time

browser = webdriver.Chrome(r'./chromedriver')
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')

browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)

browser.close()
```

## iframe处理以及动作链的使用

* iframe表示的子页面中，包含子html
* ![image-20230912210653972](https://typora567.oss-cn-chengdu.aliyuncs.com/temp_picture/image-20230912210653972.png)

* 一些交互动作是针对某个节点执行的。比如，对于输入框，我们就调用它的输入文字和清空文字方法；对于按钮，就调用它的点击方法。其实，还有另外一些操作，它们没有特定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。动作链【拖动】使用场景：网页用户登录时的滑块验证（也是一种验证方式）

* ```python
  selenium处理iframe　
  
  　　- 如果定位的标签存在于iframe标签之中，则必须使用switch_to.frame(id)
  　　- 动作链（拖动）：from selenium.webdriver import ActionChains
  　　- 实例化一个动作链对象：action = ActionChains(bro)
  　　- click_and_hold（div）：长按且点击操作
  　　- move_by_offset(x,y)
  　　- perform()让动作链立即执行
  　　- action.release()释放动作链对象
  ```

```python
from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
sleep(1)
#注意：如果定位的标签是存在于iframe表示的子页面中，则常规的标签定位报错
#处理：使用如下指定操作
bro.switch_to.frame('iframeResult')
div_tag = bro.find_element_by_id('draggable')

#实例化一个动作链对象且将该对象绑定到指定的浏览器中
action = ActionChains(bro)
action.click_and_hold(div_tag) #对指定标签实现点击且长按操作
for i in range(5):
    action.move_by_offset(10,10).perform() #perform让动作链立即执行
    sleep(0.5)
sleep(3)
action.release()
bro.quit()
```

### ==qq空间模拟登录==

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
bro = webdriver.Chrome()
bro.get('https://qzone.qq.com/')
sleep(1)
#注意：如果定位的标签是存在于iframe表示的子页面中，则常规的标签定位报错
#处理：使用如下指定操作
bro.switch_to.frame('login_frame')
mima_login = bro.find_element(by=By.ID,value='switcher_plogin')
mima_login.click()
user = bro.find_element(by=By.ID,value='u')
pwd = bro.find_element(by=By.ID,value='p')
user.send_keys('xxx')
sleep(1)
pwd.send_keys('xxx')
sleep(1)
button = bro.find_element(by=By.ID,value='login_button')
button.click()
bro.quit()
```

## Google无头浏览器+规避检测selenium

* 无头浏览器：

```python
from selenium.webdriver.chrome.options import Options
option = Options()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
bro = webdriver.Chrome('./chromedriver.exe', options=option)
```

* 规避检测：

  ```python
  from selenium.webdriver import ChromeOptions
  chrome_options = ChromeOptions()
  chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
  ```

  
