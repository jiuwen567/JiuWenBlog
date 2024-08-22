@[toc]
# Git的使用



## Linux下载

* 安装：` sudo apt-get install git`
* 查看版本核实是否安装成功: ` git --version`
* 查看帮助：` git --help`
* 查看当前文件夹全部内容：`la`
* 创建py文件：`vim test.py`=>`:wq`退出编辑
* 查看文件里的内容：`cat test.py`
* 往test.py里追加内容`echo print("hello" >> test.py)`

## 初始化仓库并做最简单的配置

* cmd终端中进入想要存储代码的文件夹

* cd 到文件夹

* 使用`git init`初始化仓库 --》在当前目录下初始化本地仓库，即生成版本库(.git目录）

* ` git config --global user.name "jiuwen567"`创建用户名

* `git config --global user.email "2750826557@qq.com"`配置邮箱

* `git config --global --list`查看用户名和邮箱相关信息

  

## 设置工作区、暂存区和仓库

* 使用`git status`检测当前文件夹(需含有.git文件)状态--》增加或者删除某些东西==工作区==

* 使用`git add .`提交当前改变所有的东西(git status检测到的所有东西)或者使用`git add "文件名"`提交单个文件的改动==暂存区==

* 使用`git commit -m "自己对当前改动的解释"`==提交git仓库==

  ![image-20230126211456124](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/5ec5f381128ed75337ddd23e871e62c9.png)

  

* 使用`git commit -am "自己对当前改动的解释"`==直接提交到git仓库，不经过暂存区==

## **查看历史提交记录**

```cmd
git log
git reflog# 查看每个版本对应的 SHA-1 值和操作信息，以便我们进行代码回滚或者撤销等操作。

# git reflog 可以查看所有分支的所有操作记录（包括commit和reset的操作），包括已经被删除的commit记录，git log不能查看已经删除了的commit记录
```

## 切换版本

```cmd
git reset --hard + `SHA-1哈希值`
```

![image-20230603170448634](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/fcf4e82362511abf4a1e23a98e17fba1.png)

黄色值对应响应版本SHA-1哈希值

## Git 分支管理

几乎每一种版本控制系统都以某种形式支持分支，一个分支代表一条独立的开发线。

使用分支意味着你可以从开发主线上分离开来，然后在不影响主线的同时继续工作。

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-VvfUNGS4-1685803840716)(null)]

Git 分支实际上是指向更改快照的指针。

有人把 Git 的分支模型称为**必杀技特性**，而正是因为它，将 **Git** 从版本控制系统家族里区分出来。

* 创建分支命令：

```
git branch (branchname)
git branch –v # 显示当前版本及备注
```

* 切换分支命令:

```
git checkout (branchname)
```

>  当你切换分支的时候，Git 会用该分支的最后提交的快照替换你的工作目录的内容， 所以多个分支不需要多个目录。

* 合并分支命令:

```
git merge 
```

* **合并冲突**

  >  合并分支时，两个分支在同一个文件的同一个位置有两套完全不同的修改，git无法替我们决定使用哪一个，必须人为决定新代码内容

## 将本地仓库同步到GitHub&Gitee

### GitHub

* 创建仓库

  ```cmd
  git remote add origin git@github.com:jiuwen567/learn-git.git
  git branch -M main
  git push -u origin main
  ```

* 配置公钥

  ![image-20230126213555784](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/e7950f390942d840d654ec735b3250fa.png)

* 获取公钥

  1. cmd中通过命令`ssh-keygen`再三次回车得到公钥
  2. 再进入到`.ssh`文件通过`explorer .`记事本打开`id_rsa.pub`查看公钥
  3. 复制粘贴公钥

* 将本地仓库推送给远程GitHub仓库

  终端输入：

  ```cmd
  git remote add origin git@github.com:jiuwen567/learn-git.git
  git branch -M main
  git push -u origin main
  ```

  ![image-20230126220506109](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/3ebd79dbc35ea5a32b08cf1cb003eece.png)

###  Gitee(以Linux系统为例)

* [Gitee平台]:https://gitee.com/创建仓库

* 配置公钥

  1. `ssh-keygen -t rsa -C + 邮箱名`
  2. 进入.ssh查看公钥
  3. ![image-20230603191612715](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/1463f1d5fb1a00b066d31e4a8639fea2.png)

  4. `la查看.ssh目录`
  5. `cat id_rsa_pub`查看公钥
  6. ![image-20230603191748750](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/af6583d3de1762ff3b895e36fa9833af.png)

* 粘贴公钥

* ![image-20230603192509564](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/23ddf2e0d2a78743b894fe56317545e8.png)

* 测试是否配置成功：`ssh –T git@gitee.com`

* 查看远程仓库：`git remote -v`

* ![image-20230603200654144](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/22785f45c1bdc9ff776d039fc3316868.png)

* origin可增加名字=》`git remote add +更名 +远程仓库地址 `

* 将本地仓库推送给远程Gitee仓库

* 终端输入：

  ```cmd
  git remote add gitee git@gitee.com:jiuwen567/learn_git.git # 配置远程仓库，克隆的仓库就不用配置
  git push -u gitee main # 将数据传送到远程仓库
  git pull # 拉取远程仓库数据
  ```

  * 注意GitHub中的origin可以随意替换如果在两个平台同时创建则origin需要替换成不同的值

## 克隆别人仓库

* `git clone +'Http地址或ssh地址'`

* `git remote -v`查看远程仓库

* `git fetch origin master:temp`从远程获取最新版本到本地

* `git diff temp`比较本地的仓库与远程仓库的区别

* `git pull`更新本地仓库