import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = 'http://quotes.toscrape.com'
url = '/page/1/'
all_quotes = []
while url:
	response = requests.get(f"{base_url}{url}")
	print(f"Now Scraping {base_url}{url}....")
	soup = BeautifulSoup(response.text, 'html.parser')
	quotes = soup.find_all(class_="quote")
	for quote in quotes:
		all_quotes.append({
			"text": quote.find(class_="text"),
			"author":quote.find(class_="author"),
			"link":quote.find('a')['href']
			})
		nextBtn = soup.find(class_="next")
		url = nextBtn.find('a')['href'] if nextBtn else None 
		# sleep(2)
print(all_quotes)