# PDB : Python Debugger
# To set breakpoints in our code we can use pdb by inserting this line:
# import pdb;
# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)
first = "First"
second = "Second"
# pdb.set_trace()
result = first + second
third = "Third"
result += third
print(result)

# Be careful with variable names!
def add_numbers(a, b, c, d):
    # import pdb; pdb.set_trace() 
    return a + b + c + d
add_numbers(1,2,3,4)

# Exercise
def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total

print(divide(4,2)) # 2
print(divide([],"2")) # Please provide two integers or floats
print(divide(1,0)) # Please do not divide by zero
