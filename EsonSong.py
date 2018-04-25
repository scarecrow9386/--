# coding=utf-8

import requests
import json
from pyecharts import Bar

from wordcloud import WordCloud
import matplotlib.pyplot as plt


url='http://music.163.com/weapi/v1/resource/comments/R_SO_4_520581566?csrf_token='

headers={
    'Host':'music.163.com',
    'Origin':'http://music.163.com',
    'Referer':'http://music.163.com/song?id=520581566',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.3964.2 Safari/537.36'
}


#加密数据，直接拿过来用
user_data ={
    'params': 'vRlMDmFsdQgApSPW3Fuh93jGTi/ZN2hZ2MhdqMB503TZaIWYWujKWM4hAJnKoPdV7vMXi5GZX6iOa1aljfQwxnKsNT+5/uJKuxosmdhdBQxvX/uwXSOVdT+0RFcnSPtv',
    'encSecKey': '46fddcef9ca665289ff5a8888aa2d3b0490e94ccffe48332eca2d2a775ee932624afea7e95f321d8565fd9101a8fbc5a9cadbe07daa61a27d18e4eb214ff83ad301255722b154f3c1dd1364570c60e3f003e15515de7c6ede0ca6ca255e8e39788c2f72877f64bc68d29fac51d33103c181cad6b0a297fe13cd55aa67333e3e5'
}


response = requests.post(url,headers = headers, data = user_data)

data = json.loads(response.text)
hotcomments =[]
for hotcomment in data['hotComments']:
    item= {
        'nickname':hotcomment['user']['nickname'],
        'content':hotcomment['content'],
        'likedCount':hotcomment['likedCount']
    }
    hotcomments.append(item)

#获取评论的用户，内容，以及对应的获赞数
content_list =[content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]


bar = Bar("热评中点赞数示例图")
bar.add("点赞数",nickname,liked_count,is_stack =True,mark_line =["min","max"],mark_point =["average"])
bar.render()



content_text = " ".join(content_list)
wordcloud = WordCloud(font_path=r"C:\simhei.ttf",max_words=200).generate(content_text)
plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
