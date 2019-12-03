# ml-practice
「数据分析、机器学习、深度学习」练习


- 技能

类型 | 工具 | 应用
--- | --- | ---
爬虫 | Scrapy | [Scrapy使用](crawler/README.md)
&nbsp; | requests | [从leetcode旧帐号爬取ac代码提交到新帐号](crawl-leetcode)
可视化 | pandas, matplotlib seaborn pyecharts wordcloud, jieba | [影评分析](./film-reviews/README.md)（热力图+柱状图+词云）

- 机器学习

类型 | 工具 | 应用
--- | --- | ---
监督学习 | sklearn | 线性回归
&nbsp; | &nbsp; | 逻辑回归
&nbsp; | &nbsp; | 贝叶斯
&nbsp; | &nbsp; | SVM
集成思想 | &nbsp; | 决策树
&nbsp; | &nbsp; | 随机森林
无监督学习 | Python、sklearn | [k-means](./ml/kmeans.py)
&nbsp; | Python | [层次聚类](./ml/hierarchicalClusterer.py)

- 深度学习

类型 | 工具 | 应用
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