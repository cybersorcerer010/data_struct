"""
list_operations.py

This module demonstrates basic list operations in Python. The operations include:
- Creating an empty list
- Appending elements to the list
- Inserting an element at a specific position
- Extending the list with another list
- Removing the last element
- Sorting the list in ascending order
- Finding and printing the index of a specific value

The script uses a simple example to illustrate how each operation works.
"""

# Create an empty list
my_list = []

# Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
