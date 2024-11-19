

## 1. let、const、var

> 大写字母作为常量标识符，用小写字母或者驼峰命名作为变量（对象或数组）标识符。

###  1.1**`let` 与 `var`的区别与使用：**

使用 `var` 关键字声明变量的最大问题之一是你可以轻松覆盖变量声明：

```js
var camper = "James";
var camper = "David";
console.log(camper);
```

在上面的代码中，`camper` 变量最初声明为 `James`，然后被覆盖为 `David`。 然后控制台显示字符串 `David`。

在小型应用程序中，你可能不会遇到此类问题。 但是随着你的代码库变大，你可能会意外地覆盖一个你不打算覆盖的变量。 由于此行为不会引发错误，因此搜索和修复错误变得更加困难。

ES6 中引入了一个名为 `let` 的关键字，这是对 JavaScript 的一次重大更新，以解决与 `var` 关键字有关的潜在问题。 你将在后面的挑战中了解其他 ES6 特性。

如果将上面代码中的 `var` 替换为 `let` ，则会导致错误：

```js
let camper = "James";
let camper = "David";
```

该错误可以在你的浏览器控制台中看到。

所以不像 `var`，当你使用 `let` 时，同名的变量只能声明一次。

**`const`的使用：**

关键字 `let` 并不是声明变量的唯一新方法。 在 ES6 中，你还可以使用 `const` 关键字声明变量。

`const` 具有 `let` 的所有出色功能，另外还有一个额外的好处，即使用 `const` 声明的变量是只读的。 它们是一个常量值，这意味着一旦一个变量被赋值为 `const`，它就不能被重新赋值：

```js
const FAV_PET = "Cats";
FAV_PET = "Dogs";
```

由于重新分配 `FAV_PET` 的值，控制台将显示错误。

你应该始终使用 `cons`

### 1.2 不存在变量提升

`var`命令会发生“变量提升”现象，即变量可以在声明之前使用，值为`undefined`。这种现象多多少少是有些奇怪的，按照一般的逻辑，变量应该在声明语句之后才可以使用。

为了纠正这种现象，`let`命令改变了语法行为，它所声明的变量一定要在声明后使用，否则报错。

```javascript
// var 的情况
console.log(foo); // 输出undefined
var foo = 2;

// let 的情况
console.log(bar); // 报错ReferenceError
let bar = 2;
```

上面代码中，变量`foo`用`var`命令声明，会发生变量提升，即脚本开始运行时，变量`foo`已经存在了，但是没有值，所以会输出`undefined`。变量`bar`用`let`命令声明，不会发生变量提升。这表示在声明它之前，变量`bar`是不存在的，这时如果用到它，就会抛出一个错误。
## 2. 数据类型

* Number
* NAN
  * 非数字类型
* String
  * ‘’包裹
  * “”包裹
  * ``包裹
  * 转义字符
    * `\`+特点字符
    * `\n`换行
    * `\"`  "
    * `\'` ‘
* Boolean
  * 表示逻辑值，即true或false。
* Null
* Symbol
  * ES6新增
  *  唯一且不可变的值，通常用作对象属性的键值。
* function
* undefined
  * 变量没有被赋值
* Object
  * 对象，可以包含多个键值对。

typeof 获取数据类型

- typeof operand;//operand：要检测其类型的操作数。

## html引入js

1. 法一

   ```html
   <script type="text/javascript">
   	function myFunction(argument) {
   		alert("<\/script>")
   	}
    </script>
   
   ```

2. 法二

   ```js
   <script type="text/javascript" src="example.js"></script>
   ```

## 弹框输入语句

prompt

示例

1. demo.html

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
   </head>
   <body>
       <script type="text/javascript" src="./demo.js"></script>
   </body>
   </html>
   ```

2. demo.js

   ```js
   var n = prompt("请输入你的姓名")
   alert(n)
   ```

   

## Date对象

1. JavaScript 获取当前毫秒时间戳

   ```js
   console.log((new Date()).valueOf());   
   console.log(new Date().getTime());      
   console.log(Date.now());                
   console.log(+new Date());           
   ```

2. 获取具体时间

   ```js
   var myDate = new Date();
   console.log(myDate.getYear()); //通常是一个 2 位数（但有时可能会显示成 3 位数），已经不推荐使用。并不是直接返回当前的年份，而是返回从 1900 年到现在的年份差。
   console.log(myDate.getFullYear()); //获取完整的年份(4位,1970-????)
   myDate.getMonth(); //获取当前月份(0-11,0代表1月)         // 所以获取当前月份是myDate.getMonth()+1; 
   myDate.getDate(); //获取当前日(1-31)
   myDate.getDay(); //获取当前星期X(0-6,0代表星期天)
   myDate.getTime(); //获取当前时间(从1970.1.1开始的毫秒数)
   myDate.getHours(); //获取当前小时数(0-23)
   myDate.getMinutes(); //获取当前分钟数(0-59)
   myDate.getSeconds(); //获取当前秒数(0-59)
   myDate.getMilliseconds(); //获取当前毫秒数(0-999)
   ```

3. 案例-计算双十一过去时间

   ```js
   var myDate = new Date();
   var double11 = new Date('2024-11-11 00:00:00')
   var diff = myDate-double11
   var second = Math.floor(diff/1000%60)
   var minute = Math.floor(diff/1000/60%60)
   var hour = Math.floor(diff/1000/60/60%24)
   var day = Math.floor(diff/1000/60/60/24)
   console.log(`双十一过去${day}天${hour}时${minute}分${second}秒`)
   ```

   

