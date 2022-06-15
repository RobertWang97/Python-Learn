import scrapy


class MyQuotes(scrapy.Spider):
    name = "myquotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
