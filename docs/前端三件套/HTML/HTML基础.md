# HTML



**参考文档**
[枫枫知道个人博客 (fengfengzhidao.com)](https://www.fengfengzhidao.com/special/2/23)

## 1. html常用标签

### 1.1 块级标签

#### 1.1.1 form表单

重要属性：

* action
* method

#### 1.1.2 div

* 无论如何都会占据整行。
* 如果没有手动指定高度，高度由其内容决定。

#### 1.1.3 列表

* 有序列表
* 无序列表

### 1.2 行内标签

#### 1.2.1 input

* 搭配label标签

  ```html
  <label for="user">
      用户名
  </label>
  <input placeholder="请输入用户名" id="user">
  ```

* input中的name属性是用来干嘛的？
* value属性
* type属性
  * text
  * password
  * radio(单选框)checkbox(复选框)
  * submit reset
  * button

#### 1.2.2 下拉框 单选框 复选框

* select下拉框

```html
<label for='place'>
  上课地点
</label>
<select id='place' name="place">
  <option>江南校区</option>
  <option>南山校区</option>
</select>
```

* 单选框

  * `checked` 属性设置在第一个单选框上，表示默认情况下它会被选中
  * `name`属性相同

  ```html
  <input type="radio" id="mode1" name="mode" value="mode1" checked>
  <label for="mode1">模式1</label>
  
  <input type="radio" id="mode2" name="mode" value="mode2">
  <label for="mode2">模式2</label>
  ```

* 复选框

  * `name`属性相同
  * `checked` 属性设置在第一个复选框上，表示默认情况下它会被选中

  ```html
    <input type="checkbox" id="hobby1" name="hobby[]" value="football" checked>
    <label for="hobby1">足球</label><br>
    
    <input type="checkbox" id="hobby2" name="hobby[]" value="basketball">
    <label for="hobby2">篮球</label><br>
    
    <input type="checkbox" id="hobby3" name="hobby[]" value="swimming">
    <label for="hobby3">游泳</label><br>
  ```

#### 1.2.3 span

## 2. 路径问题

* 加载图片等静态资源时尽量用相对路径

* web中相对路径和绝对路径

      相对路径
      <form action="xxx">
          <input type="submit" value="提交">
      </form>
      
      绝对路径
      <form action="/xxx">
          <input type="submit" value="提交">
      </form>

  相对路径

  ```html
  http://localhost:63342/qianduan_study/html/4.%E7%9B%B8%E5%AF%B9%E8%B7%AF%E5%BE%84%E5%92%8C%E7%BB%9D%E5%AF%B9%E8%B7%AF%E5%BE%84.html
  提交 地址 变成了
  http://localhost:63342/qianduan_study/html/xxx?
  ```

  绝对路径

      http://localhost:63342/qianduan_study/html/4.%E7%9B%B8%E5%AF%B9%E8%B7%AF%E5%BE%84%E5%92%8C%E7%BB%9D%E5%AF%B9%E8%B7%AF%E5%BE%84.html
      提交 地址 变成了
      http://localhost:63342/xxx?

## 3. 常用属性

1. a标签

   * href 跳转位置

   * target

     * _self 

       本标签页

     * _blank

       重新开一个标签页

2. dwq

##  4. 小知识点

1. `&nbsp`代表空格
