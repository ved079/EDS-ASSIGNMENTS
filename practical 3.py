import numpy as np
import csv

# Create a NumPy array
file1 = open('dataset7.csv','r')
data1 = list(csv.reader(file1,delimiter=','))
arr = np.array(data1)

# Perform various operations
print("Array:", arr)
print("Array shape:", arr.shape)
print("Array size:", arr.size)
print("Array dtype:", arr.dtype)
print("Array dimension:", arr.ndim)


# Perform operations on multi-dimensional arrays
arr2d = np.array(data1)
print("2D Array:")
print(arr2d)
print("2D Array shape:", arr2d.shape)
print("Sum of 2D Array (axis=0):", np.sum(arr2d, axis=0))
print("Sum of 2D Array (axis=1):", np.sum(arr2d, axis=1))
print("Transpose of 2D Array:")
print(np.transpose(arr2d))

# Reshaping arrays
arr3d = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = np.reshape(arr3d, (2, 3))
print("Reshaped 3D Array:")
print(reshaped_arr)

# Broadcasting
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print("Broadcasting:")
print(result)

#Program to take databases for any real life application.read a database into an array and perform following:

# stacking, searching, sorting, counting, broadcasting
import numpy as np

# Database of student records
# Each row represents a student with columns: ID, Name, Age, Grade
database = np.array([
    [101, 'John', 15, 9],
    [102, 'Jane', 16, 10],
    [103, 'David', 14, 8],
    [104, 'Emily', 15, 9],
    [105, 'Michael', 16, 10]
])

# 1. Perform all matrix operations
# Transpose the matrix
transposed = np.transpose(database)
print("Transposed Database:")
print(transposed)

# Matrix multiplication
matrix_product = np.matmul(database[:, 2:4], transposed[2:4, :])
print("Matrix Product:")
print(matrix_product)

# 2. Horizontal and vertical stacking of arrays
# Create additional data arrays
grades = np.array([9, 10, 8, 9, 10])
heights = np.array([165, 170, 155, 160, 175])

# Horizontal stacking
horizontal_stack = np.hstack((database, grades.reshape(-1, 1), heights.reshape(-1, 1)))
print("Horizontal Stacked Array:")
print(horizontal_stack)

# Vertical stacking
vertical_stack = np.vstack((database, grades, heights)).T
print("Vertical Stacked Array:")
print(vertical_stack)

# 3. Custom sequence generation
custom_sequence = np.arange(1, 11, 2)  # Generates sequence [1, 3, 5, 7, 9]
print("Custom Sequence:")
print(custom_sequence)

# 4. Arithmetic and statistical operations, bitwise operators
# Arithmetic operations
addition = database[:, 2] + database[:, 3]
print("Addition:")
print(addition)

# Statistical operations
mean_age = np.mean(database[:, 2])
print("Mean Age:", mean_age)

# Bitwise operators
bitwise_and = database[:, 2] & database[:, 3]
print("Bitwise AND:")
print(bitwise_and)

# 5. Copying and viewing arrays
# Copy array
copied_array = database.copy()

# View array
view_array = database.view()
view_array[0, 0] = 201  # Modifying the view will affect the original array

# 6. Data stacking, searching, sorting, counting, broadcasting
# Data stacking
data_stack = np.column_stack((database, grades, heights))
print("Data Stack:")
print(data_stack)

# Searching
search_result = np.where(database[:, 1] == 'John')
print("Search Result:")
print(search_result)

# Sorting
sorted_array = np.sort(database, axis=0)
print("Sorted Array:")
print(sorted_array)

# Counting
grade_counts = np.bincount(database[:, 3])
print("Grade Counts:")
print(grade_counts)

# Broadcasting
broadcasted = database * 10
print("Broadcasted Array:")
print(broadcasted)
