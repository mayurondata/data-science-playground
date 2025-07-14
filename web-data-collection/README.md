# Web Data Collection

- This module demonstrates the foundational and practical techniques for acquiring data from the web using Python.

- It combines conceptual explainers with hands-on implementations to build a clear understanding of modern web data pipelines.

## Core Components

- **Web Crawling** (Scrapy)  
  Learn how to systematically traverse websites and extract links, page data, and content using the Scrapy framework.

- **Web Scraping** (Selenium)  
  Extract structured information from static and dynamically rendered pages (including JavaScript-based content) using browser automation.

- **Working with APIs**  
  Understand how to retrieve, parse, and work with data from public APIs (e.g., Open Library API), including authentication, response parsing, and error handling.

## Structure

This repository is organized to separate conceptual learning from implementation:

| Folder             | Description                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| `books_crawler/`   | Scrapy-based spider project for crawling book listings.                 |
| `books_scaper/`    | Standalone script for scraping book data.                               |
| `fetch_book_data/` | Script to fetch book data from Open Library API using `requests`.       |
| `explainers/`      | Supporting documentation and conceptual overviews.                      |
| `apriori.md`       | Foundational concepts: HTTP, URLs, HTML, CSS selectors, API principles. |
| `notes.md`         | Notes on APIs and scraping — to be expanded.                            |

## Goal

To provide a unified resource that bridges theoretical understanding with practical tools for collecting structured data from the web.
