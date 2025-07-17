# Fetch Book Data by ISBN

This project demonstrates how to access structured book information from the [Open Library API](https://openlibrary.org/developers/api) using Python's `requests` module.

Unlike traditional web scraping, this script retrieves data directly from Open Library’s backend service through a documented public API.

---

## What It Does

- Accepts an ISBN number as input from the user
- Sends a GET request to Open Library’s API endpoint
- Retrieves book data in JSON format
- Saves the response to a file called `book_data.json`

This is a practical example of how to work with RESTful APIs and JSON in Python.

---

## How to Run

1. Install `requests` (if not already installed)

   ```bash
   pip install requests
   ```

2. Run the script

   ```bash
   python fetch_book_data.py
   ```

3. Enter a valid ISBN when prompted.

   Example:

   ```bash
   Enter ISBN: 9780142410370
   ```

4. If successful, the output will be saved to `book_data.json` in the current directory.

---

## Example Output

```json
{
  "title": "Matilda",
  "authors": [
    {
      "key": "/authors/OL34184A",
      "name": "Roald Dahl"
    }
  ],
  "publish_date": "1988",
  "number_of_pages": 240,
  ...
}
```

---

## Notes

- The script uses the Open Library API endpoint:
  `https://openlibrary.org/isbn/{isbn}.json`
- This is **not web scraping**. It is structured API access as per [Open Library’s developer guidelines](https://openlibrary.org/developers/api).

---

## Resources

- [Open Library API Docs](https://openlibrary.org/developers/api)
- [requests documentation](https://docs.python-requests.org/en/latest/)
- [Understanding JSON](https://www.w3schools.com/js/js_json_intro.asp)
