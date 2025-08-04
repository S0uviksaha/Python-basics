# sets

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Accessing elements in a set

for element in my_set:
    print(element)  # Prints each element in the set


# Note: Sets are unordered, so the order of elements may vary
# You cannot access elements by index like in lists or tuples
# my_set[0]   This will raise an error because sets are unordered and do not support indexing


my_set.add(6)  # Adding an element to the set
print(my_set)
my_set.remove(3)  # Removing an element from the set
print(my_set)

# Checking if an element exists in the set
print(2 in my_set)  # True
print(10 in my_set)  # False

# Set operations
set_a = {1, 2, 3}   
set_b = {3, 4, 5}
print(set_a.union(set_b))  # Union: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b))  # Intersection: {3}
