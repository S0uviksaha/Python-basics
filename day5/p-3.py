# break & continue statements

for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # Print numbers from 0 to 4


list = [1, 2, 3, 4, 5]

for i in list:
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    print(i)  # Print numbers except 3