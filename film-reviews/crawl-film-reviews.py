import requests
import json
import time
import random

#下载一页数据
def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:  #页面正常响应
        return response.text # 返回页面源代码
    return None

#解析一页数据
def parse_one_page(html):
    data = json.loads(html)['cmts'] #评论以json形式存储,故以json形式截取
    for item in data:
        yield{ #该方法返回一个字典
            'comment':item['content'],
            'date':item['time'].split(' ')[0],
            'rate':item['score'],
            'city':item['cityName'],
            'nickname':item['nickName']
        }

#保存数据到文本文档
def save_to_txt():
    exist=set()
    for i in range(1, 500):
        url='http://m.maoyan.com/mmdb/comments/movie/341516.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        print('正在保存第%d页.'% i)
        for item in parse_one_page(html):
            with open('movie-reviews.txt','a',encoding='utf-8') as f:
                item=item['date'] + ',' + item['nickname'] + ',' + item['city'] + ',' +str(item['rate'])+','+item['comment']+'\n'
                if item not in exist:
                    f.write(item)
        #反爬
        time.sleep(5 + float(random.randint(1,100)) /20)

if __name__ =='__main__':
    save_to_txt()
