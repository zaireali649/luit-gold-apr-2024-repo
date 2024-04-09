import random

# Generate a random integer between 0 and 10
number = random.randint(0, 10)

# Initialize a counter for the number of iterations
counter = 0

# Use a while loop to repeat the following block of code until the condition number != 7 is met
while number != 7:
    # Check if the counter has reached 13
    if counter >= 13:
        # If it has, exit the loop
        break
    
    # Generate a new random number between 0 and 10
    number = random.randint(0, 10)
    # Increment the counter by 1
    counter += 1  # Equivalent to counter = counter + 1
    
# Print the number of iterations and the final number
print(counter, number)


# Use a for loop to iterate over a range of values from 0 to 4
for i in range(5):
    # Print the square of each value
    print(i**2)
