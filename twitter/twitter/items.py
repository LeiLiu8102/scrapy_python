# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProfileItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Tweets = scrapy.Field()
    Following = scrapy.Field()
    Followers = scrapy.Field()
    Moments = scrapy.Field()
    Lists = scrapy.Field()
    Likes = scrapy.Field()

class TabItem(scrapy.Item):
    username = scrapy.Field()
    tab = scrapy.Field()


