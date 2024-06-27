import scrapy

class SvetnewparseSpider(scrapy.Spider):
    name = "svetnewparse"
    allowed_domains = ["https://ami.by"]
    start_urls = ["https://ami.by/catalog/tablelamps.html",
                  "https://ami.by/catalog/floorlamps.html",
                  "https://ami.by/catalog/photographyequipment.html",
                  "https://ami.by/catalog/flashlights.html",
                  "https://ami.by/catalog/gardenlamps.html"
                  ]



    def parse(self, response):

        try:
            lamps = response.css('div.item_new')
            for lamp in lamps:
                name = lamp.css('div.itemtitle a::text').get()
                price = lamp.css('div.Price span.digitsGroup2::text').get() + '.' + lamp.css(
                    'div.Price span.digitsGroup3::text').get()
                url = lamp.css('div.itemtitle a').attrib['href']

                yield {
                    'name': name,
                    'price': price,
                    'url': url
                }

        except:
            print('Произошла ошибка при парсинге')






