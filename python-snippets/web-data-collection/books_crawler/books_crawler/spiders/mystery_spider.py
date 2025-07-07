import scrapy

# Define a new Scrapy Spider class


class MysterySpider(scrapy.Spider):
    # Unique name to run the spider from command line
    name = "mystery_spider"

    # Domain(s) the spider is allowed to crawl
    allowed_domains = ["books.toscrape.com"]

    # Starting point of the crawl
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        """
        This is the default callback for the initial request to start_urls.
        It looks for all genre links in the sidebar, filters out the one
        labeled 'Mystery', and follows its link.
        """
        # Select all <a> tags inside the sidebar's genre list
        genre_links = response.css("div.side_categories a")

        for link in genre_links:
            # Extract the genre name (text), clean it, and convert to lowercase
            genre_name = link.css("::text").get().strip().lower()

            # If the genre is 'mystery', follow that link
            if genre_name == "mystery":
                # Construct the full URL from the relative href
                genre_url = response.urljoin(link.attrib["href"])

                # Follow the link to the Mystery category and use parse_mystery as the callback
                yield response.follow(genre_url, callback=self.parse_mystery)

    def parse_mystery(self, response):
        """
        This method handles pages in the Mystery category.
        It extracts book titles and links on the current page and
        follows the 'next' page if it exists.
        """
        # Select all book blocks on the page
        books = response.css("article.product_pod")

        for book in books:
            # Extract the title from the 'title' attribute of the <a> tag
            title = book.css("h3 a::attr(title)").get()

            # Extract the relative URL and convert it to an absolute URL
            url = response.urljoin(book.css("h3 a::attr(href)").get())

            # Yield a dictionary (this becomes one item in the output file)
            yield {
                "title": title,
                "url": url
            }

        # Check if there's a 'next' button to go to the next page of books
        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            # Build full URL and recursively call this method on the next page
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, callback=self.parse_mystery)
