# Web Scraping
# Web Scraping involves programmatically grabbing data from a web page.

# Why Scrape?
# There's data on a site that you want to store or analyze.
# You can't get by other means (e.g. an API)
# You want to programmatically grab the data (instead of lots of manual copying/pasting)

# Is it...OK?
# Some websites don't want people scraping them.
# Best practice: Consult the robots.txt file
# If making many requests, time them out
# If you're too aggressive, your IP can be blocked.

# Getting Started with Beautiful Soup
# To extract data from HTML, we'll use Beautiful Soup
# Install it with pip
# Beautiful Soup lets us navigate through HTML with Python
# Beautiful Soup doesn NOT download HTML, for this, we need to requests module! 

# Parsing and Navigating HTML
# BeautifulSoup(html_string, "html.parser") - parse HTML
# Once Parsed, There are several ways to navigate:
	# By Tag Name
	# Using find - returns one matching tag
	# Using find_all - returns a list of matching tags
from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
print('######### ALL HTML ############')
print(soup)
print(type(soup))
print('######### HTML BODY ############')
print(soup.body)
print('######### HTML BODY DIV ############')
print(soup.body.div)
print('######### HTML FIND DIV ############')
print(soup.find("div"))
print('######### HTML ALL FIND DIV ############')
print(soup.find_all("div"))
print('######### HTML FIND ID ############')
print(soup.find(id="first"))
print('######### HTML FIND ALL CLASS ############')
print(soup.find_all(class_="special"))
print('######### HTML FIND ALL DATA-ATTRIBUTES ############')
d = soup.find_all(attrs = {"data-example": "yes"})
print(d)