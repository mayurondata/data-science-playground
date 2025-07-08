import requests
import json


def fetch_book_data(isbn):
    """
    Fetch book data from the Open Library API.
    Enhanced error handling for common issues.
    """
    url = f"https://openlibrary.org/isbn/{isbn}.json"

    try:
        response = requests.get(url, timeout=10)  # Added timeout
        response.raise_for_status()  # Check for HTTP errors

        book_data = response.json()

        with open("book_data.json", "w", encoding="utf-8") as f:
            json.dump(book_data, f, indent=4)

        print("Success! Data saved to 'book_data.json'")
        return book_data

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except json.JSONDecodeError:
        print("Error: Invalid API response (not JSON).")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    isbn = input("Enter ISBN: ").strip()
    fetch_book_data(isbn)
