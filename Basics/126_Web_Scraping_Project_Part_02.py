import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

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
			"text": quote.find(class_="text").get_text(),
			"author":quote.find(class_="author").get_text(),
			"link":quote.find('a')['href']
			})
		nextBtn = soup.find(class_="next")
		url = nextBtn.find('a')['href'] if nextBtn else None 
		# sleep(2)
quote = choice(all_quotes)
remaining_guesses = 4
print("Here's a quote: ")
print(quote['text'])
print(quote['author'])
guess = ''
while guess.lower() != quote['author'].lower() and remaining_guesses > 0:
	guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses}\n")
	if guess.lower() == quote["author"].lower():
		print("YOU GOT IT RIGHT!")
		break
	remaining_guesses -= 1
	if remaining_guesses == 3:
		res = requests.get(f"{base_url}{quote['link']}")
		soup = BeautifulSoup(res.text, 'html.parser')
		birth_date = soup.find(class_="author-born-date").get_text()
		birth_place = soup.find(class_="author-born-location").get_text()
		print(f"Here's a hint: The author was born on {birth_date} {birth_place}")
	elif remaining_guesses == 2:
		print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
	elif remaining_guesses == 1:
		print(f"Here's a hint: The author's last name starts with: {quote['author'].split(' ')[1][0]}")
	else:
		print(f"Sorry you ran out of guesses. The answer was {quote['author']}")