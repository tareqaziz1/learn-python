# All about List []
# List is like a container that can hold multiple values in one variable.

names = ["John", "Tom", "Sofia", "Sarah"]
print(names[0]) # output- John
print(names[1]) # output- Tom
print(names[-1]) # output- Sarah
print(names[-2]) # output - Sofia
print(names[2:]) # All items index from 2 ['Sofia', 'Sarah']
print(names[1:4]) #index 1 to 3 ['Tom', 'Sofia', 'Sarah']

# Accessing with index does not change the original list.

# Modifying list

names[0] = "John Smith"
print(names) #output - ['John Smith', 'Tom', 'Sofia', 'Sarah']

# Find the largest number from the list

numbers = [10,15,13,20,14,16,17,19,18]

largest_number = numbers[0]

for i in numbers:
    if i > largest_number:
        largest_number = i

print(largest_number)

# 2D list

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# How to find 5 from the 2nd items of the list

print(matrix[1][1]) #output - 5

# How to find 7 from the list?

print(matrix[2][0])

# modify the value 9 to 10

matrix[2][2] = 10
print(matrix[2][2]) #output - 10

print(matrix) #output - [[1, 2, 3], [4, 5, 6], [7, 8, 10]]

#Get all the numbers from the 2D list

for row in matrix:
    for items in row:
        print(items)

#Exercise

data = [
    [10, 20, 30],
    [11, 12, 13],
    [15, 30, 45],
    [30, 60, 90]
]

num_rows = len(data)
num_cols = len(data[0])

averages = []

for col in range(num_cols):
    total = 0
    for row in range(num_rows):
        total += data[row][col]

    avg = total / num_rows
    averages.append(avg)

print("Averages:", averages)