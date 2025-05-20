import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class LoginCodeSpider(scrapy.Spider):
    name = "login_code"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]


    def parse(self, response):
        return FormRequest.from_response(
            response,
            formdata= {'username': 'admin', 'password': 'password'},
            callback= self.after_login
        )
    
    
    def after_login(self, response):
        if "Logout" not in response.text:
            self.logger.error("\nLogin Failed!\n")
            return
        
        self.logger.info("\nLogin Successful!\n")
        
        yield scrapy.Request(
            url='https://quotes.toscrape.com/',
            callback=self.parse_quotes,
            dont_filter=True
        )
    
    
    def parse_quotes(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text' : quote.css('span.text::text').get(),
                'author' : quote.css('small.author::text').get(),
                'tags' : quote.css('div.tags a.tag::text').getall()
            }
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_quotes)