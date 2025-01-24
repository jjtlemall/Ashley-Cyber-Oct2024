# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Get the total number of names in the list
num_names = len(names)

# Select a random index
random_index = random.randint(0, num_names - 1)

# Get the name at the random index
payer = names[random_index]

# Print the result
print(f"{payer} is going to buy the meal today!")

