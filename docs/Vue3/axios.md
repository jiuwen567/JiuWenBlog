> 官网：https://www.axios-http.cn/

#### 登录请求封装示例

1. 封装用户请求用到axios

```shell
npm i axios
```

2. 进度条nprogress

> [NProgress: slim progress bars in JavaScript (ricostacruz.com)](https://ricostacruz.com/nprogress/)

```shell
npm i nprogress
```

3. src目录下新建api目录用于封装用户请求(这里是用axios封装的，只是命名用的ajax,并未用原生ajax封装)

目录结构为

![image-20240724110719935](https://typora5672.oss-cn-chengdu.aliyuncs.com/temp/image-20240724110719935.png)



* 封装

  ajaxs.js

  ```js
  // 1.配置base url 超时时间
  //2.请求拦截
  //3.响应拦截
  //4配置进度条
  //显示 隐藏
  import axios from 'axios'
  import NProgress from 'nprogress'
  import 'nprogress/nprogress.css'
  
  
  const service = axios.create({
      baseuRL: '/api',
      timeout: 5000
  })
  
  //请求拦截
  service.interceptors.request.use(config => {
      //开启进度条
      NProgress.start();
      // 请求时，携带token
  
      let arr = ['/user/code/', '/user/register/', '/user/login/'];
  
      if (arr.includes(config.url)) {
          // 如果请求的uRL在数组中，不做任何特殊处理，这些请求可能是不需要携带token的特殊请求，比如验证码、注册、登录等。
      } else {// 从localStorage中获取保存的用户信息（假设在localStorage中存储了用户的信息）, // 获取用户信息中的token，并将其添加到请求的headers中
          config.headers['Authorization'] = 'Bearer ' + JSON.parse(localStorage.getItem('userInfo'))['user']['userInfo']['token'];
      }
      return config;
  })
  // 响应拦截
  service.interceptors.response.use(res => {
      //关闭进度条
      NProgress.done();
      // 返回响应数据
      return res.data;
  }, err => {
      //关闭进度条
      NProgress.done();
      // 返回一个带有错误信息的Promise，用于后续处理
      return Promise.reject(err)
  
  })
  
  export default service
  ```

  nozzle/index.js 

  > 后续按照格式增加接口即可

  ```js
  const base = {
     getcode:'/user/code/',//获取注册时的验证码接口
     getregister:"/user/register/",//获取注册账号的接口
     getlogin:"/user/login/",//获取账号登录的接口
  }
  export default base
  ```

  index.js

  ```js
  import service from './ajax/ajaxs.js'
  import base from './nozzle/index.js'
  
  // 封装获取验证码的请求函数
  export const GetRegisterCode = (parm)=>{
      return service.post(base.getcode,parm)
  }
  // 封装用户注册账号的请求函数
  export const GetRegisterAccount = (parm)=>{
      return service.post(base.getregister,parm)
  }
  
  // 封装用户登录平台的请求函数
  export const login = (parm)=>{
      return service.post(base.getlogin,parm)
  }
  ```
