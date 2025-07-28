import numpy as np

A = np.array([[1, 5],
              [4, -3]])

a = np.linalg.det(A)  # Determinant of matrix A
A_inv = np.linalg.inv(A) # Inverse of matrix A
print("Determinant of A:", a)
print(A_inv)
print(np.dot(A, A_inv))  # Should be close to identity matrix