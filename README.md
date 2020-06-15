# examples-of-crawlers
  各爬虫示例，淘宝、京东、知乎、bilibili等网站，简单，拿来即用

## [1.taobao_login][login]

### 技术选项

| 技术项 | 技术选择 | 版本 |备注 |
| --- | --- | --- | --- |
| 开发语言 | python  |  3.8.1 | |
| 无头驱动 | selenium  |  3.141.0 | |
| 代理 | mitumproxy  |  5.1.1 | |

### 准备

1. 谷歌浏览器
2. 对应谷歌浏览器版本号的驱动 [点击下载](http://chromedriver.storage.googleapis.com/index.html)
3. 安装pip包
```
pip3 install -r requirements.txt

or 

pip3 install mitmproxy
pip3 install selenium
```  

### 描述
1. 利用代理修改淘宝检测无头浏览器js，详见 httpProxy.py
2. 无头浏览器傻瓜式登录

### 运行
1. 启动代理过滤淘宝检测无头
```
mitmdump -s httpproxy.py -p 9000
```

2. 进行登录测试
```
python3 login.py
```
