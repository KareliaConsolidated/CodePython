# Navigating with CSS Selectors
# select - returns a list of elements matching a CSS selector
# Selector Cheatsheet
# Select by id of foo: #foo
# Select by class of bar: .bar
# Select children: div > p
# Select descendents: div p


# SELECT ALWAYS RETURNS A LIST

soup = BeautifulSoup(html, "html.parser")
d = soup.select("#first")[0] # To Get Data From the List
print('######### CSS SELECT ID ############')
print(d)
print('######### CSS SELECT CLASS ############')
d = soup.select(".special")
print(d)
print('######### CSS SELECT DIV ############')
d = soup.select("div")
print(d)
print('######### CSS SELECT ATTRIBUTES ############')
d = soup.select("[data-example]")
print(d)