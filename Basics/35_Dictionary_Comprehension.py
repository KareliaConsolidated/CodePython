# The Syntax
# { __:__ for __ in __ }
# Iterates over keys by default
# To iterate over keys and values using .items()
numbers = dict(first=1, second=2, third=3)

squared_numbers = {key:value**2 for key,value in numbers.items()}

print(squared_numbers)
 
# Another Example
print({num: num**2 for num in [1,2,3,4,5]})

str1 = "ABC"
str2 = "123"
print({str1[i]:str2[i] for i in range(0,len(str1))})

# Conditional Logic with Dictionaries
num_list = [1, 2, 3, 4]
print({num:("even" if num % 2 == 0 else "odd") for num in num_list})

course = {
	"name":"Python",
	"duration":5,
	"editor":"Sublime"
}
print({(k.upper() if k is 'editor' else k):str(v).upper() for k,v in course.items()})

abbr = ["CA", "NJ", "RI"]
state = ["California", "New Jersey", "Rhode Island"]
print({abbr[i]:state[i] for i in range(0,len(abbr))}) # {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}

# Using Zip
print(dict(zip(abbr,state)))

# List to Dictionary Exercise
person = [["name","John"], ["job", "Data Scientist"], ["city", "Berlin"]]

# Way 01
print({thing[0]:thing[1] for thing in person})

# Way 02
print({k:v for k,v in person})

# Way 03
print(dict(person))

# Create a dictionary with the key as a vowel in the alphabet and the value as 0.
print({}.fromkeys('aeiou',0))

# Using Dict Comprehension
print({char:0 for char in 'aeiou'})

# Your Task is to create dictionary that maps ASCII keys to their corresponding letters.
print({char:chr(char) for char in range(65,91)}) # {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}