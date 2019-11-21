# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')
with open('Datasets/blog_data.csv', 'w') as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["Title, Link, Date"])
	for article in articles:
		a_tag = article.find('a')
		Title = a_tag.get_text()
		Link = a_tag['href']
		Date = article.find('time')['datetime']
		csv_writer.writerow([Title, Link, Date])
