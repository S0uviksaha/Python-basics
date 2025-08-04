# Tuples

marks = (10, 20, 30, 40, 50, 50, 50)
print(marks)

# marks[0] = 15       This will raise an error because tuples are immutable

for i in range(len(marks)):
    print(marks[i])

print(marks.count) # Count occurrences of 50 in the tuple
print(marks.index(50))  # Find the starting index of 50 in the tuple