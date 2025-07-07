# Mystery Book Scraper (Selenium-Based)

This project uses Selenium to scrape detailed information about books from the "Mystery" category on books.toscrape.com.

It uses a list of pre-crawled book URLs (from the Scrapy crawler) and visits each page to extract rich information — making it a pure scraping task.

---

## What It Does

- Reads a list of Mystery book URLs from a JSON file (from the crawler).
- For each book URL:
  - Opens the page using a headless browser
  - Extracts:
    - Title
    - Price
    - Availability
    - Description (if available)
- Saves the collected data to a new JSON file

---

## Prerequisites

1. Python (3.7+)
2. Selenium
3. Chrome browser
4. ChromeDriver (must match your Chrome version)

Install Selenium:

```bash
pip install selenium
```

---

## ChromeDriver Setup

Download the correct ChromeDriver for your browser version:
[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

➡ To check your Chrome version:

- Open Chrome
- Go to `chrome://settings/help`

➡ Place the downloaded `chromedriver.exe` in a known location.

➡ For help with setup:
Watch this guide: [https://youtu.be/4gJAAeEPxFo?si=rVHKVOfCl3QZkptK](https://youtu.be/4gJAAeEPxFo?si=rVHKVOfCl3QZkptK)

---

## How to Run

1. Update the following two paths in `scrape_from_urls.py`:

   - Path to `chromedriver.exe`
   - Path to `mystery_books.json` (input)

2. Run the script:

```bash
python scrape_from_urls.py
```

3. Output will be saved to:

```
mystery_books_detailed.json
```

---

## Output Example

```json
{
  "title": "Sharp Objects",
  "price": "£47.82",
  "availability": "In stock (20 available)",
  "description": "Gillian Flynn’s debut novel...",
  "url": "http://books.toscrape.com/catalogue/sharp-objects_997/index.html"
}
```

---

## Resources

- Selenium Docs: [https://www.selenium.dev/documentation/webdriver/](https://www.selenium.dev/documentation/webdriver/)
- ChromeDriver Download: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- Setup Help Video: [https://youtu.be/4gJAAeEPxFo?si=rVHKVOfCl3QZkptK](https://youtu.be/4gJAAeEPxFo?si=rVHKVOfCl3QZkptK)
