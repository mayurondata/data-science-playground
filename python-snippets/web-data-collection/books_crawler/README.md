# Mystery Book Crawler

This project is a basic web crawler using [Scrapy](https://scrapy.org/) that collects book titles and URLs from the **"Mystery"** category on [books.toscrape.com](http://books.toscrape.com).

It only crawls listing pages and does not visit individual book detail pages.

---

## What It Does

- Starts from the homepage
- Locates the "Mystery" category from the sidebar
- Crawls through all paginated Mystery pages
- Extracts:
  - Book title
  - Book URL
- Saves the data to a JSON file

## How to Run

1. Install Scrapy
   ```bash
   pip install scrapy
   ```

````

2. Create a Scrapy project

   ```bash
   scrapy startproject books_crawler
   cd books_crawler
   ```

   This creates a project blueprint with folders like `spiders/`, `items.py`, `settings.py`, and more.
   It provides a ready-made structure that makes it easier to organize and manage your crawler code.

3. Generate and edit the spider

   ```bash
   scrapy genspider mystery_spider books.toscrape.com
   ```

   This creates a new spider file inside the `spiders/` folder.
   Replace the contents of `mystery_spider.py` with the crawler code.

4. Run the spider

   ```bash
   scrapy crawl mystery_spider -o mystery_books.json
   ```

   This runs the spider and saves the results to `mystery_books.json`.

---

## Output Example

```json
{
  "title": "Sharp Objects",
  "url": "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
}
```

---

## Resources

[Scrapy Documentation](https://docs.scrapy.org/en/latest/)
[Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
[Scrapy GitHub](https://github.com/scrapy/scrapy)

````
