# data-analysis
数据分析练习


### 爬虫
- [爬虫](crawler/crawler.md)
### 数据预处理
- [数据预处理](./pre-process/pre-process.py)
    1. 缺失值处理
    2. 异常值处理
    3. 数据标准化处理
    4. 数据连续属性离散化
### 可视化
- 影评分析（热力图+柱状图+词云）(./film-reviews)
    ```
    运行环境：
    Ubuntu 18.04
    python 3.6
    pip3 install -r requirements.txt
    apt install python3-tk
    
    爬影评：
    python3 crawl-film-reviews.py
    展示：
    python3 draw.py
    
    运行结果保存在/out目录
    ```
### 机器学习
- [机器学习笔记](https://www.processon.com/view/link/5ccef770e4b085d010905bc0)
- 分类算法
    - [决策树](./machine-learning/decisionTree.py)
    - 随机森林
    - 逻辑回归
    - SVM
### 深度学习
- DNN
- CNN
- RNN
- LSTM