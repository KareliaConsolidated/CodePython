# Built-in modules come with python 
# External modules are downloaded from the internet
# You can download external modules using pip

# pip
# As 3.4, comes with Python by default
# python3 -m pip install NAME_OF_PACKAGE
from termcolor import colored

print(colored("HI THERE!", color="cyan", on_color = "on_magenta", attrs = ["blink"]))