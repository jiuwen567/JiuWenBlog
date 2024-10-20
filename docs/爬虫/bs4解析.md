# bs解析

官方文档*https://www.crummy.com/software/BeautifulSoup/bs4/doc/*

## 示例-博客园

```python
from bs4 import BeautifulSoup
import requests,csv,os
url = "https://www.cnblogs.com/"
res = requests.get(url).text
soup = BeautifulSoup(res, 'lxml')
articles = soup.select('.post-item')
items = []
for article in articles:
    title = article.select_one('.post-item-title').text
    summary = article.select_one('.post-item-summary').text.strip()
    footer = article.select_one('.post-item-foot')
    author = footer.select_one('a>span').text
    publish_time = footer.select_one('.post-meta-item').text.strip()
    item = {
        '标题':title,
        '概要':summary,
        '作者':author,
        '发布时间':publish_time
    }
    items.append(item)
base_dir = os.getcwd()
file_path = os.path.join(base_dir,'items.csv')
headers = {'标题','概要','作者','发布时间'}
with open(file_path,'w',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,headers)
    writer.writeheader()
    writer.writerows(items)
```



