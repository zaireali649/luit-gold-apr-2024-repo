var = {}  # Creating an empty dictionary

# Checking the type of an empty dictionary
print(type(var))

var2 = {"juice": "cranberry", "movie": "The Lion King", "dessert": "cheesecake"}

# Checking the type and contents of a dictionary
print(type(var2), var2)

# Accessing a value from the dictionary by key
print(var2["juice"])

# Checking if a key exists in the dictionary and printing its value
if "movie" in var2:
    print(var2["movie"])
    
# Checking if a key exists in the dictionary and printing its value (which does not exist)
if "show" in var2:
    print(var2["show"])
    
# Adding a new key-value pair to the dictionary
var2['drank'] = "petron"
print(type(var2), var2)

# Deleting a key-value pair from the dictionary
del var2['drank']
print(type(var2), var2)

# Displaying available methods for the dictionary object
print(dir(var2))

# Converting dictionary keys to a list
print(list(var2.keys()))

# Converting dictionary values to a list
print(list(var2.values()))

# Iterating over key-value pairs in the dictionary and printing them
for k, v in var2.items():
    print(k, v)
    
var3 = {"a": {"d": "d"}, "b": {"e": "e"}, "c": {"f": "f"}}

# Checking the type and contents of a nested dictionary
print(type(var3), var3)

# Iterating over key-value pairs in the outer dictionary
for key, value in var3.items():
    # Printing the key and value of the outer dictionary
    print(key, value)
    # Iterating over key-value pairs in the inner dictionary
    for key2, value2 in value.items():
        # Printing the key and value of the inner dictionary
        print(key2, value2)
