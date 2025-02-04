# Ask user for their name
name = input ("What is your name? ").strip().title()

# Remove leading and trailing whitespace from the user's name
#name = name.strip().title()

# Capitalize the first letter of the user's name
#name = name.capitalize() 

# Convert the user's name to title case (capitalize the first letter of each word)
#name = name.title()

# Split the user's name into first name and last name using the space as the delimiter
first, last = name.split(" ")

# Print a greeting message with the user's name
print("Hello,", name)

# Use a formatted string to print a greeting message with the user's name
print(f"Welcome, {name}")