# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.
import requests

# Prompt the user for the destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP Method
print("Select an HTTP Method from the following options:")
methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS"]
for i, method in enumerate(methods, 1):
    print(f"{i}. {method}")

method_choice = int(input("Enter the number corresponding to your choice: "))
method = methods[method_choice - 1]

# Print the request details and ask for confirmation
print("\nYour request details:")
print(f"URL: {url}")
print(f"HTTP Method: {method}")
confirm = input("Do you want to proceed with this request? (yes/no): ").lower()

if confirm != "yes":
    print("Request canceled.")
else:
    print("Proceeding with the request...\n")
    try:
        # Perform the HTTP request
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url)
        elif method == "PUT":
            response = requests.put(url)
        elif method == "DELETE":
            response = requests.delete(url)
        elif method == "HEAD":
            response = requests.head(url)
        elif method == "PATCH":
            response = requests.patch(url)
        elif method == "OPTIONS":
            response = requests.options(url)
        else:
            print("Invalid HTTP method selected.")
            exit()

        # Interpret the status code
        if response.status_code == 200:
            print("Success: The request was successful.")
        elif response.status_code == 404:
            print("Error: Site not found.")
        elif response.status_code == 403:
            print("Error: Access forbidden.")
        elif response.status_code == 500:
            print("Error: Internal server error.")
        else:
            print(f"Response status code: {response.status_code}")

        # Print the response headers
        print("\nResponse headers:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
