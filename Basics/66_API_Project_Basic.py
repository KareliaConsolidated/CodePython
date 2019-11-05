import requests
import pyfiglet
from random import choice

print(pyfiglet.figlet_format("DAD Joke 5000"))

term = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"
response_json = requests.get(url, headers = {"Accept" : "application/json"}, params = {"term": term}).json()

results = response_json["results"]
total_jokes = response_json["total_jokes"]

if total_jokes > 1:
	print(f"I've got {total_jokes} jokes about {term}. Here's one:\n{choice(results)['joke']}")
elif total_jokes == 1:
	print(f"I've got one joke about {term}. Here it is:\n",results[0]['joke'])
else:
	print(f"Sorry, I don't have any jokes about {term}! Please try again.")
