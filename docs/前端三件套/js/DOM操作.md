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

