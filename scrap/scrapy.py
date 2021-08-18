import scrapy

class BlogSpider(scrapy.Spider):
    name='blogspider'
    allowed_domains = ['https://www.zyte.com/blog/']
    start_urls = ['https://www.zyte.com/blog/']
    def parse(self, response):
        print(response)
        for title in response.css('.oxy-post-title'):
            yield {'title': title.css('::text').get()}

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
