import scrapy

class TalkSpider(scrapy.Spider):
    name = "talktext"
    start_urls = [
      "https://www.lds.org/general-conference/1972/10/every-man-in-his-own-place?lang=eng"
    ]

    def parse(self, response):
        for item in response.css('section.article-page'):
            yield {
                'date': item.css('div.title-block h2.title::text').extract(), #brittle
                'text': item.css('div.article-content p::text').extract(),
                'author': response.selector.xpath('/html/head/meta[contains(@name, "author")]/@content').extract(),
                'title': response.selector.xpath('/html/head/meta[contains(@property, "og:title")]/@content').extract(),
                'url': response.selector.xpath('/html/head/meta[contains(@property, "og:url")]/@content').extract(),
            }

# Works but only grabs the content.
#    def parse(self, response):
#        for talk in response.css('div.article-content'):
#            yield {
#                'text': talk.css('p::text').extract(),
#            }
