# Randomness has many uses in science, art, statistics, cryptography, gaming, gambling, and other fields. You're going to use randomness to simulate a game.

# All the functionality you need is contained in the random package, a sub-package of numpy. In this exercise, you'll be using two functions from this package:

# seed(): sets the random seed, so that your results are reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
# rand(): if you don't specify any arguments, it generates a random float between zero and one.
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

#=====================================================================#

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

# Numpy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice is [3,4,5] :
    step += 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
