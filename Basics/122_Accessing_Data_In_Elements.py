# Accessing Data in Elements
# get_text - access the inner text in an Element
# name - tag name

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

soup = BeautifulSoup(html, "html.parser")
d = soup.select('.special')[0]
print(d.get_text())
# Can also Loop over all special class texts
for el in soup.select('.special'):
	print(el.get_text())
	print(el.name)
	print(el.attrs)

attr = soup.find("div")['id']
print(attr)