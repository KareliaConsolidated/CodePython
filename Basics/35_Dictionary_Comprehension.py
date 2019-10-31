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