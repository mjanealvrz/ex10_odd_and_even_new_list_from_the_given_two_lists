# Create a new list from two list using the following condition
#Given two list of numbers, write a program to create a new list such that the new list should 
#contain odd numbers from the first list and even numbers from the second list.


# Pseudocode

# Initialize  the given list
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Initialize empty list and store results
empty_list = []

# Using for loop iterate the list number 1
for number in (list1):   
    # Check if the number is odd
     if number % 2 != 0:
    # If it's odd, append it to the empty_list
           empty_list.append(number)

# Using for loop iterate the list number 2
for numbers in (list2):
    # Check if the number is even
      if numbers % 2 == 0:
    # If it's even, append it to the result_list
            empty_list.append(numbers)
# Print results 
print("The new list is", empty_list)
