# -*- coding: utf-8 -*-
import scrapy

email= 'liulei18119@gmail.com'
pwd = '4F3D38CA'
myname = 'Larry00Liu'

class LoginSpider(scrapy.Spider):
    name = 'following'
    allowed_domains = ['twitter.com']

    # Start by the login page
    def start_requests(self):
        return [scrapy.Request("https://twitter.com/login?lang=en",
                     meta={'cookiejar': 1}, callback=self.post_login)]

    # Form request
    def post_login(self, response):

        # get the authenticity_token
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').get()

        self.logger.info('authenticity_token=' + authenticity_token)
        
        # set the login headers
        login_headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",                
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded",
                "pragma": "no-cache",
                "origin": "https://twitter.com",
                "referer": "https://twitter.com/login?lang=en",
                }

        # set the form data, e.g., username, pwd
        form_data = {'session[username_or_email]': email, 
                'session[password]': pwd,
                'authenticity_token': authenticity_token,
                'redicrect_agterlogin': "",
                'scribe_log': "",
                'remember_me': '1',
                }

        return [scrapy.FormRequest.from_response(response,
                                          url='https://twitter.com/sessions',
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=login_headers,
                                          formdata=form_data,
                                          callback=self.after_login,
                                          dont_filter=True,
                                          )]

    # After login successfully, parse the home page
    def after_login(self, response):

        if myname in response.text:
            self.logger.info("Log in successfully!")

        username= response.xpath('//style[@class="js-user-style-header-img"]/@id').get().split('-')[-3]

        self.logger.info("username: {}".format(username))

        # The format of url of "following" page
        following_url = "https://twitter.com/{}/following"

        return scrapy.Request(url = self.following_url.format(username),
                    meta={'cookiejar': response.meta['cookiejar']},
                    callback = self.parse_following,
                    dont_filter=True)

    def parse_following(self, response):

        followees = response.xpath('//div[@class="js-stream-item"]')
        for followee in followees:
            username = followee.xpath('./div/@data-screen-name').get()
            self.logger.info(username)


