import numpy as np


'1D- array'

arr1d = np.array([10, 20, 30, 40, 50])

print("Array:\n", arr1d)
print("Shape:", arr1d.shape)
print("Dimensions:", arr1d.ndim)

print("First element:", arr1d[0])
print("Slice [1:4]:", arr1d[1:4])

print("Array + 5:\n", arr1d + 5)


'2D-Array'

import numpy as np

arr2d = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

print("Array:\n", arr2d)
print("Shape:", arr2d.shape)
print("Dimensions:", arr2d.ndim)

print("Element at row 1, col 2:", arr2d[1, 2])
print("Sub-matrix (cols 1-2):\n", arr2d[:, 1:3])

print("Sum of each column (axis=0):", arr2d.sum(axis=0))
print("Sum of each row (axis=1):", arr2d.sum(axis=1))


'3D-Array'

import numpy as np

arr3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]
])

print("Array:\n", arr3d)
print("Shape:", arr3d.shape)
print("Dimensions:", arr3d.ndim)

print("Element at matrix 1, row 2, col 0:", arr3d[1, 2, 0])
print("First 2D matrix:\n", arr3d[0, :, :])


'Operations on 1D,2D,3D array'

# 1D Array Operations
a1 = np.array([2, 4, 6, 8])
b1 = np.array([1, 2, 3, 4])

print(a1 + b1)
print(a1 - b1)
print(a1 * b1)
print(a1**b1)
print(a1 / b1)
print(a1.T)

# 2D Array Operations
a2 = np.array([[2, 4], [6, 8]])
b2 = np.array([[1, 2], [3, 4]])

print(a2 + b2)
print(a2 - b2)
print(a2 * b2)
print(a2**b2)
print(a2 / b2)
print(a2.T)

# 3D Array Operations
a3 = np.array([[[2, 4], [6, 8]], [[10, 12], [14, 16]]])
b3 = np.array([[[1, 2], [2, 1]], [[2, 1], [1, 2]]])

print(a3 + b3)
print(a3 - b3)
print(a3 * b3)
print(a3**b3)
print(a3 / b3)
print(a3.T)

