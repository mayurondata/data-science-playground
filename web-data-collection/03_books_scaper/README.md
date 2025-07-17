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

## Why Selenium?

Unlike `requests`, which only fetches the static HTML of a page, Selenium controls a real browser and renders the full page including any content loaded via JavaScript.

- `requests` cannot access content that appears after JavaScript execution.
- `selenium` opens the page just like a user would, waits for the browser to load everything, and provides the final rendered version of the page.

Even though books.toscrape.com is mostly static, using Selenium makes the scraping approach robust and adaptable for future work with dynamic websites.

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

To check your Chrome version:

- Open Chrome
- Go to `chrome://settings/help`

Place the downloaded `chromedriver.exe` in a known location.

For help with setup:
[Watch this setup guide](https://youtu.be/4gJAAeEPxFo?si=rVHKVOfCl3QZkptK)

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

## Alternative: Using BeautifulSoup

For scraping static websites, many engineers use the `requests` library along with `BeautifulSoup` because it is lightweight, simple to use, and fast.

### How It Works:

- `requests.get(url)` is used to fetch the raw HTML of the page.
- `BeautifulSoup` parses that HTML and allows you to extract data using tags, CSS selectors, or attributes.

This approach works well when the data is already present in the HTML returned by the server. It is not suitable for pages that load data using JavaScript after the initial page load.

### Key Differences:

| Tool                     | JavaScript Support | Speed  | Best Used For                        |
| ------------------------ | ------------------ | ------ | ------------------------------------ |
| BeautifulSoup + requests | No                 | Faster | Static websites                      |
| Selenium                 | Yes                | Slower | Dynamic or JavaScript-heavy websites |

This project uses Selenium because it simulates a real browser. This makes it suitable for scraping pages that might use JavaScript or require browser-like interaction, even though `books.toscrape.com` is mostly static.

### Official Documentation:

- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

---
