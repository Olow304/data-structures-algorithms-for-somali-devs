# Declaring an array containing list of names
my_array = ['abdi', 'ali', 'ashia', 'fartun']

print(my_array[2]) # -> ashia

# pushing to the array
my_array.append('mohamed') # -> the time complexity for appending item is O(1)

# removing item from the end
my_array.pop() # -> the time complexity for removing item is O(1)

# inserting item for a specific location
my_array.insert(2, 'omar') # -> the time complexity for insert item for specific index is O(n)

print(my_array) # -> ['abdi', 'ali', 'omar', 'ashia', 'fartun']