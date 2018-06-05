import feedparser
from django.contrib.syndication.views import Feed
from googletrans import Translator


class ReFeeder(Feed):

    title = u"Elliott Zheng's Refeeder"
    link = "/feeds/"

    description = "Transfor from source to your language"

    def get_object(self, request,src,url):
        print(url)
        self.translator = Translator(service_urls=['translate.google.cn'])
        self.src=src
        return feedparser.parse(url)

    def items(self,feed):
        return feed.entries


    def item_title(self, item):
        return self.translator.translate(item.title, src=self.src, dest='zh-cn').text


    def item_description(self, item):
        print(1)
        return self.translator.translate(item.summary, src=self.src, dest='zh-cn').text


    def item_link(self, item):
        return item.id

