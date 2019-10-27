# While Loop Continue to execute while a certain condition is truthy, and will end when they become falsy. 
# user_response = None
# while user_response != "please":
# 	user_response = input("Ah ah ah, you didn't say the magic word: ")
# While Loop require more careful setup than for loops, since you have to specify the termination condition manually.

msg = input("What's your Secret Password? ")

while msg != "dragon":
	print("WRONG !")
	msg = input("What's your Secret Password? ")
print("CORRECT !")

# Changing For Loop to While Loop
for num in range(1,11):
	print(num)

num = 1
while num < 11:
	print(num)
	num += 1