import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup headless Chrome with correct path
options = Options()
options.add_argument("--headless=new")  # Recommended headless mode
driver_path = r"C:\Users\Joshi Mayuresh\Downloads\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Input and output file paths
INPUT_FILE = r"C:\Users\Joshi Mayuresh\Desktop\data-science-playground\python-snippets\web-data-collection\books_crawler\mystery_books.json"
OUTPUT_FILE = "mystery_books_detailed.json"

# Load crawled URLs
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    books = json.load(f)

scraped_books = []

# Loop over URLs and scrape detailed info
for book in books:
    url = book["url"]
    driver.get(url)
    time.sleep(1)  # Let page load

    try:
        title = driver.find_element(By.CSS_SELECTOR, ".product_main h1").text
        price = driver.find_element(By.CSS_SELECTOR, ".price_color").text
        availability = driver.find_element(
            By.CSS_SELECTOR, ".availability").text.strip()

        try:
            description = driver.find_element(
                By.CSS_SELECTOR, "#product_description ~ p").text
        except:
            description = "No description available"

        scraped_books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "description": description,
            "url": url
        })

    except Exception as e:
        print(f"[ERROR] Failed to scrape: {url}\nReason: {e}")

# Close browser
driver.quit()

# Save scraped data
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(scraped_books, f, indent=4)

print(
    f"✅ Scraping completed. {len(scraped_books)} books saved to {OUTPUT_FILE}")
