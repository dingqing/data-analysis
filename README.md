# ml-practice
「数据分析、机器学习、深度学习」练习


- 技能

类型 | 应用
--- | ---
爬虫 | [Scrapy使用](crawler/README.md)
&nbsp; | 爬取猫眼电影排行（Request与正则表达式）
&nbsp; | 爬取淘宝商品（Selenium）
&nbsp; | 爬取微信公众号文章（使用代理）
&nbsp; | 爬取Github（模拟登录）
&nbsp; | 爬取微信朋友圈（Appium）
可视化 | [影评分析](./film-reviews/README.md)（热力图+柱状图+词云）

- 机器学习

类型 | 应用
--- | ---
监督学习 | 逻辑回归
&nbsp; | SVM
集成思想 | 决策树
&nbsp; | 随机森林

- 深度学习

类型 | 实现 | 应用
--- | --- | ---
DNN | numpy | [手写深度神经网络](./dl/dnn.py)
&nbsp; | Tensorflow | 搭建神经网络
CNN | numpy | 搭建CNN
&nbsp; | Tensorflow | CNN的Tensorflow实现
LSTM | numpy、keras | LSTM的numpy和keras实现
NLP | Python | 训练一个word2vec词向量
&nbsp; | numpy | 文本情感分析
自编码器 | keras | 自编码器（AutoEncoder）keras实现
变分自编码器 | keras | 变分自编码器VAE的keras实现
GAN | keras | 训练一个深度卷积对抗网络DCGAN