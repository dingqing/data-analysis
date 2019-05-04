## 爬虫


### 工具
- [Scrapy](https://scrapy-chs.readthedocs.io/zh_CN/stable/intro/tutorial.html)
- 请求库
    - Urllib
    - Requests
- 解析库
    - [XPath](http://www.w3school.com.cn/xpath/index.asp)
        
        表达式 | 描述
        --- | ---
        nodename | 此节点的所有子节点
        / | 直接子节点
        // | 子孙节点
        . | 当前节点
        .. | 父节点
        @ | 选取属性
        …… | 
    - BeautifulSoup

### 存储
- 文件
- 关系型数据库
- NoSQL
    
### 反爬
- 验证码识别
    - 图形验证码
    - 滑动验证码
    - 点触验证码
    - 微博宫格验证码
- 代理的使用
    - 代理设置
    - 代理池
- 模拟登录
    - Cookies池
- APP的爬取
    - 使用Charles
    - 使用Appium

### 异步、分布式爬虫

### 实践
- [Scrapy使用](scrapy-practice.md)
- 爬取猫眼电影排行（Request与正则表达式）
- 爬取今日头条街拍美图
- 爬取淘宝商品（Selenium）
- 爬取微信公众号文章（使用代理）
- 爬取Github（模拟登录）
- 爬取微信朋友圈（Appium）