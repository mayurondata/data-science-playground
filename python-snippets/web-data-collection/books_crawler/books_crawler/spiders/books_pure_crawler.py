import scrapy


class BooksPureCrawler(scrapy.Spider):
    name = "books_pure_crawler"
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # Collect all book page URLs
        book_links = response.css(
            'article.product_pod h3 a::attr(href)').getall()

        for link in book_links:
            yield {'book_url': response.urljoin(link)}

        # Follow the pagination link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
