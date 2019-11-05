# Using the requests Module
# import requests
# url = "https://news.ycombinator.com"
# res = requests.get(url)
# print(f"Your request to {url} came back with status code {res.status_code}")
# print(res.text)

#================= Headers====================#
# import requests
# url = "https://icanhazdadjoke.com"
# # res = requests.get(url, headers = {"Accept": "text/plain"})
# res = requests.get(url, headers = {"Accept": "application/json"})
# data = res.json()
# print(type(res.text)) # type is str
# print(type(res.json())) # type is dict
# print(data) # {'id': 'vk31LJB5Elb', 'joke': 'Why didn’t the orange win the race? It ran out of juice.', 'status': 200}
# print(data['joke']) # How much does a hipster weigh? An instagram.
#================= Headers====================#

#========= Sending Requests with Params =======# 
# What's a Query String?
# A way to pass data to the server as part of a GET request.

import requests
url = "https://icanhazdadjoke.com/search"

response = requests.get(
	url, 
	headers={"Accept": "application/json"},
	params={"term": "cat", "limit": 1}
)

data = response.json()
print(data["results"])

