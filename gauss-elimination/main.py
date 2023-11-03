import numpy as np

def gauss_elimination(A, b, pivoting=True):
    n, m = A.shape
    if n != m:
        print("Matrix is not square")
        return

    # Forward elimination
    for i in range(len(A) - 1):
        if pivoting:
            # Partial pivoting
            max_row = np.argmax(np.abs(A[i:, i])) + i
            A[[i, max_row]] = A[[max_row, i]]
            b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, len(A)):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= A[i, i:] * factor
            b[j] -= b[i] * factor

    # Back substitution
    x = np.zeros(len(A))
    for i in range(len(A) - 1, -1, -1):
        sum_terms = np.sum(A[i, i + 1:] * x[i + 1:])
        if A[i, i] == 0:
            x[i] = 0
        else:
            x[i] = (b[i] - sum_terms) / A[i, i]

    return x

# Solve the linear system of equations using Gauss Elimination with partial pivoting
x_partial_pivoting = gauss_elimination(np.array([[1e-25, 1, 1], [1, 0, 1], [2, 8, 2]], dtype=np.float64), np.array([3, 4, 0], dtype=float))

# Solve the linear system of equations using Gauss Elimination with non-pivoting
x_non_pivoting = gauss_elimination(np.array([[10e-25, 1, 1], [1, 0, 1],[2,8,2]],dtype=np.float64), np.array([3, 4,0],dtype=float),pivoting=False)

# Print the results
print("Non-pivoting:", x_non_pivoting)
print("Partial pivoting:", x_partial_pivoting)



# 📄 Interpratation
# The non-pivoting approach resulted in invalid solution ([0. 3. 0.]) because it encountered numerical instability when trying to divide by a very small value (10e-25). This is a clear example of why partial pivoting is necessary in Gaussian elimination when dealing with potentially ill-conditioned matrices, as it helps avoid such numerical issues and leads to valid solutions.



