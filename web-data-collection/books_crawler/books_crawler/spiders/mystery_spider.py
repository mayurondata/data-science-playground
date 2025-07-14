import scrapy

# Define a new Scrapy Spider class

# This spider inherits from scrapy.Spider, which gives it crawling powers.


class MysterySpider(scrapy.Spider):
    # Unique name to run the spider from command line
    name = "mystery_spider"

    # Domain(s) the spider is allowed to crawl
    allowed_domains = ["books.toscrape.com"]

    # Starting point of the crawl
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        """
        This is the first method Scrapy calls after visiting the start URL and getting the response back.
        The response here is not raw HTML, but a parsed object provided by Scrapy, which lets us use
        methods like .css() or .xpath() directly to query elements.

        In this method, we look through all the genre links in the sidebar, and if we find the one labeled
        'Mystery', we follow that link and use the parse_mystery() method to handle that page.
        """

        # Select all <a> tags inside the sidebar's genre list
        genre_links = response.css("div.side_categories a")
        # The response object is the HTTP response that the spider gets after requesting a URL(which is done implicitly)
        # .css(...) is a method provided by Scrapy’s Selector object (like the response object).
        # “Find all anchor (<a>) tags inside the sidebar div labeled with class side_categories.”

        for link in genre_links:
            # Extract the genre name (text), clean it, and convert to lowercase
            genre_name = link.css("::text").get().strip().lower()

            # If the genre is 'mystery', follow that link
            if genre_name == "mystery":
                # The href in each genre link is a relative URL (e.g., "catalogue/category/books/mystery_3/index.html").
                # While a browser can handle relative links by combining them with the current page's URL,
                # Scrapy needs the full (absolute) URL to make a proper request.
                # So we use response.urljoin(...) to build the full URL before following the link.

                # Construct the full URL from the relative href
                genre_url = response.urljoin(link.attrib["href"])

                # Starting from the current page (home_page response), follow the link stored in genre_url.
                # Scrapy will make a new request to that URL (i.e., the Mystery category page).
                # Once the response from that page is received, Scrapy will pass it to the parse_mystery() method for processing.
                # This is controlled using the callback=self.parse_mystery argument.
                # In short: follow the link → wait for the new page → pass its response to parse_mystery() for scraping.

                yield response.follow(genre_url, callback=self.parse_mystery)
                # yield is used to hand over this request to Scrapy’s engine.
                # It tells Scrapy: “Go to this new URL and once you get the response, call the function I gave you.”(parse_mystery)
                # Unlike return, yield doesn’t stop the function — it lets Scrapy keep processing more links or data.

    def parse_mystery(self, response):
        # The response you receive here is the parsed HTML of the Mystery category page
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

            # Extract the relative URL of the book’s detail page and convert it to an absolute URL
            url = response.urljoin(book.css("h3 a::attr(href)").get())
            # ::attr(href) is a Scrapy-specific way of accessing attributes using CSS selectors.

            # Yield a dictionary (this becomes one item in the output file)
            # Why use yield here?
            # Scrapy streams data as it crawls — it doesn't wait to collect all items at once.
            # Each time yield is called, one item is passed to Scrapy’s item pipeline or output file immediately.
            # This makes the spider memory-efficient and suitable for large datasets.

            yield {
                "title": title,
                "url": url
            }

        # -------------------- Pagination Logic --------------------
        # Check if the current page has a "Next" button.
        # We target: <li class="next"><a href="page-2.html">next</a></li>
        # This CSS selector finds the 'href' value of the anchor tag inside the <li class="next">
        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            # Convert the relative next page link (e.g., 'page-2.html') to a full absolute URL
            next_page_url = response.urljoin(next_page)

            # Follow the next page and use the same parsing method (recursive crawl)
            # This keeps crawling until there are no more "next" buttons/pages
            yield response.follow(next_page_url, callback=self.parse_mystery)

        # ----------------------------------------------------------
