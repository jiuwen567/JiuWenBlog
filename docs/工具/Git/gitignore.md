## 什么是.gitignore文件？

.gitignore文件是一个文本文件，用于告诉Git在进行版本控制时应该忽略哪些文件或文件夹。我们可以在.gitignore文件中编写需要忽略的规则，这样Git在执行提交、推送和拉取操作时就会自动忽略这些文件。通常，.gitignore文件应该位于Git仓库的根目录下。

## .gitignore文件的基本语法

.gitignore文件的语法非常简单，每行一个忽略规则。可以使用以下语法来定义忽略规则：

1. 使用`#`符号开头的行表示注释，这些行将被Git忽略；
2. 使用`/`表示文件夹，例如`node_modules/`表示忽略当前目录下的node_modules文件夹；
3. 使用`*`表示任意字符，例如`*.log`表示忽略所有的.log文件；
4. 使用`!`表示否定，例如`!example.log`表示不忽略example.log文件。

## 如何在.gitignore中忽略node_modules文件夹

在大多数Node.js项目中，我们都会使用npm包管理器来安装和管理依赖包。这些依赖包通常位于项目根目录下的[ node](https://geek-docs.com/git/git-questions/856_git_ignoring_node_modules_using_gitignore.html#)_modules文件夹中。由于依赖包的数量庞大，将node_modules纳入[ 版本控制系统](https://geek-docs.com/git/git-questions/856_git_ignoring_node_modules_using_gitignore.html#)会导致仓库过于庞大、上传和下载速度过慢。因此，我们应该将node_modules添加到.gitignore文件中，以便忽略该文件夹。

在.gitignore文件中设置忽略node_modules文件夹的规则如下：

```plaintext
node_modules/
```

Plaintext

Copy

以上规则表示忽略根目录下的node_modules文件夹以及其下的所有文件。

## 在.gitignore中添加其他忽略规则

除了node_modules文件夹以外，还有一些其他常见的文件或文件夹也应该添加到.gitignore中。例如，我们通常不想将编译生成的文件、IDE或文本编辑器生成的配置文件、敏感信息等提交到Git仓库中。以下是一些常见的忽略规则示例：

```plaintext
# 忽略IDE生成的文件和配置
.idea/
*.iml
.vscode/

# 忽略敏感信息
config.js
*.env
*.pem

# 忽略编译生成的文件
build/
dist/
*.dll
*.exe
```

Plaintext

Copy

根据项目实际情况，我们可以根据需要添加其他的忽略规则。

## 如何应用.gitignore文件的变更

一旦我们在.gitignore文件中添加了相应的忽略规则，Git会自动开始忽略这些文件。但是，如果在.gitignore文件中添加或修改了规则，Git可能不会立即生效。这时我们需要执行以下命令来应用.gitignore文件的变更：

```bash
# 清除已缓存的文件
git rm -r --cached .

# 重新添加所有文件
git add .

# 提交变更
git commit -m "Update .gitignore"
```

Bash

Copy

通过以上命令，我们清除了已缓存的文件并重新将所有文件添加到暂存区中，然后再次提交变更即可。