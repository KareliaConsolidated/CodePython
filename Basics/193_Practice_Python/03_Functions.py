def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(10, 3)

# Function Header
# Let's start with the function header, which is the first line of a function definition.

# The function header always starts with the def keyword, which indicates that this is a function definition.
# Then comes the function name (here, cylinder_volume), which follows the same naming conventions as variables. You can revisit the naming conventions below.
# Immediately after the name are parentheses that may include arguments separated by commas (here, height and radius). Arguments, or parameters, are values that are passed in as inputs when the function is called, and are used in the function body. If a function doesn't take arguments, these parentheses are left empty.
# The header always end with a colon :.
# Function Body
# The rest of the function is contained in the body, which is where the function does its work.

# The body of a function is the code indented after the header line. Here, it's the two lines that define pi and return the volume.
# Within this body, we can refer to the argument variables and define new variables, which can only be used within these indented lines.
# The body will often include a return statement, which is used to send back an output value from the function to the statement that called the function. A return statement consists of the return keyword followed by an expression that is evaluated to get the output value for the function. If there is no return statement, the function simply returns None.

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

# Variable Scope
# Variable scope refers to which parts of a program a variable can be referenced, or used, from.

# Documentation
# Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings. Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.

def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area
Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose. If you feel that this is sufficient documentation you can end the docstring at this point; single line docstrings are perfectly acceptable, as in the example above.

def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area

# Lambda Expressions
# You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments.

# With a lambda expression, this function:

def multiply(x, y):
    return x * y
# can be reduced to:

multiply = lambda x, y: x * y
# Both of these functions are used in the same way. In either case, we can call multiply like this:

multiply(4, 7)
# This returns 28.    

# Iterators and Generators
# Iterables are objects that can return one of their elements at a time, such as a list. Many of the built-in functions we’ve used so far, like 'enumerate,' return an iterator.

# An iterator is an object that represents a stream of data. This is different from a list, which is also an iterable, but not an iterator because it is not a stream of data.

# Generators are a simple way to create iterators using functions. You can also define iterators using classes, which you can read more about here.

# Here is an example of a generator function called my_range, which produces an iterator that is a stream of numbers from 0 to (x - 1).

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1