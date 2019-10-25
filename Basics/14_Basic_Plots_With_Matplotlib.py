import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]

pop = [2.519, 3.692, 5.263, 6.972]

# Line Plot
plt.plot(year,pop)

# Scatter Plot
plt.scatter(year,pop)
plt.show()

# When you have a time scale along the horizontal axis, the line plot
# is your friend. But in many other cases, when you're trying to assess if there's a 
# correlation between two variables, For Example, the scatter plot is the better choice.
