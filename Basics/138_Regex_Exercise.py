# Regex Profanity Filter
# Define a function called censor that accepts a single string, Rather than censoring any real profanity, we're going to censor any words that start with "frak". This includes "fracking", " fracker", "frack", etc. Replace the entire word with the string "CENSORED". Regex should be case insensitive.
import re

def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)

print(censor("Frack You!")) # CENSORED You!
print(censor("I Hope you Fracking Die!")) # I Hope you CENSORED Die!
print(censor("You Fracking Frack")) # You CENSORED CENSORED