import numpy as np

A = np.array([[1, 5],
              [4, -3]])

B = np.array([[2, -1],
              [7, 6]])

print(A + B)
print(A - B)
print(A * B)
print(np.dot(A, B))