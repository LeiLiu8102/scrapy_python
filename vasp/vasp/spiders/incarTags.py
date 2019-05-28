# -*- coding: utf-8 -*-
import scrapy
from vasp.items import VaspItem


class IncartagsSpider(scrapy.Spider):
    name = 'incarTags'
    # allowed_domains = ['https://cms.mpi.univie.ac.at']
    start_urls = ['https://cms.mpi.univie.ac.at/wiki/index.php?title=Category:INCAR&pageuntil=ML+FF+LMLFF#mw-pages',
                'https://cms.mpi.univie.ac.at/wiki/index.php?title=Category:INCAR&pagefrom=ML+FF+LMLFF#mw-pages']

    def parse(self, response):

        data = VaspItem()

        td = response.xpath('//td')
        for col in td[:]:
            item = col.xpath('./ul/li')
            for tag in item[:]:
                link = tag.xpath('./a/@href').get()
                title = tag.xpath('./a/@title').get()
                data['tag'] = title
                data['link'] = link

                yield data


