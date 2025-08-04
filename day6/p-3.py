# dictionary

mark = {'Math': 90, 'Science': 85, 'English': 88} # key-value pairs
print(mark)

print(mark['Math'])  # Access value by key
print(mark.get('Science'))  # Access value using get method

# Adding a new key-value pair
mark['History'] = 92
print(mark)
# Removing a key-value pair
del mark['English']
print(mark)

# Checking if a key exists
print('Math' in mark)  # True
print('English' in mark)  # False

# updating a value
mark['Science'] = 90
print(mark)

