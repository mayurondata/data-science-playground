# Notes on Web Crawling, Scraping, and APIs

This note captures my current understanding and reflections on web crawling, web scraping, and working with APIs. These concepts are explored through hands-on experiments in the `web-data-collection` directory.

---

## Web Crawling vs Web Scraping (My Perspective)

- **Web Crawling**  
  Crawling is the process of discovering and navigating through links on a website, starting from an entry point (like a homepage or category page).  
  The goal is to map the site structure or collect URLs of interest — for example, gathering all book URLs from the "Mystery" section on [books.toscrape.com](http://books.toscrape.com).

- **Web Scraping**  
  Scraping involves extracting specific information from the individual pages discovered via crawling.  
  This usually includes pulling structured data like titles, prices, images, and descriptions.

---

## When They Work Together

In practice, crawling and scraping often work hand-in-hand:

1. Use a crawler to collect relevant links.
2. Use a scraper to extract structured content from those links.

In my project:

- I used **Scrapy** to crawl book URLs from the Mystery category.
- I then used **Selenium** to scrape detailed data from those book pages.

---

## Understanding the Website Structure

One key takeaway:

> To scrape or crawl effectively, you must understand how data is structured in the site's HTML.

This includes:

- Identifying key HTML tags, classes, and IDs
- Understanding pagination and nested content
- Building accurate and robust CSS or XPath selectors

Useful tools:

- Browser Developer Tools (Inspect Element)
- Real-time page inspection while debugging
- Manual testing of selectors before automation

---

## Notes on Working with APIs

I have also implemented API-based data collection, including working with the **Open Library API**.

### Key Concepts and Observations:

- **REST APIs vs Scraping**
  APIs provide structured access to data directly from the server, without relying on HTML parsing. This is often more efficient and stable than scraping.

- **Authentication**
  Some APIs are public (like Open Library), while others require authentication via API keys, tokens, or OAuth.

- **Pagination and Rate Limiting**
  Many APIs paginate results or enforce limits on the number of requests per time period. Understanding headers, status codes, and backoff strategies is critical.

- **Data Format**
  JSON is the standard format for most APIs. Navigating nested JSON structures is key for extracting useful information.

- **Error Handling**
  Always check response codes, handle timeouts, and build retry logic for robustness.

---

## Final Thoughts

This note reflects how I currently understand and apply web crawling, scraping, and API-based data collection in my projects. The distinctions between them are important, but in practice, they often complement one another within a larger data acquisition workflow.
