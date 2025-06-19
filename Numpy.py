 # Step 1: Install NumPy (run in terminal or notebook cell if not installed)
# !pip install numpy

# Step 2: Import NumPy
import numpy as np

# 1. Create a 1D NumPy array with integers from 1 to 20
arr_1d = np.arange(1, 21)

# a. Calculate sum, mean, median, and standard deviation
sum_arr = np.sum(arr_1d)
mean_arr = np.mean(arr_1d)
median_arr = np.median(arr_1d)
std_dev_arr = np.std(arr_1d)

print("1D Array:", arr_1d)
print("Sum:", sum_arr)
print("Mean:", mean_arr)
print("Median:", median_arr)
print("Standard Deviation:", std_dev_arr)

# b. Find indices of elements greater than 10
indices_gt_10 = np.where(arr_1d > 10)[0]
print("Indices of elements > 10:", indices_gt_10)

print("\n" + "="*40 + "\n")

# 2. Create a 2D array of shape 4x4 with numbers 1 to 16
arr_2d = np.arange(1, 17).reshape(4, 4)

# a. Print the array
print("2D Array:\n", arr_2d)

# b. Transpose of the array
transpose_arr = arr_2d.T
print("Transpose:\n", transpose_arr)

# c. Row-wise and column-wise sums
row_sums = np.sum(arr_2d, axis=1)
col_sums = np.sum(arr_2d, axis=0)
print("Row-wise sums:", row_sums)
print("Column-wise sums:", col_sums)

print("\n" + "="*40 + "\n")

# 3. Create two 3x3 arrays with random integers between 1 and 20
array1 = np.random.randint(1, 21, size=(3, 3))
array2 = np.random.randint(1, 21, size=(3, 3))

print("Array 1:\n", array1)
print("Array 2:\n", array2)

# a. Element-wise operations
add_result = array1 + array2
sub_result = array1 - array2
mul_result = array1 * array2

print("Element-wise Addition:\n", add_result)
print("Element-wise Subtraction:\n", sub_result)
print("Element-wise Multiplication:\n", mul_result)

# b. Dot product
dot_product = np.dot(array1, array2)
print("Dot Product:\n", dot_product)

print("\n" + "="*40 + "\n")

# 4. Reshape a 1D array of size 12 into a 3x4 array and slice first two rows and last two columns
arr_12 = np.arange(1, 13)
reshaped_arr = arr_12.reshape(3, 4)
print("Reshaped 3x4 Array:\n", reshaped_arr)

# Slice: first two rows and last two columns
sliced_arr = reshaped_arr[:2, -2:]
print("Sliced Array (first two rows, last two columns):\n", sliced_arr)
