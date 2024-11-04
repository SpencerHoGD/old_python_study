
import scrapy


class ProvinceSpider(scrapy.Spider):
    name = 'test1'

    start_urls = [
        'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/13/1306.html',
        # 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html',
    ]


    # def parse(self, response):
    #     year = response.url.split("/")[-3]
    #     filename = 'stats-%s.html' % year
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    # def parse(self, response):
    #     # for county in response.css('td table.countytable tbody tr.countytr'):
    #     for county in response.css('tr.countytr'):
    #         yield {
    #             # 'county': county.css('td a::text').get(),
    #             # 'link': county.css('td a::attr(href)').get(),
    #             # 'code': county.css('td a::text')[0].get(),
    #             # 'county': county.css('td a::text')[1].get(),
    #             # 'link': county.css('td a::attr(href)')[0].get(),
    #             # 'class': 'county'
    #             'code': county.css('td a::text').get(),
    #             'county': county.css('td a::text').get(),
    #             'link': county.css('td a::attr(href)').get(),
    #             'class': 'county'
    #         }

    # def parse(self, response):
    #     for county in response.xpath('//tr[@class="countytr"]'):
    #         yield {
    #             'code': county.xpath('td[1]/a/text()').get(),
    #             'county': county.xpath('td[2]/a/text()').get(),
    #             'link': county.xpath('td[1]/a/@href').get(),
    #         }


    def parse(self, response):
        # for county in response.css('td table.countytable tbody tr.countytr'):
        for county in response.xpath('//tr[@class="countytr"]'):
            if county.xpath('.//td/a/text()') is not None:
                yield {
                    'code': county.xpath('td[1]/text()').get,
                    'link': county.xpath('td[1]/@href').get(),
                    'county': county.xpath('td[2]/text()').get(),
                    'class': 'county'
                }
            else:
                yield {
                    'code': county.xpath('td[1]/a/text()').get(),
                    'link': county.xpath('td[1]/a/@href').get(),
                    'county': county.xpath('td[2]/a/text()').get(),
                    'class': 'county'
                }
