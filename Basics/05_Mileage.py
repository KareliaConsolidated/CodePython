print("How many kilometers did you cycle today?")

kms = input() # Getting User Input

miles = float(kms)/1.60934 # Converting String to Float

print(f"Your {kms} km ride was {round(miles, 2)} mi")