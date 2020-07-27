import scrapy


class DmozSpider(scrapy.Spider):  # 继承Spider类
    name = "dmoz"  # 爬虫的唯一标识，不能重复，启动爬虫的时候要用
    allowed_domains = ["toscrape.com"]  # 限定域名，只爬取该域名下的网页
    start_urls = [  # 开始爬取的链接
        "https://www.baidu.com/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]  # 获取url，用”/”分段，获去倒数第二个字段
        print('*'*100 + filename)
        with open(filename, 'a') as f:
            f.write(response.body)  # 把访问的得到的网页源码写入文件
