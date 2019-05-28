# -*- coding: utf-8 -*-
import scrapy
from twitter.items import ProfileItem
"""
Spider scraping the number of "Following", "Tweets",
"Likes", "Followers", "Moments", and "Lists"
"""

class UserProfileSpider(scrapy.Spider):

    name = 'user_profile'
    allowed_domains = ['twitter.com']
    # The username of the user
    username = 'rihanna'

    # The format of the url of home page
    user_url = "https://twitter.com/{}"

    # Generate the first requests
    def start_requests(self):

        yield scrapy.Request(url = self.user_url.format(self.username),
                    callback = self.parse_users)

    def parse_users(self, response):
        """
        Extract the item from the user_url page.
        """
        item = ProfileItem()
        available_keys = item.fields.keys()
        
        profileNav_labels = response.xpath("//span[@class='ProfileNav-label']")

        for span in profileNav_labels:
            key = span.xpath('./text()').get().strip()
            if key in available_keys:
                value = span.xpath("./../span[@class='ProfileNav-value']/@data-count").get()
                if value and value.isdigit():
                    item[key] = int(value)
        
        print(item)
           
            



        







