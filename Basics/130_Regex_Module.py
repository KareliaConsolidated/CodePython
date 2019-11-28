# import regex module
import re

# define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search a string with our regex
res = pattern.search('Call me at 950 555-5656 or 950 555-6565')

print(res) # <re.Match object; span=(11, 23), match='950 555-5656'>

print(res.group()) # 950 555-5656

# Return all 
res = pattern.findall('Call me at 950 555-5656 or 950 555-6565')

print(res) # ['950 555-5656', '950 555-6565']