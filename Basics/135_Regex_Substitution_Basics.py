import re
text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"
pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) [a-z]+', re.I)
results = pattern.sub("\g<1> REDACTED", text)
print(results)