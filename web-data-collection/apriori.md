# Apriori

- Foundational Concepts for Understanding Web Data Collection  
  (Covers core ideas needed before learning web crawling, web scraping, and APIs)

---

## 1. What Is the Web?

The web is like a giant library full of connected pages. Each page has its own address called a URL (like `https://example.com`), just like every book has a title.

These pages are written in code (mainly HTML) and can show things like text, pictures, buttons, or links.

When you open a website in your browser, it sends a message to another computer (called a server) asking for the page. That server replies by sending back the page, and your browser shows it to you by rendering it.

This back-and-forth is done using a set of rules called **HTTP**, which makes sure both sides understand each other.

---

## 2. HTML – Structure of Web Pages

HTML stands for HyperText Markup Language. It is used to build the structure and content of web pages.

A web page is made up of elements, written using tags like:

```html
<a href="/book1.html" class="book-link">Book 1</a>
```

Here:

- `<a>` is a tag (for a link)
- `href` is an attribute (holds the link destination)
- `"book1.html"` is the value of the attribute
- class="book-link" assigns the tag a class attribute, which allows it to be targeted using the CSS class selector .book-link.
- `"Book 1"` is the text that will be shown on the page

Important HTML concepts:

- Tags: `<div>`, `<p>`, `<a>`, `<h1>`, `<img>`, `<ul>`, `<li>`, etc.
- Attributes: `href`, `class`, `id`, `src`, `alt`, etc.
- Nesting: HTML elements can be placed inside one another
- DOM (Document Object Model): The browser turns HTML into a tree-like structure we can navigate or inspect

---

## 3. CSS – Styling and Selecting Elements

CSS stands for Cascading Style Sheets. It is used to control the look of a webpage (fonts, colors, layout, etc.). But it also plays a role in helping us locate specific parts of a page.

CSS selectors let us target elements in the HTML by tag, class, ID, or position.

Examples:

- `div`: selects all `<div>` elements
- `.book`: selects anything with class="book"
- `#title`: selects the element with id="title"
- `div.book a`: selects links inside a `<div>` that has class "book"

These selectors help find exactly what we're interested in inside a web page.

---

## 4. HTTP – The Web Communication Protocol

HTTP stands for HyperText Transfer Protocol. It defines how data is shared between your browser and a website.

Whenever you visit a page, your browser sends an HTTP request to a web server, and the server sends back an HTTP response.

This is how all content on the web is sent and received.

---

## 5. HTTP Request

An HTTP request is a message sent by a browser (or any program) to a web server to request or send data.

Parts of an HTTP request:

- **Method**: What kind of action to perform

  - `GET`: Ask for something (like a page)
  - `POST`: Submit data (like a login form)

- **URL**: The address of what you're requesting

- **Headers**: Extra info like what kind of response is expected

- **Body**: Optional data (mainly for methods like POST or PUT)

Example: Visiting `https://example.com/books` sends a `GET` request to that URL.

---

## 6. HTTP Response

An HTTP response is what the server sends back after receiving a request.

Parts of a response:

- **Status Code**: Shows the result

  - `200`: OK
  - `404`: Page not found
  - `403`: Forbidden (access denied)

- **Headers**: Details about the content (like format or length)

- **Body**: The actual content (like an HTML page or other data)

The body is where the useful information lives.

---

## 7. Understanding URLs

A URL (Uniform Resource Locator) is the address of something on the web.

Example:

```
https://example.com/products?page=2
```

Parts:

- `https://`: The protocol being used
- `example.com`: The domain (site’s name)
- `/products`: The path to a specific section or resource
- `?page=2`: A query parameter used to filter or navigate

Every URL tells the browser exactly what to request and how.

---

## 8. Client vs Server

- A **client** is a browser, app, or script that asks for information
- A **server** is a machine that receives the request and sends back a response

The process:

```
Client → sends HTTP Request → Server
Server → sends HTTP Response → Client
```

All websites work using this back-and-forth system.

---

## 9. JavaScript and Dynamic Content

Some web pages don’t include all their content in the first response. Instead, they load it later using JavaScript running in the browser.

This is common on modern sites. For example:

- A browser loads the basic HTML from a site.
- Then JavaScript runs and makes more requests in the background.
- The page updates and fills in more content (like user profiles or job listings).

If you’re looking at the page in a browser, you see everything. But if you're using a tool that just fetches the HTML (like a script or terminal), you might not see the full content — because the JavaScript never ran.

This is called **client-side rendering**, and it's important to know when trying to get information from a page.

---

## 10. Headers and User-Agent

When your browser sends a request to a website, it also sends some extra details called **headers**.

One important header is the `User-Agent`. It tells the server what kind of browser or tool is making the request.

If a request doesn't include a normal User-Agent (like from Chrome or Firefox), some websites might block or ignore it.

Example in code:

```python
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
```

Using proper headers helps you get better and more complete responses from websites.

---

## 11. Session and Cookies

Some websites remember who you are after you log in. They do this using **cookies** — small pieces of data stored in the browser.

Once you're logged in, the server gives your browser a cookie to identify your session. If you want to get content that only logged-in users can see, you'll need to send that cookie with your requests.

Without it, the website may think you're not logged in and show a different or restricted page.

---

## 12. robots.txt – Site Instructions for Automated Tools

Most websites have a file called `robots.txt`. It's a set of rules placed by the site owner to tell automated tools and programs what parts of the site they can or cannot access.

You can see it by visiting:

```

https://example.com/robots.txt

```

Sample contents:

```

User-agent: \*
Disallow: /private/

```

This means that all types of automated programs (like search engine crawlers or scripts that access web pages) should avoid visiting the `/private/` section.

While this file doesn’t technically block access, it's considered good practice to respect it when building or running automated scripts that collect web content.

---

## 13. Rate Limits and Being Polite

Websites can slow down or block users who send too many requests too quickly.

It’s important to:

- Add short delays between requests (`time.sleep(1.5)`)
- Avoid flooding the server
- Respect the site's limits and structure

This helps you stay under the radar and not get blocked.

---

## 14. Static vs Dynamic Pages

Websites can be:

- **Static**: All the data is included in the first page load.
- **Dynamic**: Data is loaded later using JavaScript.

Static pages are simpler to analyze because all the content is visible right away. Dynamic pages may need more advanced tools to access what's hidden behind JavaScript.

---

## 15. A Note on Responsible Access

Some websites may not want you to download their content automatically.

Before accessing any site repeatedly or programmatically:

- Check their `robots.txt`
- Read their Terms of Service
- Only collect what you need, and avoid overloading their servers

It’s always good to act responsibly when working with public web data.

---
