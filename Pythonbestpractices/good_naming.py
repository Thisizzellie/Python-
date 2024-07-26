"""
Rename the following variables and function names to make them more Pythonic. 
"""

## 1 - Unclean Version 
var = input("What is your first name? ")

# - Revised Version
# Descriptive name
First_name = input("What is your first name? ")
#Why 
#The revised version is better for the following reasons:
#Clearer Variable Name: Using first_name instead of var makes it immediately clear what the variable represents. Good variable names improve code readability and maintainability.

#Polite and Complete Prompt: "Please enter your first name:" is more polite and specific than "What is your first name?". It provides a clear instruction to the user about what is expected. These small improvements make the code more professional and user-friendly.



# 2 - Unclean Version 
lastName = "Johnson"

# - Revised Version
#snake_case
Last_Name = "Johnson"
#Why
#Proper Variable Naming: Using last_name instead of lastName follows the common Python convention of using snake_case for variable names. This enhances readability and consistency with other Python code.
#Correct Assignment: Using the = operator correctly assigns the string "Johnson" to the variable last_name. In the original version, and is a logical operator and would cause a syntax error in this context.



# 3 - Unclean Version 
MovieTitle = "Pulp Fiction"
Movie_Title = ....

# - Revised Version
#  - snake_case (could even be just "movie")
movie_title = "Pulp Fiction"


# 4 - Unclean Version 
l = ["Windows", "Linux", "MacOS"]

# 5 - Unclean Version 
actrs = ["Tom Hanks", "Brad Pitt", "Johnny Depp"]

# - Revised Version 

# 6 - Unclean Version 
list_of_fruits = ["apple", "banana", "kiwi", "orange"]

# 7 - Unclean Version 
grades_dict = {"English": 90, "Biology": 80, "Math": 100}


# 8 - Unclean Version 
def convTemp(celcius):
    """Return temperature converted from Celsius to Fahrenheit"""
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit


# 9 - Unclean Version 
class electricvehicle:

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
