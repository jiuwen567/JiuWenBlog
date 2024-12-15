## Unittest框架

Unittest框架是一个单元测试框架，最初是由JUnit启发而设计的模块，而开发的一款Python语言的单元测试框架。

https://docs.python.org/3.6/library/unittest.html

作用：

* 管理测试用例
* 断言
* 生成测试报告

###  Unittest框架的组成部分

Unittest框架主要由4个部分组成：test fixture、test case、test suite、test runner

| Unittest组成部分 | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| test fixture     | 测试固定组件，unittest框架中，一些有固定用法的组件           |
| test case        | 测试用例，被执行测试的最小单元                               |
| test suite       | 测试套件，它是一个用例集，用来汇总应该一起执行的测试用例。   |
| test runner      | 测试运行器，它是一个设计测试执行方式的元件，主要对用户提供了输出结果的展现方式。它可以用图标、文本、html等方式来展现测试结果 |

各个组成部分的运行逻辑关系：

![1618295049537](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/1618295049537.png)

注意：TestFixture是融合在代码中运行的，主要是体现在TestCase当中。TestResult是指测试结果

### Unittest框架入门案例

unittest在python3中，已经改为python内置模块，无需安装就能使用

#### 示例代码

```python
import unittest  # 导包

class UnittestDemo(unittest.TestCase):
    def test01(self):
        print("执行测试用例1")

    def test02(self):
        print("执行测试用例2")

if __name__ == '__main__':
    unittest.main()
```

### TestCase

TestCase就是Unittest框架执行的测试用例。

主要用法是，把测试用例编写在继承了TestCase的类中，通过unittest.main()来自动加载测试用例运行

#### 示例代码

```text
import unittest  # 导包

class UnittestDemo(unittest.TestCase):
    def test01(self):
        print("执行测试用例1")

    def test02(self):
        print("执行测试用例2")
        
    def test03(self):
        print("执行测试用例3")    

if __name__ == '__main__':
    unittest.main()
```

两种执行方式：

* Pycharm内置的unittest模式运行，可在此处选择使用哪种测试框架。

![image-20241119092217733](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20241119092217733.png)

* unittest.main()运行

  需要配置，才能进行

无论哪种方式，本质上都是运行unittest.main()中的代码



- unittest.main() 使用unittest框架运行测试用例
- 运行的是main.py的代码，其中自动将编写的测试用例加载到TestSuite、TestRunner和自动运行编写的test01和test02用例

注意事项：

- 每个测试用例默认都以test开头，非test开头的测试用例不会自动被执行

  ```text
  def test01(self):
          print("执行测试用例1")
  ```

- 测试用例的执行顺序是按照ASCII码的顺序运行，ASCII值越小，越优先执行

  ![image-20241119092549942](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20241119092549942.png)

  ```text
      def test01(self):
          print("执行测试用例1")
  
      def test02(self):
          print("执行测试用例2")
         
       # 先运行test01，再运行test02
  ```

- 只有继承了unittest.TestCase的类，才会被unttest.main()运行

#### 跳过要执行的测试用例

当我们希望跳过一些测试测试用例，不执行时，我们可以使用装饰器@unitest.skip("备注")来完成

示例代码：

```text
import unittest  # 导包


class XXX(unittest.TestCase):
    def test01(self):
        print("执行测试用例1")

    @unittest.skip("demonstrating skipping")
    def test02(self):
        print("执行测试用例2")

    def test03(self):
        print("执行测试用例3")

if __name__ == '__main__':
    unittest.main()
```

![image-20241119092754400](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20241119092754400.png)

###  引入TestFixture

TestFixture一般都是写在运行的测试用例的类中，作用该类的类方法或者实例方法而存在

####  TestFixture介绍

TestFixture一般使用4个常见方法：setUp()、tearDown()、setUpClass()、tearDownClass()

需要注意的是，在代码中，大小写严格区分。

代码编写方法：

```text
class TestFixtureDemo(unittest.TestCase):
    def setUp(self):
        pass
    
    @classmethod
    def setUpClass(self):
        pass
        
    def tearDown(self):
        pass
        
    @classmethod
    def tearDownClass(self):
        pass
    
    def testXX(self):
        pass
        
    # 注意，这些方法都是重写的TestCase中的方法
```

#### 运行规则和应用场景

* setUp()

  每运行一个测试用例之前，先运行的函数；主要用于设置一些配置信息，静态属性等等

* setUpClass()

  它是类方法，必须和@classmethod装饰器结合使用（unittest设计如此）

  实例化类后，会自动运行的方法，主要用于实例化类、设置某些环境配置如数据库连接配置等等。

* tearDown()

  每运行完一个测试用例之后，后运行的函数；主要用于销毁每个测试用例之间的数据，释放资源，还原数据

* tearDownClass()

  类中的代码全部运行完成后，会自动运行的方法，主要用于销毁类级别的资源，还原数据。

```txt
类方法：被@classmethod装饰的方法被称为类方法。
类方法不需要实例化就能使用。
例如：
class A:
    @classmethod
    def add(x,y):
        print(x+y)
    
    def add22(x, y):
        print(x + y)

A.add(1,2) #返回3
A.add22(1,2) # 报错
A().add22(1,2) # 返回3
```

####  TestFixture使用案例

```
import unittest


class MathDemo:

    def plus(self, x, y):
        return x + y


class TestFixtureDemo(unittest.TestCase):
    add = None

    def setUp(self):
        self.x = 1
        self.y = 1

    @classmethod
    def setUpClass(cls):
        cls.add = MathDemo()

    def tearDown(self):
        del self.x
        del self.y

    @classmethod
    def tearDownClass(cls):
        del cls.add

    def test01(self):
        result = self.add.plus(1, 2)
        print(result)

    def test02(self):
        result = self.add.plus(3, 5)
        print(result)


if __name__ == '__main__':
    unittest.main()
```

###  Unittest的断言

断言是让程序帮助人来判断，实际结果与预期结果的一种方法。

进行自动化测试中，只能通过断言来判断执行结果是否正确。所以，掌握断言技术是进行自动化测试的前提条件。

Python语言自带断言，但是应用时，会有许多不方便理解的地方。为了让我们能更方便的断言数据，Unittest对Python的断言进行了多层封装，使断言更丰富，更容易使用。

#### Unittest常见断言方法和作用

| Unittest断言方法      | 作用                               |
| --------------------- | ---------------------------------- |
| assertEqual(a,b)      | 检查 a和b是否相等                  |
| assertTrue(x)         | 检查x是不是一个True                |
| assertIs(a,b)         | 检查a和b是不是完全一样             |
| assertIsNone(x)       | 检查x是不是一个None                |
| assertIn(a,b)         | 检查a是不是b的子集                 |
| assertIsInstance(a,b) | 检查a、b两个对象，实例类型是否相同 |
|                       |                                    |

#### 案例演示

```
import unittest


class TestAssertDemo(unittest.TestCase):
    def setUp(self):
        self.l1, self.l2 = [1, 2], [1, 2]
        self.a, self.b = 1, 1

    def test01_assertEqual(self):
        self.assertEqual(self.a, self.b) # a和b相等

    def test02_assertIs(self):
        self.assertIs(self.l1, self.l2) # l1和l2不相同
        self.assertIs(self.a, self.b) # a和b相同

    def test03_assertTrue(self):
        self.assertTrue(self.a) # 1 是true
        self.assertTrue(0) # 0 是false

    def test04_assertIsNone(self):
        self.assertIsNone(self.b) # 1 不是 None
        self.assertIsNone(None)  # None 是 None

    def test05_assertIn(self):
        self.assertIn(self.l1, self.l2) # l1  不是l2的子集

    def test06_assertIsInstance(self):
        self.assertIsInstance(self.a, int) # a是int整型
        self.assertIsInstance(self.l1, list) # l1是list列表型


if __name__ == '__main__':
    unittest.main()

```

### TestSuite和TestRunner

Unittest中，主要使用TestSuite来管理测试用例，使用TestRunner运行测试用例，并生成测试报告

此前，运行unittest框架中的代码中，我们使用的都是默认的方式，自动加载用例然后运行得到结果

有没有一种方法，让我们可以自定义运行呢？当然有！

我们可以使用TestSuite添加测试用例到测试套件，然后用TestRunner来运行

####  TestSuite和TestRunner基本用法

```text
# 导包
import unittest

# 创建测试用例的类
class TestSuiteDemo1(unittest.TestCase):

    def test01(self):
        print("测试用例：aaaa")

    def test02(self):
        print("测试用例：bbbb")


class TestSuiteDemo2(unittest.TestCase):

    def test01(self):
        print("测试用例：奥特曼")

    def test02(self):
        print("测试用例：光头强")


if __name__ == '__main__':
    # 实例化测试套件
    suite = unittest.TestSuite()

    # 添加测试用例到测试套件当中
    suite.addTest(TestSuiteDemo1('test01'))

    # 实例化test_runner
    runner = unittest.TextTestRunner()

    # 使用runner运行测试套件
    runner.run(suite)
```

#### TestSuite添加测试用例的3种方式

添加测试用例到测试套件时，我们可以使用

suite.addTest、suite.addTests、TestLoader来添加

* suite.addTest

  添加单个测试用例，一般添加以test开头的函数

* suite.addTests，添加多个测试用例

  ```
  import sys
  import unittest
  
  
  def testXX(aa):
      print("编外的测试用例")
  
  
  class TestSuiteDemo1(unittest.TestCase):
  
      def test01(self):
          print("执行测试用例aaaa")
  
      def test02(self):
          print("执行测试用例bbbb")
  
  
  class TestSuiteDemo2(unittest.TestCase):
  
      def test01(self):
          print("执行测试用例xxxx")
  
      def test02(self):
          print("执行测试用例yyyy")
  
  
  if __name__ == '__main__':
      suite = unittest.TestSuite()  # 实例化测试套件
      suite.addTest(TestSuiteDemo1('test01'))  # 添加测试用例
      suite.addTests([ TestSuiteDemo2('test01'), TestSuiteDemo2('test02')])
      runner = unittest.runner.TextTestRunner()  # 实例化runner
      runner.run(suite)  # 使用runner执行测试套件
  
  ```

#### TestLoader加载测试用例

TestLoader添加测试用例的方法有很多种，这里我们主要介绍两种

第一种：TestLoader().discover(("./", "*.py")

根据执行的路径来寻找指定的py文件中的测试用例，加载到测试套件当中。

第二种：TestLoader().loadTestsFromTestCase(测试用例类名)

根据测试用例的类名来加载测试用例

示例代码：

```
import unittest

def testXX(aa):
    print("编外的测试用例")

class TestSuiteDemo1(unittest.TestCase):

    def test01(self):
        print("执行测试用例aaaa")

    def test02(self):
        print("执行测试用例bbbb")

class TestSuiteDemo2(unittest.TestCase):

    def test01(self):
        print("执行测试用例xxxx")

    def test02(self):
        print("执行测试用例yyyy")

class TestSuiteDemo3(unittest.TestCase):

    def test01(self):
        print("执行接口测试")

    def test02(self):
        print("执行单元测试")

    def test03(self):
        print("执行安全测试")

if __name__ == '__main__':
    t1 = unittest.TestLoader()
    suite = t1.discover("./", "*.py") # 使用discover来寻找测试用例
    # suite = t1.loadTestsFromTestCase(TestSuiteDemo3)
    runner = unittest.runner.TextTestRunner() # 实例化runner
    runner.run(suite) # 使用runner执行测试套件
```

###  测试报告TestResult

使用unittest运行测试用例之后，最后会生成测试报告，我们可以把测试报告保存到文件中

####  TextTestRunner生成的报告

```text
import unittest
class TestSuiteDemo1(unittest.TestCase):

    def test01(self):
        print("执行测试用例aaaa")

    def test02(self):
        print("执行测试用例bbbb")

class TestSuiteDemo2(unittest.TestCase):

    def test01(self):
        print("执行测试用例xxxx")

    def test02(self):
        print("执行测试用例yyyy")

class TestSuiteDemo3(unittest.TestCase):

    def test01(self):
        print("执行接口测试")

    def test02(self):
        print("执行单元测试")

    def test03(self):
        print("执行安全测试")

if __name__ == '__main__':
    t1 = unittest.TestLoader()
    # suite = t1.discover("./", "demo_testloader.py") # 使用discover来寻找测试用例
    suite = t1.loadTestsFromTestCase(TestSuiteDemo3)
    with open(file="./test_result.txt", mode='w') as f:
        runner = unittest.runner.TextTestRunner(f,descriptions=True, verbosity=2) # 实例化runner
        result = runner.run(suite) # 使用runner执行测试套件
    print(result)
```

#### HTMLTestRunner_PY3生成的报告

HTMLTestRunner_PY3是一个能生成HTML格式的，显示更友好的测试报告。

它不仅能够显示出测试用例的执行结果，还能跟踪测试用例执行失败的原因。

**安装HTMLTestRunner_PY**（目前官网下载不了）

下载下来放到Python的lib文件下

以下为源码：

```python
#coding=utf-8
__author__ = "Wai Yip Tung,  Findyou"
__version__ = "0.8.2.1"
import datetime
import io
import time
import unittest
from xml.sax import saxutils
import importlib
import sys
importlib.reload(sys)
class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """
    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()

stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)

# ----------------------------------------------------------------------
# Template

class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.
    Overall structure of an HTML report
    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
    0: '通过',
    1: '失败',
    2: '错误',
    }

    DEFAULT_TITLE = '接口测试报告'
    DEFAULT_DESCRIPTION = ''
    DEFAULT_TESTER='九问'

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    %(stylesheet)s
</head>
<body >
<script language="javascript" type="text/javascript">
output_list = Array();
/*level 调整增加只显示通过用例的分类 --Findyou
0:Summary //all hiddenRow
1:Failed  //pt hiddenRow, ft none
2:Pass    //pt none, ft hiddenRow
3:All     //pt none, ft none
4:Error  
*/
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level == 2 || level == 0 ) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level < 2 || level ==4) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
    }
    //加入【详细】切换文字变化 --Findyou
    detail_class=document.getElementsByClassName('detail');
    //console.log(detail_class.length)
    if (level == 3) {
        for (var i = 0; i < detail_class.length; i++){
            detail_class[i].innerHTML="收起"
        }
    }
    else{
            for (var i = 0; i < detail_class.length; i++){
            detail_class[i].innerHTML="详细"
        }
    }
}
function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        //ID修改 点 为 下划线 -Findyou
        tid0 = 't' + cid.substr(1) + '_' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        //修改点击无法收起的BUG，加入【详细】切换文字变化 --Findyou
        if (toHide) {
            document.getElementById(tid).className = 'hiddenRow';
            document.getElementById(cid).innerText = "详细"
        }
        else {
            document.getElementById(tid).className = '';
            document.getElementById(cid).innerText = "收起"
        }
    }
}
function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
</script>
%(heading)s
%(report)s
%(ending)s
</body>
</html>
"""
    # variables: (title, generator, stylesheet, heading, report, ending)


    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 80%; }
table       { font-size: 100%; }
/* -- heading ---------------------------------------------------------------------- */
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}
.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}
/* -- report ------------------------------------------------------------------------ */
#total_row  { font-weight: bold; }
.passCase   { color: #5cb85c; }
.failCase   { color: #d9534f; font-weight: bold; }
.errorCase  { color: #f0ad4e; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }
</style>
"""

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """<div class='heading'>
<h4 style="font-family: Microsoft YaHei">%(title)s</h4>
%(parameters)s
<p class='description'>%(description)s</p>
</div>
""" # variables: (title, parameters, description)

    HEADING_ATTRIBUTE_TMPL = """<p class='attribute'><strong>%(name)s : </strong> %(value)s</p>
""" # variables: (name, value)



    # ------------------------------------------------------------------------
    # Report
    #
    # 汉化,加美化效果 --Findyou
    REPORT_TMPL = """
<p id='show_detail_line'>
<a class="btn btn-primary" href='javascript:showCase(0)'>概要{ %(passrate)s }</a>
<a class="btn btn-warning" href='javascript:showCase(4)'>错误{ %(error)s }</a>
<a class="btn btn-danger" href='javascript:showCase(1)'>失败{ %(fail)s }</a>
<a class="btn btn-success" href='javascript:showCase(2)'>通过{ %(Pass)s }</a>
<a class="btn btn-info" href='javascript:showCase(3)'>所有{ %(count)s }</a>
</p>
<table id='result_table' class="table table-condensed table-bordered table-hover">
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
    <td>用例集/测试用例</td>
    <td>总计</td>
    <td>通过</td>
    <td>失败</td>
    <td>错误</td>
    <td>详细</td>
    <td>截图</td>
</tr>
%(test_list)s
<tr id='total_row' class="text-center active">
    <td>总计</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td>通过率：%(passrate)s</td>
    <td> <a href="" target="_blank"></a></td>
</tr>
</table>
""" # variables: (test_list, count, Pass, fail, error ,passrate)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s warning'>
    <td>%(desc)s</td>
    <td class="text-center">%(count)s</td>
    <td class="text-center">%(Pass)s</td>
    <td class="text-center">%(fail)s</td>
    <td class="text-center">%(error)s</td>
    <td class="text-center"><a href="javascript:showClassDetail('%(cid)s',%(count)s)" class="detail" id='%(cid)s'>详细</a></td>
    <td class="text-center">Assert or Error Image</td>
</tr>
""" # variables: (style, desc, count, Pass, fail, error, cid)

    #失败 的样式，去掉原来JS效果，美化展示效果  -Findyou
    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s' width='300px'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='left' width='600px'> <!--print 输出框位置-->
    <!--默认收起错误信息 -Findyou
    <button id='btn_%(tid)s' type="button"  class="btn btn-danger btn-xs collapsed" data-toggle="collapse" data-target='#div_%(tid)s'>%(status)s</button>
    <div id='div_%(tid)s' class="collapse">  -->
    <!-- 默认展开错误信息 -Findyou -->
    <button id='btn_%(tid)s' type="button"  class="btn btn-danger btn-xs" data-toggle="collapse" data-target='#div_%(tid)s'>%(status)s</button>
    <div id='div_%(tid)s' class="collapse in">
    <pre>
    %(script)s
    </pre>
    </div>
    </td>
    <td align="right">
        <a %(hidde)s href="%(image)s">
            <img   src="%(image)s" height="200" width="400"/>
        </a>
    </td>
</tr>


""" # variables: (tid, Class, style, desc, status)

    # 通过 的样式，加标签效果  -Findyou
    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'><span class="label label-success success">%(status)s</span></td>
    <td align="right">
        <a %(hidde)s href="%(image)s">
            <img   src="%(image)s" height="200" width="400"/>
        </a>
    </td>
</tr>
""" # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
""" # variables: (id, output)

    # ------------------------------------------------------------------------
    # ENDING
    #
    # 增加返回顶部按钮  --Findyou
    ENDING_TMPL = """<div id='ending'>&nbsp;</div>
    <div style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer">
    <a href="#"><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
    </span></a></div>
    """

# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult

class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []
        #增加一个测试通过率 --Findyou
        self.passrate=float(0)


    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector


    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()


    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()


    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')


class HTMLTestRunner(Template_mixin):
    """
    """
    def __init__(self, stream=sys.stdout, verbosity=1,title=None,description=None,tester=None):
        self.stream = stream
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description
        if tester is None:
            self.tester = self.DEFAULT_TESTER
        else:
            self.tester = tester

        self.startTime = datetime.datetime.now()


    def run(self, test):
        "Run the given test case or test suite."
        result = _TestResult(self.verbosity)
        test(result)
        self.stopTime = datetime.datetime.now()
        self.generateReport(test, result)
        print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime - self.startTime))
        return result


    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n,t,o,e in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n,t,o,e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    #替换测试结果status为通过率 --Findyou
    def getReportAttributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        status = []
        status.append('共 %s' % (result.success_count + result.failure_count + result.error_count))
        if result.success_count: status.append('通过 %s'    % result.success_count)
        if result.failure_count: status.append('失败 %s' % result.failure_count)
        if result.error_count:   status.append('错误 %s'   % result.error_count  )
        if status:
            status = '，'.join(status)
            self.passrate = str("%.2f%%" % (float(result.success_count) / float(result.success_count + result.failure_count + result.error_count) * 100))
        else:
            status = 'none'
        return [
            (u'测试人员', self.tester),
            (u'开始时间',startTime),
            (u'合计耗时',duration),
            (u'测试结果',status + "，通过率= "+self.passrate),
        ]


    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        generator = 'HTMLTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        output = self.HTML_TMPL % dict(
            title = saxutils.escape(self.title),
            generator = generator,
            stylesheet = stylesheet,
            heading = heading,
            report = report,
            ending = ending,
        )
        self.stream.write(output.encode('utf8'))


    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    #增加Tester显示 -Findyou
    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            line = self.HEADING_ATTRIBUTE_TMPL % dict(
                    name = saxutils.escape(name),
                    value = saxutils.escape(value),
                )
            a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title = saxutils.escape(self.title),
            parameters = ''.join(a_lines),
            description = saxutils.escape(self.description),
            tester= saxutils.escape(self.tester),
        )
        return heading

    #生成报告  --Findyou添加注释
    def _generate_report(self, result):
        rows = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = nf = ne = 0
            for n,t,o,e in cls_results:
                if n == 0: np += 1
                elif n == 1: nf += 1
                else: ne += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style = ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                desc = desc,
                count = np+nf+ne,
                Pass = np,
                fail = nf,
                error = ne,
                cid = 'c%s' % (cid+1),
            )
            rows.append(row)

            for tid, (n,t,o,e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = self.REPORT_TMPL % dict(
            test_list = ''.join(rows),
            count = str(result.success_count+result.failure_count+result.error_count),
            Pass = str(result.success_count),
            fail = str(result.failure_count),
            error = str(result.error_count),
            passrate =self.passrate,
        )
        return report


    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        # ID修改点为下划线,支持Bootstrap折叠展开特效 - Findyou
        tid = (n == 0 and 'p' or 'f') + 't%s_%s' % (cid+1,tid+1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        # utf-8 支持中文 - Findyou
         # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            # uo = o.decode('latin-1')
            uo = e
        else:
            uo = o
        if isinstance(e, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            # ue = e.decode('latin-1')
            ue = o
        else:
            ue = o

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id = tid,
            output = saxutils.escape(uo+ue),
        )
        # 插入图片
        unum = str(uo+ue).find('screenshot:')
        if unum != -1:
            hidde_status = ''
            unum=str(uo+ue).find('screenshot:')
            print(str(uo+ue))
            image_url = '../images/'+str(uo+ue)[unum+11:unum+34].replace(' ','')

        else:
            hidde_status = '''hidden="hidden"'''
            image_url = ''

        row = tmpl % dict(
            tid = tid,
            Class = (n == 0 and 'hiddenRow' or 'none'),
            style = n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'passCase'),
            desc = desc,
            script = script,
            hidde=hidde_status,
            image=image_url,
            status = self.STATUS[n],
        )
        rows.append(row)
        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """
    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)

main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
```

使用HTMLTestRunner

```python
import unittest
from HTMLTestRunner import HTMLTestRunner


# 定义测试类
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)


# 创建测试套件
suite = unittest.TestSuite()
suite.addTest(MyTestCase("test_addition"))
suite.addTest(MyTestCase("test_subtraction"))
with open('test.html',mode='wb') as f:
    # 创建测试运行器
    runner = HTMLTestRunner(title="测试", verbosity=2,stream=f)
    # 运行测试套件
    runner.run(suite)

```

## 多线程执行测试用例实战

###  案例

场景：现在假设有六百六十六个测试用例，每个用例至少需要执行1秒，如果是单线程执行，则需要花费666秒。

需求：使用十个线程执行六百六十六个用例



实现分析：我们可以使用线程池来完成。

代码：

```text
import unittest
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_testcase():
    # 获取当前目录下所有以 'test' 开头的测试用例
    return unittest.defaultTestLoader.discover("./", pattern="test*.py")


def action(suite):
    # 创建一个TextTestRunner并运行测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    # 创建一个包含10个线程的线程池
    with ThreadPoolExecutor(max_workers=10) as executor:
        # 获取所有的测试用例
        test_case = get_testcase()

        # 提交所有的测试用例到线程池中执行
        future_to_suite = {executor.submit(action, suite): suite for suite in test_case}

        # 等待所有任务完成，并处理结果
        for future in as_completed(future_to_suite):
            suite = future_to_suite[future]
            try:
                future.result()  # 如果执行过程中有异常，会抛出
            except Exception as exc:
                print(f"测试用例 {suite} 执行时发生异常: {exc}")

```

### 多线程运行测试用例的注意事项

使用多线程运行测试用例时，并不是所有的测试用例都能用多线程场景运行。

只有数据不冲突的场景，才能使用多线程技术运行测试用例。

例如：

1. 如果使用多线程同时使用相同用户名测试登陆和退出登陆，那么肯定会导致测试结果不准确。

2. 多线程测试修改同一行数据时，也会出现问题，导致测试结果不准确
3. 多线程测试删除同一个数据时，容易出现问题，导致结果不准确

