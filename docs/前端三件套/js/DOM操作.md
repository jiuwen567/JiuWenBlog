# DOM操作

## 获取DOM节点

1. 常用

   * document.getElementById()

   * document.getElementsByTagName()

   * document.getElementsByClassName() 

   * ```js
     // 返回ID为'test'的节点：
     let test = document.getElementById('test');
     
     // 先定位ID为'test-table'的节点，再返回其内部所有tr节点：
     let trs = document.getElementById('test-table').getElementsByTagName('tr');
     
     // 先定位ID为'test-div'的节点，再返回其内部所有class包含red的节点：
     let reds = document.getElementById('test-div').getElementsByClassName('red');
     
     // 获取节点test下的所有直属子节点:
     let cs = test.children;
     
     // 获取节点test下第一个、最后一个子节点：
     let first = test.firstElementChild;
     let last = test.lastElementChild;
     ```

2. selector

   * querySelectorAll()

   * querySelector()

   * ```js
     // 通过querySelector获取ID为q1的节点：
     let q1 = document.querySelector('#q1');
     
     // 通过querySelectorAll获取q1节点内的符合条件的所有节点：
     let ps = q1.querySelectorAll('div.highlighted > p');
     ```

   * 注意：低版本的IE<8不支持`querySelector`和`querySelectorAll`。IE8仅有限支持。

## 更新DOM

### innerHTML



### innerText

#### 时钟案例

> setInterval(响应函数,时间ms)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id="clock">

    </div>
    <script type="text/javascript" src="./demo.js"></script>
</body>
</html>
```

```js
var myDate = new Date()
var clock = document.querySelector('#clock')

function getCurTime(){
    var myDate = new Date(); // 每次获取当前时间时重新创建 Date 对象
    clock.innerText = `当前时间${myDate.getFullYear()}年${myDate.getMonth()+1}月${myDate.getDate()}日${myDate.getHours()}时${myDate.getMinutes()}分${myDate.getSeconds()}秒`
}
setInterval(function(){
    getCurTime()
},1000)
```

### value

获取表单元素(input textarea)的值

形式：`element.value`

### style

形式：`element.style.属性`=属性值

> 属性要用驼峰式命名 eg:font-size  —>fontSize

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .div1{
            width: 100px;
            height: 100px;
            margin: auto;
            background-color: aqua;
        }
    </style>
</head>
<body>
    <div class="div1" onclick="changeBacColor()">

    </div>
    <script type="text/javascript" src="./demo.js"></script>
</body>
</html>
```

```js
var div1 = document.getElementsByClassName('div1')[0]
function changeBacColor(){
    if(div1.style.backgroundColor == "aqua"){
        div1.style.backgroundColor = "red"
    }else{
        div1.style.backgroundColor = "aqua"
    }
}
```

### className classList

1. className

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Document</title>
       <style>
           .div1{
               width: 100px;
               height: 100px;
               margin: auto;
               background-color: aqua;
           }
           .div11{
               color: blue;
           }
       </style>
   </head>
   <body>
       <div class="div1" onclick="changeColor()">
           我以我血荐轩辕
       </div>
       <script type="text/javascript" src="./demo.js"></script>
   </body>
   </html>
   ```

   ```js
   var div1 = document.getElementsByClassName('div1')[0]
   function changeColor() {
       div1.className = div1.className + ' div11'
   }
   ```

2. classList

   ```js
   var div1 = document.getElementsByClassName('div1')[0];
   
   function changeColor() {
       div1.classList.add('div11');
   }
   ```


## 自定义属性

### setAttribute

设置一个属性和值

形式：`element.setAttribute("键","值")`

### getAttribute

获取属性值

形式：`element.getAttribute('属性名')`

eg:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <a href="http://www.baidu.com" target="_self">百度</a>
    <script type="text/javascript" src="./demo.js"></script>
</body>
</html>
```

```js
var tag_a = document.getElementsByTagName('a')
console.log(tag_a[0].getAttribute('href'),tag_a[0].getAttribute('target'))//http://www.baidu.com  _self
```

### 案例-对应相同属性值的div框，点击不同框，改变对应颜色

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .div1{
            width: 50px;
            height: 50px;
            border-style: solid;
        }
        .bg0{
            background-color: aqua;
        }
        .bg1{
            background-color: rgb(171, 109, 16);
        }
        .bg2{
            background-color: rgb(118, 17, 24);
        }
        .bg3{
            background-color: rgb(33, 25, 174);
        }
        .bg4{
            background-color: rgb(192, 221, 25);
        }
    </style>
</head>
<body>
    <div class="div1">div1</div>
    <div class="div1">div2</div>
    <div class="div1">div3</div>
    <div class="div1">div4</div>
    <div class="div1">div5</div>
    <script type="text/javascript" src="./demo.js"></script>
</body>
</html>
```

```js
var divs = document.getElementsByClassName('div1')
for (let index = 0; index < divs.length; index++) {
   var element = divs[index]
    element.setAttribute('index',index)
    element.onclick = function(){
        var i = this.getAttribute('index')
        var bg = `bg${i}`
        this.classList.add(bg)
    }
}
```

## DOM事件绑定

### 使用 HTML 属性绑定事件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

</head>
<body>
    <button onclick="handleClick(this)">点击我</button>
    <script type="text/javascript" src="./demo.js"></script>
</body>
</html>
```

```js
function handleClick(button) {
    alert('你点击了按钮: ' + button.textContent);
}
```

### `on` 系列事件属性

案例-tabs标签栏

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .tabs{
            width: 800px;
            height: 80px;
            border-style: solid;
            margin: auto;
            display: flex;
            justify-content: space-evenly;
            border-color: gainsboro;
            align-items: center;
        }
        .tab{
            width: 80px;
            height: 60px;
            border-color: gainsboro;
            border-style: solid;
            border-radius: 2px;
            color:#8e8e8e;
            /*文本居中*/
            display: flex;
            flex-direction: column;
            justify-content: space-evenly;
            align-items: center;
        }
        #bg{
            background-color: #eef3f8;
            color: #3a84ff;
        }
        .bg2{
            background-color: #eef3f8;
            color: #3a84ff;
        }
    </style>
</head>
<body>
    <div class="tabs">
        <div class="tab" id="bg"><div class="date">11月11日</div><div class="week">星期一</div></div>
        <div class="tab"><div class="date">11月12日</div><div class="week">星期二</div></div>
        <div class="tab"><div class="date">11月13日</div><div class="week">星期三</div></div>
        <div class="tab"><div class="date">11月14日</div><div class="week">星期四</div></div>
        <div class="tab"><div class="date">11月15日</div><div class="week">星期五</div></div>
        <div class="tab"><div class="date">11月16日</div><div class="week">星期六</div></div>
        <div class="tab"><div class="date">11月17日</div><div class="week">星期天</div></div>
    </div>
    <script type="text/javascript" src="./demo.js"></script>
</body>
</html>
```

```js
var tabs = document.querySelectorAll('.tab')
var lastIndex = 0
for (let index = 0; index < tabs.length; index++) {
    const tab = tabs[index];
    tab.setAttribute('index',index)
    tab.onclick = function(){
        var i = this.getAttribute('index')
        if(i!==lastIndex){
            this.id = 'bg'
            tabs[lastIndex].id = ''
            lastIndex = i
        }
    }
    tab.onmouseenter = function(){
        var i = this.getAttribute('index')
        this.classList.add('bg2')
    }
    tab.onmouseleave = function(){
        var i = this.getAttribute('index')
        this.classList.remove('bg2')
    }
}
```

### addEventListener()  &&  removeEventListener()

## window事件

* onload() --- html加载完成后再执行

* onresize() --- 浏览器窗口大小发生改变时触发

* onscroll() --- 浏览器滚动条移动时触发

### 案例-scroll相关

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="./style.css">
</head>

<body>
    <button class="scroll-to-top">
        <svg t="1733022815337" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6795" width="40" height="40">
            <path d="M847.9744 438.85226668l-308.9408-310.9888a34.2528 34.2528 0 0 0-24.6784-10.0864c-1.2288-0.1024-2.2528-0.7168-3.4304-0.7168a33.6384 33.6384 0 0 0-13.9776 3.1232 32.9216 32.9216 0 0 0-12.0832 7.6288L206.08 406.13546668a34.304 34.304 0 0 0 24.3712 58.7264 34.5088 34.5088 0 0 0 24.32-9.984l221.7472-221.3888v606.0032a34.4064 34.4064 0 1 0 68.8128 0V231.79946668l253.952 255.5904a34.4064 34.4064 0 0 0 48.6912-48.5376z" p-id="6796"></path>
        </svg>
    </button>

    <script src="./demo.js" type="text/javascript"></script>
</body>

</html>
```

```css
/* 页面背景和布局 */
body {
    font-family: Arial, sans-serif;
    height: 2000px; /* 设置较大的页面高度，便于演示滚动效果 */
    margin: 0;
    padding: 0;
}

/* 定义返回顶部按钮的样式 */
.scroll-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #3498db; /* 蓝色背景 */
    border: none;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: none;
}

/* 设置SVG图标大小 */
.scroll-to-top svg {
    fill: white;
    width: 24px;
    height: 24px;
}

/* 鼠标悬停时的效果 */
.scroll-to-top:hover {
    transform: scale(1.1); /* 放大效果 */
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
}

/* 点击时的动画效果 */
.scroll-to-top:active {
    transform: scale(0.95);
}
```

#### 回到顶部、判断是否到达底部

```js
// 获取返回顶部按钮
var scrollToTopButton = document.querySelector(".scroll-to-top");

// 获取页面滚动元素
var e = document.documentElement

// 监听页面滚动事件
window.onscroll = function() {
    // 检查滚动位置，显示/隐藏返回顶部按钮
    if (e.scrollTop > 300) {
        scrollToTopButton.style.display = "block"; // 显示按钮
    } else {
        scrollToTopButton.style.display = "none"; // 隐藏按钮
    }

    // 判断是否滚动到页面底部
    if (e.scrollTop + e.clientHeight >= e.scrollHeight) {
        console.log("已经滚动到底部");
    }
};

// 点击返回顶部按钮时，平滑滚动到顶部
scrollToTopButton.onclick = function(){
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}
```

## 鼠标事件

* onclick() --- 鼠标单击触发
* ondblclick() --- 鼠标双击触发

* onmouseover() --- 鼠标指针移动到元素上触发

* onmouseout() --- 鼠标指针移开元素时触发

* onmousedown() --- 鼠标左键按下触发

* onmouseup() --- 鼠标左键松开触发

* onmousemove() --- 鼠标指针在元素上移动时触发

### 案例-鼠标移入移出

#### 表格

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
<div ="">

</div>
    <table id="table1">
        <tr>
            <th>id</th>
            <th>种类</th>
            <th>名称</th>
        </tr>
        <tr>
            <td>1</td>
            <td>水果</td>
            <td>橘子</td>
        </tr>
        <tr>
            <td>2</td>
            <td>水果</td>
            <td>李子</td>
        </tr>
        <tr>
            <td>3</td>
            <td>蔬菜</td>
            <td>白菜</td>
        </tr>
        <tr>
            <td>4</td>
            <td>海鲜</td>
            <td>龙利鱼</td>
        </tr>
    </table>


    <script src="./demo.js" type="text/javascript"></script>
</body>

</html>
```

```js
var table1 = document.querySelector('#table1')
var rows = table1.rows
for (let index = 1; index <rows.length; index++) {
    const element = rows[index];
    element.onmouseover = function(){
        this.style.backgroundColor = 'red'
    }
    element.onmouseout = function(){
        this.style.backgroundColor = ''
    }
}
```

#### 阴影

> ### **box-shadow：盒子阴影**
>
> `box-shadow` 属性用于为元素添加阴影效果。它的基本语法是：
>
> ```css
> box-shadow: h-offset v-offset blur-radius spread-radius color inset;
> ```
>
> #### 参数说明：
>
> - **h-offset**：水平偏移量，单位通常是像素（px）。正值表示阴影向右，负值表示阴影向左。
> - **v-offset**：垂直偏移量，单位通常是像素（px）。正值表示阴影向下，负值表示阴影向上。
> - **blur-radius**：模糊半径，决定阴影的模糊程度。值越大，阴影越模糊，越远离元素；值为 0 时阴影是锐利的。
> - **spread-radius**：阴影扩展半径。正值会使阴影变大，负值会使阴影变小。
> - **color**：阴影的颜色，可以使用任何颜色格式，如 `#000000`、`rgba(0, 0, 0, 0.5)` 等。
> - **inset**（可选）：可选的 `inset` 关键字，表示阴影会出现在元素内部，而不是外部。

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./style.css">
</head>

<body>
    <div class="box">
        <img src="./bilibili.svg">
    </div>
    <script src="./demo.js" type="text/javascript"></script>
</body>

</html>
```

```css
.box{
    width: 200px;
    height: 200px;
    margin: auto;
    transition: all 0.3s linear;
}
```

```js
var box = document.querySelector('.box')
box.onmouseenter = function(){
    this.style.boxShadow = "5px 5px 0px gainsboro"
}
box.onmouseleave = function(){
    this.style.boxShadow = ""
}
```

#### 轮播图

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./style.css">
</head>

<body>
    <div class="box">
        <img src="https://img-baofun.zhhainiao.com/pcwallpaper_ugc/static/d59375899923ef1249f7a8a27cf19a68.jpg?x-oss-process=image%2fresize%2cm_lfit%2cw_1920%2ch_1080" alt="">
        <img src="https://pic1.zhimg.com/v2-19d657e1f93c77e381205bf64d37ed58_r.jpg" alt="">
        <img src="https://img-baofun.zhhainiao.com/fs/15cdd2b1ea6cd26f53e76bbf9ca46b3b.jpg" alt="">
        <img src="https://ts1.cn.mm.bing.net/th/id/R-C.7d25ddc83d967bd3e4f6d7f36b3d475d?rik=b0dkPlA7pofd0g&riu=http%3a%2f%2fimg.netbian.com%2ffile%2f2023%2f1219%2fsmall011148ngMZE1702919508.jpg&ehk=cEbRCZtm%2f9Je5XDph0hd5V80n2e8ZW1M3RcjMpFbOcw%3d&risl=&pid=ImgRaw&r=0" alt="">
    </div>
    <script src="./demo.js" type="text/javascript"></script>
</body>

</html>
```

```css
.box{
    width: 700px;
    height: 300px;
    margin: auto;
    background-color: aqua;
    transition: all 0.3s linear;
    position: relative;
}
img{
    width: 700px;
    height: 300px;
    position: absolute;
    opacity: 0;
    transition: all 1s linear;
}
```

```js
var imgs = document.querySelector('.box').children
var index = 3
var lastIndex = 3
setInterval(function () {
    index++
    if (index == 4){
        index = 0
    }
    imgs[index].style.opacity = "1"
    imgs[lastIndex].style.opacity = "0"
    lastIndex = index
},2000)
```

## 键盘事件

* onkeypress() --- 键盘按下并松开后触发

* onkeydown() ---键盘按下触发

* onkeyup() --- 键盘松开触发

### 案例-回车提交多行输入框内容

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <textarea class="text">

    </textarea>
<script src="./demo.js" type="text/javascript"></script>
</body>

</html>
```

```js
var textArea = document.querySelector('.text');
textArea.addEventListener('keypress', function(event) {
    // console.log(this.value); // 多行输入框的内容
    // console.log(event.key); 
    if(event.key=='Enter'){
        commit()
        this.value = ''
        event.preventDefault()//阻止回车默认事件
    }
});
function commit(){
    console.log(`发送内容${textArea.value}`)
}
```

## 表单事件

###  **focus 事件**

- **描述**：当表单元素获取焦点时触发（例如，用户点击输入框或通过键盘导航到输入框）。
- **默认行为**：没有默认行为，但可以用来进行输入框的样式修改、提示信息显示等。

```js
document.querySelector('input').addEventListener('focus', function(event) {
  console.log('输入框已获得焦点');
});
```

###  **blur 事件**

- **描述**：当表单元素失去焦点时触发（例如，用户点击其他地方或按 Tab 键移开焦点）。
- **默认行为**：没有默认行为，但可以用来验证输入内容或者清除焦点时的提示信息。

```js
document.querySelector('input').addEventListener('blur', function(event) {
  console.log('输入框已失去焦点');
});
```

## 冒泡事件

>  **DOM 冒泡事件（Event Bubbling）** 是一种事件传播机制。它是指在事件触发时，事件会从最具体的元素（目标元素）开始，逐层向上（冒泡）传播到最顶层的元素，直到文档对象模型（DOM）树的根节点。

### 事件冒泡的过程

当一个事件发生时，比如点击一个按钮，它首先在该元素上触发，然后事件会冒泡到它的父元素，再到父元素的父元素，依此类推，直到 `document` 对象（或 `window` 对象）为止。

例如：

- 如果点击了某个按钮，事件首先在按钮本身触发。
- 然后事件会冒泡到该按钮的父元素、祖父元素，直到 `document`。

#### eg

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="./style.css">
</head>

<body>
    <div class="btnDiv">
        <button>click me</button>
    </div>
<script src="./demo.js" type="text/javascript"></script>
</body>

</html>
```

```css
.btnDiv{
    width: 100px;
    height: 100px;
    background-color: aqua;
    margin: auto;
}
```

```js
var btnDiv = document.querySelector('.btnDiv')
var btn = document.getElementsByTagName('button')[0]
btnDiv.onclick = function(){
    console.log("点击父元素")
    alert("点击父元素")
}
btn.onclick = function(){
    console.log("子元素")
    alert("点击子元素")
}
```

点击子元素button

![image-20241128115401187](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20241128115401187.png)

触发父元素事件

### 如何控制事件冒泡

**阻止事件冒泡**： 可以使用 `event.stopPropagation()` 方法阻止事件的进一步传播。

js修改为

```js
var btnDiv = document.querySelector('.btnDiv')
var btn = document.getElementsByTagName('button')[0]
btnDiv.onclick = function(){
    console.log("点击父元素")
    alert("点击父元素")
}
btn.onclick = function(event){
    console.log("子元素")
    alert("点击子元素")
    event.stopPropagation()
}
```

## 默认事件

### 常见的DOM默认事件

1. **点击事件（click）**
   - 用户点击一个元素时会触发。
   - 默认行为：触发点击事件后，浏览器会执行相应的操作（如：提交表单、跳转链接等）。
2. **提交事件（submit）**
   - 用户提交表单时会触发。
   - 默认行为：浏览器会将表单数据发送到服务器。
3. **键盘事件（keydown, keypress, keyup）**
   - 键盘按下、按住或释放时触发。
   - 默认行为：通常是在输入框中输入字符，或者执行快捷键操作。
4. **焦点事件（focus, blur）**
   - 当元素获取焦点时触发 `focus`，失去焦点时触发 `blur`。
   - 默认行为：例如，在输入框内输入数据时，触发 `focus` 事件；点击其他地方，触发 `blur`。
5. **鼠标事件（mouseover, mouseout, mouseenter, mouseleave）**
   - 鼠标移动到元素上时触发 `mouseover`，移出时触发 `mouseout`，进入和离开子元素时触发 `mouseenter` 和 `mouseleave`。
6. **表单输入事件（input）**
   - 用户在表单字段中输入内容时触发。
   - 默认行为：修改输入框中的值。
7. **拖放事件（dragstart, drag, dragend）**
   - 用户开始拖动、拖动过程中和拖动结束时触发。
   - 默认行为：用户拖动元素时，浏览器会自动支持拖拽操作。
8. **页面加载事件（load）**
   - 页面或资源加载完成时触发。
   - 默认行为：浏览器加载完成后，触发该事件以执行某些操作（例如，脚本初始化）。
9. **改变事件（change）**
   - 当表单元素的值发生变化时触发（例如：`<input>`、`<select>`等）。
   - 默认行为：用户修改了字段值并离开该字段时触发。

### 默认事件行为的阻止

在JavaScript中，可以通过 `event.preventDefault()` 来阻止事件的默认行为。例如：

- **阻止表单提交**：如果你不希望表单在点击提交按钮时提交，可以在 `submit` 事件的处理函数中调用 `preventDefault()`。

```js
document.querySelector('form').addEventListener('submit', function(event) {
  event.preventDefault(); // 阻止表单提交
  console.log('表单提交已被阻止');
});
```

- **阻止链接跳转**：如果你想阻止链接的默认跳转行为，可以在点击链接时调用 `preventDefault()`。

```js
document.querySelector('a').addEventListener('click', function(event) {
  event.preventDefault(); // 阻止链接跳转
  console.log('链接跳转已被阻止');
});
```



## 案例-页面字体大小设置

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="./style.css">
</head>

<body>
    test
    <button class="font-size-set">
        <svg t="1733045310264" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7361" width="200" height="200">
            <path d="M291.5 771.4H875c28.6 0 51.8 23.2 51.8 51.8 0 28.6-23.2 51.8-51.8 51.8H291.5c-23.4 40.6-71.2 60.4-116.5 48.3-45.3-12.1-76.8-53.2-76.8-100 0-46.9 31.5-87.9 76.8-100 45.3-12.3 93.1 7.5 116.5 48.1z m131.4-207.1H150.1c-28.6 0-51.8-23.2-51.8-51.8 0-28.6 23.2-51.8 51.8-51.8h272.8c18.5-32 52.7-51.8 89.7-51.8s71.2 19.7 89.7 51.8h272.8c28.6 0 51.8 23.2 51.8 51.8 0 28.6-23.2 51.8-51.8 51.8H602.3c-18.5 32-52.7 51.8-89.7 51.8s-71.2-19.8-89.7-51.8zM733.6 150c23.4-40.6 71.2-60.4 116.5-48.3 45.3 12.1 76.8 53.2 76.8 100 0 46.9-31.5 87.9-76.8 100-45.3 12.1-93.1-7.7-116.5-48.3H150.1c-28.6 0-51.8-23.2-51.8-51.8 0-28.6 23.2-51.8 51.8-51.8h583.5z m0 0" p-id="7362"></path>
        </svg>
    </button>
    <div class="font-size-popup">
        <select name="font-size" id="select-font-size">
            <span>请选择字体大小</span>
            <option value="15">小字体</option>
            <option value="25">中字体</option>
            <option value="35">大字体</option>
        </select>
    </div>
    <script src="./demo.js" type="text/javascript"></script>
</body>

</html>

```

```css
/* 页面背景和布局 */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

/* 定义字体大小设置按钮的样式 */
.font-size-set {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: linear-gradient(135deg, #3498db, #8e44ad); /* 渐变背景 */
    border: none;
    border-radius: 50%;
    padding: 15px;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15);
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease;
}

/* 设置SVG图标大小和位置 */
.font-size-set svg {
    fill: white;
    width: 30px;  /* 增大图标 */
    height: 30px;
}

/* 鼠标悬停时的效果 */
.font-size-set:hover {
    transform: scale(1.1); /* 放大效果 */
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    background: linear-gradient(135deg, #2980b9, #9b59b6); /* 更深的渐变效果 */
}

/* 点击时的动画效果 */
.font-size-set:active {
    transform: scale(0.95); /* 按下按钮时的缩小效果 */
}

/* 弹出字体设置框样式 */
.font-size-popup {
    box-sizing: border-box;
    position: fixed;
    bottom: 80px;
    right: 30px;
    background-color: white;
    padding: 15px 25px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    display: none; /* 默认隐藏 */
    transition: opacity 0.3s ease;
}

/* 下拉框样式 */
.font-size-popup select {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 16px;
    background-color: #f7f7f7;
    cursor: pointer;
    transition: border-color 0.3s ease;
}

/* 下拉框获得焦点时 */
.font-size-popup select:focus {
    border-color: #3498db;
}

/* 选项样式 */
.font-size-popup select option {
    padding: 10px;
    background-color: white;
    color: #333;
}

/* 选项样式：选中时 */
.font-size-popup select option:checked {
    background-color: #3498db;
    color: white;
}

```

```js
// 获取按钮和选择框
const fontSizeButton = document.querySelector('.font-size-set');
const fontSizePopup = document.querySelector('.font-size-popup');

// 监听按钮点击事件
fontSizeButton.addEventListener('click', () => {
    // 切换选择框的显示和隐藏
    fontSizePopup.style.display = fontSizePopup.style.display === 'block' ? 'none' : 'block';
    fontSizePopup.style.opacity = fontSizePopup.style.display === 'block' ? '1' : '0';
});

// 获取字体大小下拉框
const selectFontSize = document.getElementById('select-font-size');

// 监听字体大小选择事件
selectFontSize.addEventListener('change', (event) => {
    const fontSize = event.target.value;
    if (fontSize) {
        document.body.style.fontSize = fontSize + 'px'; // 修改页面字体大小
    }
});

```

## 案例-网页全选功能

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    
    <input type="checkbox">全选

    <input type="checkbox">橘子
    <input type="checkbox">香蕉
    <input type="checkbox">李子
    <input type="checkbox">栗子
    <input type="checkbox">苹果
    <input type="checkbox">西瓜
    
    <script src="./demo.js" type="text/javascript"></script>
</body>

</html>
```

```js
var inputTag = document.getElementsByTagName('input')
for (let index = 1; index < inputTag.length; index++) {
    const element = inputTag[index];
    element.onclick= function(){
        inputTag[0].checked = isCheckedAll()
    }

}
function isCheckedAll(){
    for (let index = 1; index < inputTag.length; index++) {
        const element = inputTag[index];
        if (!element.checked) {
            return false
        }
    }
    return true
}
inputTag[0].onclick = function(){
    for (let index = 1; index < inputTag.length; index++) {
        const element = inputTag[index];
        element.checked = this.checked
    }
}
```

## 案例-网页抽奖功能

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./style.css">
</head>

<body>
    <div class="lotterys">
        <div class="lottery" id="prize1">奖品1</div>
        <div class="lottery" id="prize2">奖品2</div>
        <div class="lottery" id="prize3">奖品3</div>
        <div class="lottery" id="prize8">奖品8</div>
        <div class="lottery" id="start">开始</div>
        <div class="lottery" id="prize4">奖品4</div>
        <div class="lottery" id="prize7">奖品7</div>
        <div class="lottery" id="prize6">奖品6</div>
        <div class="lottery" id="prize5">奖品5</div>
    </div>


    <script src="./demo.js" type="text/javascript"></script>
</body>

</html>
```

```css
.lotterys{
    background-color: rgb(173, 241, 241);
    width: 400px;
    height: 400px;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-content: space-between;
    flex-wrap: wrap;
    border-style: solid;
    border-color: aquamarine;
}
.lottery{
    width: 130px;
    height: 130px;
    background-color: aqua;
    font-size: large;
    line-height: 130px;
    text-align: center;
}
.bg{
    background-color: brown;
}
```

```js
var start = document.querySelector('#start')
var currentIndex = 1
var lastIndex = 8
var num = 0
var isButtonClicked = false;//禁止重复点击
start.onclick = function () {
    if (isButtonClicked) {
        return;
    }
    isButtonClicked = true;
    var winner = Math.floor(Math.random() * 8 + 1)
    var timer = setInterval(function () {
        currentIndex++
        if (currentIndex > 8) {
            currentIndex = 1
            num++
        }
        var currentItem = document.querySelector('#prize' + currentIndex)
        currentItem.classList.add('bg')
        var lastItem = document.querySelector('#prize' + lastIndex)
        lastItem.classList.remove('bg')
        lastIndex = currentIndex
        if (currentIndex === winner && num === 5) {
            clearInterval(timer)
            console.log('恭喜抽中奖品' + currentIndex)
            currentIndex = 1
            num = 0
            isButtonClicked = false;
        }
        
    }, 100)
}
```

