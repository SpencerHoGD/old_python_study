import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
from WeixinSpider.HTML2doc import MyHTMLParser
 
class WeixinSpider(object):
 
    def __init__(self, gzh_name, pageno,keyword):
        self.GZH_Name = gzh_name
        self.pageno = pageno
        self.keyword = keyword.lower()
        self.page_url = []
        self.article_list = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
        self.timeout = 5
        # [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
        # re+	匹配1个或多个的表达式。
        self.pattern = r'[\\/:*?"<>|\r\n]+'

    def get_page_url(self):
        for i in range(1,self.pageno+1):
            # 起始地址
            url = "https://weixin.sogou.com/weixin?query=%s&_sug_type_=&s_from=input&_sug_=n&type=2&page=%s&ie=utf8" \
                    % (quote(self.GZH_Name),i)
            self.page_url.append(url)

    def get_article_url(self):
        article = {}
        for url in self.page_url:
            response = requests.get(url,headers=self.headers,timeout=self.timeout)
            result = BeautifulSoup(response.text, 'html.parser')
            articles = result.select('ul[class="news-list"] > li > div[class="txt-box"] > h3 > a ')
            for a in articles:
                # print(a.text)
                # print(a["href"])
                if self.keyword in a.text.lower():
                    new_text=re.sub(self.pattern,"",a.text)
                    article[new_text] = a["href"]
                    self.article_list.append(article)



headers = {'User-Agent':
                        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
timeout = 5
gzh_name = 'Gu的每日复盘'
My_GZH = WeixinSpider(gzh_name,5,'pytest')
My_GZH.get_page_url()
# print(My_GZH.page_url)
My_GZH.get_article_url()
# print(My_GZH.article_list)
for article in My_GZH.article_list:
    for (key,value) in article.items():
        url=value
        html_response = requests.get(url,headers=headers,timeout=timeout)
        myHTMLParser = MyHTMLParser(key)
        myHTMLParser.feed(html_response.text)
        myHTMLParser.doc.save(myHTMLParser.docfile)