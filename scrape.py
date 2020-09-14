import scrapy
import datetime


class LanguageSpider(scrapy.Spider):
    # Set ID and Time for logging
    scrape_id = 1
    scrape_time = datetime.time

    # For now we start small. We only look at the German Aerospace Center Website in both German and English
    name = 'itsy_bitsy'
    start_urls = ['https://www.dlr.de/DE/Home/home_node.html', 'https://www.dlr.de/EN/Home/home_node.html']

    # Instruct the Spider which passages to extract...

    def parse(self, response):
        # In this case I stuck to paragraphs exclusively. Headings would be another straightforward option.

        paragraphs = response.xpath('//p')

        # Print and log the results
        with open('aerospace.txt', 'w+') as f:
            for par in paragraphs:
                paragraph = par.get()
                print('\n', paragraph, '\n')
                f.write(paragraph)

