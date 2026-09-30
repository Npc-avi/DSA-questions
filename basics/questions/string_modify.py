# Function to take a string and return a modified string
def modify_string(s):
    # Assign existing string to a new variable
    new_str = s
    # Append extra text
    new_str += " World"
    # Return the modified string
    return new_str

# Original string
original = "Hello"

# Pass string to function and store returned value
result = modify_string(original)

# Print results
print("Original:", original)
print("Returned:", result)