import random

# Generate a random integer between 0 and 10
number = random.randint(0, 10)

# Check if the number is less than 6
if number < 6:  
    print("small number")  # If true, print "small number"
# If the number is greater than 6
elif number > 6:  
    print("big number")  # If true, print "big number"
# If neither of the above conditions is met, meaning the number is equal to 6
else:  
    print("number is 6")  # If true, print "number is 6"
    
    
# Check if the number is less than 4
if number < 4:  
    print("really small number")  # If true, print "really small number"
    
# Print the generated number
print(number)  
