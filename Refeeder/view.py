import feedparser
from django.contrib.syndication.views import Feed
from googletrans import Translator
import re


class ReFeeder(Feed):

    title = u"Elliott Zheng's Refeeder"
    link = "/feeds/"

    description = "Transfor from source to your language"

    def get_object(self, request,src,url):
        self.translator = Translator(service_urls=['translate.google.cn'])
        self.src=src
        self.insert=self.translator.translate("#39898989", src=self.src, dest='zh-cn').text
        print(type(request.get_full_path()))
        url=str(request.get_full_path())

        url=re.findall(r'/rss%3Den%3D([a-zA-z]+://[^\s]*)',url)[0]
        print("url="+url)
        feed=feedparser.parse(url)
        print(len(feed.entries))
        return feed

    def items(self,feed):
        entries=feed.entries
        for entry in entries:
            result=self.translator.translate(entry.title+'#39898989'+entry.summary, src=self.src, dest='zh-cn').text.split(self.insert)
            entry.summary = result[0]
            entry.title = result[1]
            print('yes')
        return entries


    def item_title(self, item):

        return item.title


    def item_description(self, item):
        return  item.summary


    def item_link(self, item):
        return item.id

