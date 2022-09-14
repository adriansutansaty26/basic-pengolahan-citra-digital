import numpy as np

matrix_a = np.array(([1,2,3],[4,5,6],[7,8,9]))

matrix_b = np.array(([2,7,1],[3,9,5],[1,6,4]))

matrix_c = np.zeros((3,3))

# membuat matriks koreksi b berukuran sama dengan matriks a
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        matrix_c[i, j] = matrix_a[i, j] * matrix_b[i, j]
        print(matrix_c[i, j])