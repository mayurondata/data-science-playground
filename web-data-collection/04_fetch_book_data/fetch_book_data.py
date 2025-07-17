import requests  # requests is the HTTP client (acts like the waiter)
import json


def fetch_book_data(isbn):
    """
    Fetch book data from the Open Library API.
    Enhanced error handling for common issues.

    Note:
    This script is using the Open Library API because it programmatically sends an HTTP request
    to a documented API endpoint — https://openlibrary.org/isbn/{isbn}.json — and receives
    structured data (JSON) in response.

    This is not scraping a webpage. It is accessing Open Library's backend service in the intended way,
    as documented at https://openlibrary.org/developers/api(API documentation).
    """

    # API endpoint (this is like the specific item on the menu you're ordering)
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    # Here:
    # - The **base URL** is "https://openlibrary.org"
    # - The **endpoint** is "/isbn/{isbn}.json", which gives book details by ISBN

    try:
        # Sending an HTTP GET request (this is the order being sent to the kitchen)
        # requests (the waiter) takes the order
        response = requests.get(url, timeout=10)

        # Checks if the response is successful (like confirming if the kitchen accepted the order)
        response.raise_for_status()

        # Parsing the JSON response (this is the meal being served — structured data)
        book_data = response.json()

        # Saving the data to a file (like storing the meal to-go)
        with open("book_data.json", "r+", encoding="utf-8") as f:
            json.dump(book_data, f, indent=4)

        print("Success! Data saved to 'book_data.json'")
        return book_data

    except requests.exceptions.RequestException as e:
        # Handles issues like network failure, timeout, or 4XX/5XX errors
        print(f"Request failed: {e}")
    except json.JSONDecodeError:
        # Handles non-JSON responses
        print("Error: Invalid API response (not JSON).")
    except Exception as e:
        # Handles any other unexpected errors
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Input from the user (you deciding what item to order)
    isbn = input("Enter ISBN: ").strip()
    fetch_book_data(isbn)
