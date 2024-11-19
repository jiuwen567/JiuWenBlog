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

**安装HTMLTestRunner_PY**



使用HTMLTestRunner_PY3



## 多线程执行测试用例实战

###  案例

场景：现在假设有六百六十六个测试用例，每个用例至少需要执行1秒，如果是单线程执行，则需要花费666秒。

需求：使用十个线程执行六百六十六个用例



实现分析：我们可以使用线程池来完成。

代码：

```text
import unittest
from threadpool import ThreadPool, makeRequests


def get_testcase():
    return unittest.defaultTestLoader.discover("./", "test*.py")


def action(suite):
    t1 = unittest.runner.TextTestRunner()
    t1.run(suite)



if __name__ == '__main__':
    pool = ThreadPool(10)  # 启动10个线程运行
    test_case = get_testcase() # 获取测试用例
    requests = makeRequests(action, test_case, callback=None) # 初始化要执行的任务
    for req in requests:
        print(req)
        pool.putRequest(req)
    pool.wait() # 等待任务完成

```

### 多线程运行测试用例的注意事项

使用多线程运行测试用例时，并不是所有的测试用例都能用多线程场景运行。

只有数据不冲突的场景，才能使用多线程技术运行测试用例。

例如：

1. 如果使用多线程同时使用相同用户名测试登陆和退出登陆，那么肯定会导致测试结果不准确。

2. 多线程测试修改同一行数据时，也会出现问题，导致测试结果不准确
3. 多线程测试删除同一个数据时，容易出现问题，导致结果不准确

