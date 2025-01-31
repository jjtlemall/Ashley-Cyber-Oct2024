# Create a program using maths and f-Strings that tells us how many
# days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message
# with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

import math
max_age= 90
# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = max_age - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days left, {weeks_left} weeks left, and {years_left} years left. ")




