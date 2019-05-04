import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import options as opts
from pyecharts.charts import Geo, Page
from wordcloud import WordCloud, STOPWORDS
import jieba
from pyecharts.globals import ChartType, SymbolType

f = open('movie-reviews.txt',encoding='UTF-8')
data = pd.read_csv(f,sep=',',header=None,encoding='UTF-8',names=['date','nickname','city','rate','comment'])


# 热力图
city = data.groupby(['city'])
rate_group = city['rate']
city_com = city['city'].agg(['count'])
city_com.reset_index(inplace=True)
# data_map = [[city_com['city'][i],city_com['count'][i]] for i in range(0,city_com.shape[0])]
data_map = [list(z) for z in zip(city_com['city'],city_com['count'])]
for n, v in enumerate(data_map):
    if Geo().get_coordinate(v[0])==None:
        data_map.pop(n)
# print(data_map)

def geo_base() -> Geo:
    c = (
        Geo()
            .add_schema(maptype="china")
            .add(
            "geo",
            data_map,
            # type_=ChartType.HEATMAP, #热力效果，数字小的时候颜色很淡
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="《狄仁杰之四大天王》影评用户地区分布"),
        )
    )
    return c
geo_base().render("out/base.html")


# 柱状图
#评分分析
rate = data['rate'].value_counts()

sns.set_style("darkgrid")
bar_plot = sns.barplot(x=rate.index,y=(rate.values/sum(rate)),palette="muted")
plt.xticks(rotation=90)
plt.show()


# 词云图
#分词
comment = jieba.cut(str(data["comment"]),cut_all=False)
wl_space_split= " ".join(comment)
#导入背景图
backgroud_Image = plt.imread('statics/bg.jpg')
stopwords = STOPWORDS.copy()
# print(" STOPWORDS.copy()",help(STOPWORDS.copy()))
#可以自行加多个屏蔽词，也可直接下载停用词表格
stopwords.add("电影")
stopwords.add("一部")
stopwords.add("一个")
stopwords.add("没有")
stopwords.add("什么")
stopwords.add("有点")
stopwords.add("这部")
stopwords.add("这个")
stopwords.add("不是")
stopwords.add("真的")
stopwords.add("感觉")
stopwords.add("觉得")
stopwords.add("还是")
stopwords.add("特别")
stopwords.add("非常")
stopwords.add("可以")
stopwords.add("因为")
stopwords.add("为了")
stopwords.add("比较")
print (stopwords)
#设置词云参数
#参数分别是指定字体/背景颜色/最大的词的大小,使用给定图作为背景形状
wc =WordCloud(width=1024,height=768,background_color='white',
              mask = backgroud_Image,font_path='statics/simkai.ttf',
              stopwords=stopwords,max_font_size=400,
              random_state=50)
#将分词后数据传入云图
wc.generate_from_text(wl_space_split)
plt.imshow(wc)
plt.axis('off')#不显示坐标轴
plt.show()
#保存结果到本地
wc.to_file(r'out/movie_wordcloud.jpg')