#!/bin/bash
# Create a script that ask the user for a number between 1 and 10.  Have the script tell the user if there
# number is greater than 5, less than 5, or equal to 5.  Please use an if/else or elif statement to make this happen.
# Also put the if/else statemnt inside a function.
# -eq = equal
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)
#Here are some helpful commands to make this happen.


# #!/bin/bash

# # Function to check the number
# check_number() {
#     if [ "$1" -gt 5 ]; then
#         echo "Your number is greater than 5."
#     elif [ "$1" -lt 5 ]; then
#         echo "Your number is less than 5."
#     else
#         echo "Your number is equal to 5."
#     fi
# }

# # Main script
# echo "Please enter a number between 1 and 10:"
# read -r number

# # Check if the input is within the valid range
# if [[ "$number" -ge 1 && "$number" -le 10 ]]; then
#     check_number "$number"
# else
#     echo "Invalid input! Please enter a number between 1 and 10."
# fi
#!/bin/bash

# Function to evaluate the number
evaluate_number() {
	# Ask the user for a number between 1 and 10
	echo "Enter a number between 1 and 10:"
	read number

	# Check if the input is a valid number
	if [[ ! $number =~ ^[0-9]+$ ]]; then
    	echo "Invalid input. Please enter a valid number."
    	return
	fi

	# Check if the number is within the valid range
	if [ $number -lt 1 ] || [ $number -gt 10 ]; then
    	echo "The number is out of range. Please enter a number between 1 and 10."
    	return
	fi

	# Evaluate the number using if/elif/else
	if [ $number -gt 5 ]; then
    	echo "Your number is greater than 5."
	elif [ $number -lt 5 ]; then
    	echo "Your number is less than 5."
	else
    	echo "Your number is equal to 5."
	fi
}

# Call the function
evaluate_number



