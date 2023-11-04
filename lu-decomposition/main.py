import numpy as np

# Function to perform Cholesky decomposition
def cholesky_decomposition(matrix):
  n = len(matrix)
  L = np.zeros((n, n), dtype=float)

  for i in range(n):
    for j in range(i+1):
      sum_val = sum(L[i, k] * L[j, k] for k in range(j))
      if i == j:
        L[i, j] = (matrix[i, i] - sum_val) ** 0.5
      else:
        L[i, j] = (1.0 / L[j, j]) * (matrix[i, j] - sum_val)
   
  # U is simply the transpose of L
  U = L.T
  print("Matrix L:\n",L)
  print("\nMatrix U:\n",U)

# Function to perform Doolittle decomposition
def doolittle_decomposition(mat):
  # Get the number of rows and columns in A
  n = mat.shape[0]
    # Initialize matrices L and U with zeros
  L = np.zeros((n, n))
  U = np.zeros((n, n))
  # Perform LU decomposition
  for k in range(n):
    U[k, k:] = A[k, k:] - L[k, :k] @ U[:k, k:]
    L[k+1:, k] = (A[k+1:, k] - L[k+1:, :k] @ U[:k, k]) / U[k, k]

  # Set the diagonal of L to 1
  L[np.diag_indices(n)] = 1  
  
  print("Matrix L:\n",L)
  print("\nMatrix U:\n",U)


# Function to perform Crout decomposition
def crout_decomposition(A):
  n = A.shape[0]

# Initialize matrices L and U with zeros
  L = np.zeros((n, n))
  U = np.zeros((n, n))

# Perform Crout LU decomposition
  for k in range(n):
    L[k:, k] = A[k:, k] - L[k:, :k] @ U[:k, k]
    U[k, k:] = (A[k, k:] - L[k, :k] @ U[:k, k:]) / L[k, k]

  print("Matrix L:\n",L)
  print("\nMatrix U:\n",U)


# Define the matrix A
A = np.array([[8, -9, 1, -2],
              [-16, 21, -6, 9],
              [24, -39, 25, -32],
              [-40, 63, -71, 92]], dtype=float)

# crout_decomposition(A)
# doolittle_decomposition(A)

# Calculate A^T A
ATA = np.dot(A.T, A)
cholesky_decomposition(ATA)

















