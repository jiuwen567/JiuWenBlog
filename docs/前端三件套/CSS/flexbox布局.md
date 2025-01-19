>  参考：[Flex 布局教程：语法篇 - 阮一峰的网络日志 (ruanyifeng.com)](https://www.ruanyifeng.com/blog/2015/07/flex-grammar.html)

## 简介

1. **容器与项目的关系**：
   - **容器（flex container）**：包含了要布局的项目集合。通过设置 `display: flex;` 或者 `display: inline-flex;` 将元素定义为 flex 容器。
   - **项目（flex item）**：容器内部的每一个子元素都是一个项目。

2. **主轴与交叉轴**：
   - **主轴（main axis）**：默认水平方向，但可以通过 `flex-direction` 属性进行修改。它决定了项目在容器内的排列方向。
   - **交叉轴（cross axis）**：与主轴垂直的轴线。其方向取决于主轴的方向。

3. **基本的 Flexbox 属性**：

## 容器的属性

   - **`flex-direction`**：决定主轴的方向（行/列）。
   - **`justify-content`**：在主轴上对齐项目。
     * flex-start
     * flex-end
     * center
     * space-between
     * space-around
   - **`flex-wrap`**：控制项目是否换行。
     * wrap换行

* **`align-items`**：在交叉轴上对齐项目。
* **`align-content`**：定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用

###    项目的属性

   - **`flex-grow`、`flex-shrink`、`flex-basis`**：控制项目的放大、缩小和初始大小。

     * 如果一个项目的 `flex-grow` 属性值为 `1`，另一个项目的 `flex-grow` 属性值为 `3`，那么值为 `3` 的一个会较另一个扩大 3 倍。

     * 一个项目的 `flex-shrink` 属性值为 `1`，另一个项目的 `flex-shrink` 属性值为 `3`，那么后者相比前者会受到 `3` 倍压缩。

     * `flex-basis` 为盒子设置初始值。 

       * eg:flex-basis: 10em;

     *  flex 属性有一个简写方式。 `flex-grow`、`flex-shrink` 和 `flex-basis` 属性可以在 `flex` 中一并设置。

        例如，`flex: 1 0 10px;` 会把项目属性设为 `flex-grow: 1;`、`flex-shrink: 0;` 以及 `flex-basis: 10px;`

   - **`align-self`**：允许单个项目有与其他项目不同的交叉轴对齐方式。

     * 调整单个子元素自己的对齐方式，而不会影响到全部子元素

     * `align-self` 可设置的值与 `align-items` 的一样，并且它会覆盖 `align-items` 所设置的值。

   - `order` 属性告诉 CSS flex 容器里子元素的顺序。

     * 这个属性接受数字作为参数，可以使用负数。负数在前。
     * 0为初始值，默认值。
     * 控制元素在主轴上的排列顺序。

