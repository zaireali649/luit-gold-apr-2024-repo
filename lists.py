# Creating an empty list
var = []

# Checking the type of an empty list
print(type(var))

# Creating a list with integers
var2 = [151, 251, 386, 493, 649, 721]

# Checking the type and contents of a list
print(type(var2), var2)

# Creating a list with mixed data types
var3 = [151, 251, 386, 493, 649, 721, "009"]

# Checking the type and contents of a list with mixed data types
print(type(var3), var3)

# Appending a value to the list (in place)
var3.append(445)
# Checking the type and contents after appending a value
print(type(var3), var3)

# Concatenating lists (not in place)
var3 = var3 + [1008]
# Checking the type and contents after concatenation
print(type(var3), var3)

# Displaying available methods for the list object
print(dir(var3))

# Creating a list with integers
var4 = [0, 1, 2, 3, 4, 5]

# Creating a range object
numbers = range(10)

# Checking the type of a range object
print(type(numbers), numbers)

# Creating a list from range()
numbers = list(range(10))

# Checking the type and contents of a list created from range()
print(type(numbers), numbers)

# Iterating through a list and printing the square of each number
for number in numbers:
    print(type(number), number**2)

# Accessing an element of a list by index and checking its type
print(type(numbers), numbers[5])

# Reversing the order of the list
numbers.reverse()
print(type(numbers), numbers)

# Accessing an element of the reversed list by index and checking its type
print(type(numbers), numbers[5])

# Finding the length of the list
print(len(numbers))

# Creating a list of lists
list_of_lists = [[0, 1, 2], [0, 2, 6], [87, 21, 1]]

# Printing a list of lists and their individual elements
print(list_of_lists)

# Iterating over each element in the list_of_lists
for element in list_of_lists:
    # Printing the type and content of each element
    print(type(element), element)
    # Iterating over each number in the current element
    for number in element:
        # Printing the type and content of each number
        print(type(number), number)
