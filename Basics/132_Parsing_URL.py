import re
pattern = re.compile('(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
res = pattern.search('http://www.google.com/search')
if res.group():
	print(True)
else: print(False)
print(res.group()) # http://www.google.com/search
print(res.groups()) # ('http', 'www.google.com', '/search')
print(res.group(0)) # http://www.google.com/search
print(f"Protocol: {res.group(1)}") # http
print(f"Domain: {res.group(2)}") # www.google.com
print(f"Everything Else: {res.group(3)}") # /search