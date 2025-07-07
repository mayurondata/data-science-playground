# Notes on Web Crawling, Scraping, and APIs

This note captures my current understanding and reflections on web crawling, web scraping, and (eventually) working with public or private APIs. These concepts are explored through hands-on experiments in the `web-data-collection` folder.

---

## Web Crawling vs Web Scraping — My Perspective

- **Web Crawling**  
  Crawling is the process of navigating and discovering links/pages from a given starting point (usually a homepage or category page).  
  The goal is to map out the structure of the site or collect links of interest — for example, gathering all book URLs in the "Mystery" category on [books.toscrape.com](http://books.toscrape.com).

- **Web Scraping**  
  Scraping is the process of extracting specific data from web pages (once discovered).  
  It involves accessing individual URLs and pulling out details like product titles, prices, descriptions, etc.

---

## When They Work Together

In real-world workflows, crawling and scraping are often used together:

1. First, crawl the website to gather all relevant page links.
2. Then, scrape data from each page.

In my example project:

- I used Scrapy to crawl the Mystery book links.
- I then used Selenium to scrape detailed info from those book URLs.

---

## Understanding the Website Structure

A key takeaway:

> You must understand the website’s HTML structure to crawl or scrape effectively.

Whether you’re building a spider or writing selectors, understanding how content is organized in tags, classes, or IDs is essential.

Helpful tools:

- Browser Developer Tools (F12)
- CSS Selectors and XPath
- Manual inspection of pagination, product cards, and metadata

---

## [Placeholder] Notes on Working with APIs

As I begin working with APIs, this section will capture my observations, challenges, and lessons learned.

### Planned Notes:

- Differences between REST APIs and scraping
- Rate limiting, authentication (API keys, OAuth), pagination
- JSON structure navigation
- Common caveats: status codes, headers, retries, error handling
- When to prefer APIs over scraping

> This section will evolve with practical API projects (e.g., fetching weather data, financial info, or GitHub activity).

---

## Final Thoughts

This is how I currently distinguish and understand web crawling, scraping, and API-based collection. Others may describe them differently, but this approach works well for me and reflects how I’ve used them in practice.
