# LC with Conditional Logic
numbers = [1, 2, 3, 4, 5, 6]
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens)
print(odds)

# Conditions with else
print([num*2 if num % 2 == 0 else num/2 for num in numbers])

with_vowels = "This is so much fun!"
print(''.join([char for char in with_vowels if char not in 'aeiou']))


# Given two lists [1,2,3,4] and [3,4,5,6], create a variable called answer, which is a new list that is the intersection of the two. Your output should be [3, 4].
answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
print(answer)

# Given a list of words ["Elie", "Tim", "Matt"] create a variable called answer2, which is a new list with each word reversed and in lower case (use a slice to do the reversal)
answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]
print(answer2)

# For all the numbers between 1 and 100(including 100), create a variable called answer3, which contains a list with all the numbers that are divisible by 12 (12, 24 etc)
print([num for num in range(1,101) if num % 12 == 0])

# Given the string 'amazing', create a variable called answer4, which is a list containing all the letters from "amazing" but not the vowels. The answer should look like ['m','z','n','g']
print([char for char in 'amazing' if char not in 'aeiou'])