> 参考：[grid网格布局，比flex方便太多了，介绍几种常用的grid布局属性_grid布局,子元素独占一行-CSDN博客](https://blog.csdn.net/qq_18798149/article/details/133872183)

## flex布局的问题

如果使用justify-content: space-between;让子元素两端对齐，自动分配中间间距，假设一行4个，如果每一行都是4的倍数那没任何问题，但如果最后一行是2、3个的时候就会出现下面的状况：

![image-20250118194143696](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20250118194143696.png)

### 想让最后一行左对齐，怎么办？？

> 1. 解决方式：添加占位元素，最后一行再添加一个元素，将其visibility属性设置为hidden,
>
> 2. 注意，这里不能用`display:none;`
>    * 原因：`visibility: hidden;` 会让元素不可见，但仍然会占用空间，而 `display: none;` 则是完全从页面中移除该元素，包括它所占的空间。

![image-20250118195625617](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20250118195625617.png)

### 完整代码(flex)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./demo.css">
</head>
<body>
    <div class="container">
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div> <!--占位元素-->
    </div>
</body>
</html>
```

```css
.container{
    width: 50%;
    height: 400px;
    margin: auto;
    border: solid;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
.child{
    border-radius: 2px;
    width: 150px;
    height: 100px;
    background-color: aqua;
}
.child:last-child{
    visibility: hidden;
}
```

## 同样的布局，将flex改为grid

```css
display: grid;
grid-template-columns: 1fr 1fr 1fr 1fr;
gap: 5px;   
```

* display：grid 是转为网格布局，这个是必须的
* grid-template-columns：1fr | px 这是将网格分为几列，1fr是自适配单位，可以当成栅格
* gap:30px 这是网格四周的间隔
* 注意：
  * 这三个属性是给父容器添加的，子元素，可以不用设置宽度，也不用设置margin间距即可完成如下布局
  * 实现这种响应式布局，一定要注意父容器不能使用固定宽度，可以将父容器改为如：80%，这样就能根据屏幕的宽度，自动展示一行展示几个了。

![image-20250118200819911](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20250118200819911.png)

### 完整代码(grid)

```css.container{
.container{
    width: 50%;
    height: 400px;
    margin: auto;
    border: solid;
    
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 5px;
}
.child{
    border-radius: 2px;
    height: 100px;
    background-color: aqua;
}
```

## 关于grid的属性

### grid-template-columns

```css
 grid-template-columns: 1fr 200px 1fr 1fr;
```

第二个固定200px，其他自动平均分配

![image-20250118201134062](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20250118201134062.png)

#### 响应式布局

```css
grid-template-columns: repeat(auto-fill, minmax(100px, 1fr)); 
/*这种写法可以用来做响应式布局，auto-fill主轴上指定的宽度或者重复次数是最大可能的正整数，minmax最小值255px、最大值1fr代表剩余空间的比例。*/
```

![image-20250118201421451](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20250118201421451.png)

![image-20250118201458788](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20250118201458788.png)

### 子元素属性grid-row和grid-column可以控制某个元素占领几份

以grid-row行为例，从第几列开始 / 第几列+想占几个；

![image-20250118203948756](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20250118203948756.png)

#### 完整代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./demo.css">
</head>
<body>
    <div class="container">
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
        <div class="child"></div>
    </div>
</body>
</html>
```

```css
.container{
    width: 50%;
    height: 500px;
    margin: auto;
    border: solid;
    
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 5px;
}
.child{
    border-radius: 2px;
    background-color: aqua;
}
.child:first-child{
    grid-column: 1/span 2;
    grid-row: 1/3;
}
```

