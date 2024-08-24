1. 停止nginx服务

   ```shell
   sudo ./nginx -s stop 
   ```

2. 注释掉以下内容，否则配置不会生效

![image-20240824122929125](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20240824122929125.png)

3. /etc/nginx/nginx.conf中的http中新增以下内容

参考：[部署 VitePress 站点 | VitePress](https://vitepress.dev/zh/guide/deploy)

```nginx
server {
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    listen 80;
    server_name _;
	index index.html;
    location / {
        # content location
        root /root/web/jiu-wen-blog-dist;
        
        # exact matches -> reverse clean urls -> folders -> not found
        try_files $uri $uri.html $uri/ =404;

        # non existent pages
        error_page 404 /404.html;

        # a folder without index.html raises 403 in this setup
        error_page 403 /404.html;

        # adjust caching headers
        # files in the assets folder have hashes filenames
        location ~* ^/assets/ {
            expires 1y;
            add_header Cache-Control "public, immutable";
        }
    }
}
```

4. 启动nginx服务

```shell
nginx
```

5. 检查服务是否配置正确

```shell
nginx -t
```

6. 后续改配置也可以通过`nginx -s reload`重启服务


## nginx常见错误

### 403

* 权限配置不正确

* 这个是nginx出现403 forbidden最常见的原因。

* 解决办法：　　

　　可以将权限修改为root，在nginx的nginx.conf 文件的顶部加上user root;指定操作的用户是root。