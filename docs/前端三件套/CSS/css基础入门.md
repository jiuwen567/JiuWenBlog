

## 如何理解层叠

* 优先级（权重最重要）

  * Important>内联样式(标签内部声明的)>ID 选择器 >Class 选择器

    ```css
      .pink-text {
        color: pink !important;
      }
    /*
    有最高的优先级
    */
    ```

* 同级后面的会覆盖前面的

## class

* HTML 元素可以同时包含多个 class

```html
<img src="path/to/image.jpg" class="smaller-image thick-green-border">
```

这样，img 元素就同时具有了 smaller-image 和 thick-green-border 这两个 class。

* 在 `<style>` 标签里面声明的 `class` 顺序十分重要，之后的声明会覆盖之前的声明。 第二个声明的优先级始终高于第一个声明。 

## 外边距(margin)、内边距(padding)、边框(border)

> 外边距：影响元素与其相邻元素之间的距离，可以用来控制元素之间的间隔
>
> 内边距：内边距是指元素内容与其边框之间的空间。

外边距（margin）、内边距（padding）和边框（border）是 CSS 盒子模型的三个基本部分，它们控制元素的布局和样式。

1. **内边距（padding）**：
   
   - 内边距是指元素内容与其边框之间的空间。
   
   - 可以使用 `padding` 属性来设置元素的内边距，例如 `padding: 10px;`。

   - 内边距会增加元素内容周围的空间，但不会影响元素的背景颜色或边框。
   
   - 内边距可以分别设置为上、右、下、左四个方向的值，例如 `padding-top`, `padding-right`, `padding-bottom`, `padding-left`。
   
     * 可以把它们汇总在一行里面一并声明，像是这样：
   
     ```css
     padding: 10px 20px 10px 20px;
     ```
   
     这四个值按顺时针排序：上、右、下、左，并且设置的效果等同于分别声明每一个方向的内边距。
     
   - 设置padding默认会撑大content,即在下面这种情况会出现对不齐的情况
   
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Document</title>
         <style>
             .div1{
                 width: 200px;
                 height: 200px;
                 background-color: antiquewhite;
                 padding: 20px 20px 20px 20px;
                 /* box-sizing: border-box */
             }
             .div2{
                 width: 200px;
                 height: 200px;
                 background-color:aquamarine
             }
         </style>
     </head>
     <body>
         <div class="div1">
             哈哈哈哈哈哈哈哈哈哈哈哈哈哈
         </div>
         <div class="div2">
         </div>
     </body>
     </html>
     ```
     
     ![image-20241015221918273](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20241015221918273.png)
     
   - 在原有的content基础上直接拿出对应的间距作为内间距可解决问题
   
     * box-sizing：border-box
     
     ![image-20241015222004573](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20241015222004573.png)
   
2. **外边距（margin）**：
   - 外边距是指元素边框与周围元素之间的空间。
   
   - 可以使用 `margin` 属性来设置元素的外边距，例如 `margin: 10px;`。
   
   - 外边距会影响元素与其相邻元素之间的距离，可以用来控制元素之间的间隔。
   
   - 外边距也可以分别设置为上、右、下、左四个方向的值，例如 `margin-top`, `margin-right`, `margin-bottom`, `margin-left`。
   
     * 无需分别通过 `margin-top`、`margin-right`、`margin-bottom`、`margin-left` 分别声明，比如：
   
     ```css
     margin: 10px 20px 10px 20px;
     ```
   
     这四个值按顺时针排序：上、右、下、左，并且设置的效果等同于分别声明每一个方向的外边距值。
   
     使用顺时针标记指定元素的外边距
   
3. **边框（border）**：
   
   - 边框是指围绕在元素内容和内边距外侧的线条。
   
   - 可以使用 `border` 属性来定义元素的边框，例如 `border: 1px solid #000;`。
   
   - 边框可以有不同的样式、宽度和颜色，通过 `border-style`, `border-width` 和 `border-color` 属性来定义。
   
   - 边框通常位于内边距和外边距之间，它的宽度会增加元素的总尺寸。
   
   - 在设置时默认会撑大content, 加上box-sizing: border-box;可修正。
   
     ```html
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Document</title>
         <style>
             .div1{
                 width: 200px;
                 height: 200px;
                 background-color: antiquewhite;
                 padding: 20px 20px 20px 20px;
                 box-sizing: border-box
             }
             .div2{
                 width: 200px;
                 height: 200px;
                 background-color:aquamarine;
                 border-style: solid;
                 border-radius: 10%;
                 border-width: 10px;
                 border-color: blue;
                 box-sizing: border-box;
             }
         </style>
     </head>
     <body>
         <div class="div1">
             哈哈哈哈哈哈哈哈哈哈哈哈哈哈
         </div>
         <div class="div2">
             
         </div>
     </body>
     </html>
     ```

## css选择器

1. **元素选择器（Element Selector）**：
   - 选择文档中所有具有特定元素名称的元素。
   - 示例：`p` 选择所有 `<p>` 元素。

2. **类选择器（Class Selector）**：
   - 选择具有特定类名的元素。
   - 示例：`.my-class` 选择所有具有 `class="my-class"` 的元素。

3. **ID选择器（ID Selector）**：
   - 选择具有特定 ID 的元素。
   - 示例：`#my-id` 选择 `id="my-id"` 的元素。

4. **属性选择器（Attribute Selector）**：
   - 根据元素的属性值选择元素。
   - 示例：
     - `[type="text"]` 选择所有 `type="text"` 的元素。
     - `[href^="https://"]` 选择所有 `href` 属性以 `https://` 开头的元素。

5. **伪类选择器（Pseudo-class Selector）**：
   - 根据元素的状态或位置选择元素。
   
   - 示例：
     - `:hover` 选择鼠标悬停在其上的元素。
     - `:first-child` 选择其父元素的第一个子元素。
     - `:nth-child`选择父元素的子元素
       * [:nth-child() - CSS：层叠样式表 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/Web/CSS/:nth-child)
       * 
     - ……
     
   - 案例1-伪类选择器:hover+Transform scale 属性在悬停时缩放元素
   
     ```css
     <style>
       div {
         width: 70%;
         height: 100px;
         margin:  50px auto;
         background: linear-gradient(
           53deg,
           #ccfffc,
           #ffcccf
         );
       }
       div:hover{
         transform: scale(1.1);
       }
     </style>
     
     <div></div>
     ```
     
     实现了`div` 元素在悬停时大小应该缩放到原始大小的 1.1 倍。
   
6. **伪元素选择器（Pseudo-element Selector）**：
   - 用于向某些选择器添加特殊效果。
   - 示例：
     - `::before` 在元素内容之前插入内容。
     - `::after` 在元素内容之后插入内容。

7. **组合选择器（Combinator Selector）**：
   
   - 用于结合两个或多个选择器来选择特定元素。
   - 示例：
     - `div p` 选择所有 `<div>` 元素内部的 `<p>` 元素。
     - `ul > li` 选择所有直接作为 `<ul>` 子元素的 `<li>` 元素。
   
8. **通用选择器（Universal Selector）**：
   - 选择文档中的所有元素。
   - 示例：`*` 选择所有元素。

## 常用属性

* text-align
  * center
  * right
  * left

* float（脱离文档流，高度为0，页面布局一般给其加父元素）
  * left
  
  * right
  
  * center
  
  * 示例
  
    ```html
    <!DOCTYPE html>
    <html lang="en">
    
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            .son1{
                height: 50px;
                float: left;
                background-color: bisque;
            }
            .son2{
                height: 50px;
                float: right;
                background-color: bisque;
            }
    
        </style>
    </head>
    
    <body>
        <div class="farther">
            <div class="son1">
                son1
            </div>
            <div class="son2">
                son2
            </div>
        </div>
    </body>
    
    </html>
    ```
  
* position

  * relative（相对文档流）
    * 不会释放文档流
    * 基于自身左上角的点进行定位
    * 上下左右为平移距离（可新设置属性top: 100px、left:100px等）
  * absolute
    * 释放文档流
    * 先找父视图是否有定位属性（position）如果没有继续往上找。
  * fixed
    * 释放文档流
    
  * ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            .div1{
                width: 200px;
                height: 200px;
                background-color: red;
                position: fixed;
                right: 0;
            }
            .div2{
                width: 200px;
                height: 200px;
                background-color: yellow;
                position: relative;
                left: 200px;
            }
            .div3{
                width: 200px;
                height: 200px;
                background-color: blue;
                position: absolute;
                right: 200px;
                bottom: 200px;
            }
            .div4{
                width: 200px;
                height: 1000px;
                background-color: pink;
            }
        </style>
    </head>
    <body>
        <div class="div1"></div>
        <div class="div2"></div>
        <div class="div3"></div>
        <div class="div4"></div>
    </body>
    </html>
    ```
  
  * ![image-20241027233826168](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20241027233826168.png)
  
  
