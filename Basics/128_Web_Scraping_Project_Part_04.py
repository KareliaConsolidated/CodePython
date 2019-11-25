import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv import DictWriter
BASE_URL = 'http://quotes.toscrape.com'

def scrape_quotes():
	all_quotes = []
	url = '/page/1/'
	while url:
		response = requests.get(f"{BASE_URL}{url}")
		# print(f"Now Scraping {BASE_URL}{url}....")
		soup = BeautifulSoup(response.text, 'html.parser')
		quotes = soup.find_all(class_="quote")
		for quote in quotes:
			all_quotes.append({
				"text": quote.find(class_="text").get_text(),
				"author":quote.find(class_="author").get_text(),
				"link":quote.find('a')['href']
				})
			nextBtn = soup.find(class_="next")
			url = nextBtn.find('a')['href'] if nextBtn else None 
			sleep(1)
	return all_quotes

# Write quotes to csv file
def write_quotes(quotes):
	with open('Datasets/quotes.csv', 'w') as file:
		headers = ['text', 'author','link']
		csv_writer = DictWriter(file, fieldnames = headers)
		csv_writer.writeheader()
		for quote in quotes:
			csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)