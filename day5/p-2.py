scores = [10, 20, "Math", "English"]
print(scores)

scores.append(30)  # Add a new score at the end
print(scores)

scores.insert(2, "Science")  # Insert "Science" at index 2
print(scores)


print(93 in scores)  # Check if 93 is in the list

print(len(scores))  # Get the length of the list


scores.clear()  # Clear the list
print(scores)  # Print the empty list