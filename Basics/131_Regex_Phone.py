import re

def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

print(extract_phone("Call me at 950 555-5656")) # 950 555-5656
print(extract_phone("Call me at 950 555-565622")) # None
print(extract_all_phones("Call me at 950 555-5656 or 950 555-6565")) # None
print(extract_all_phones("Call me at 950 555-565622 or 950 555-6565")) # None

def is_valid_phone(input):
	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
	match = phone_regex.search(input)
	if match:
		return True
	return False

def is_valid_phone_full_match(input):
	phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
	match = phone_regex.fullmatch(input)
	if match:
		return True
	return False

print(is_valid_phone("Call me at 950 555-565622 or 950 555-6565")) # False
print(is_valid_phone("950 555-6565")) # True
print('######  Full Match ######')
print(is_valid_phone_full_match("Call me at 950 555-565622 or 950 555-6565")) # False
print(is_valid_phone_full_match("950 555-6565")) # True