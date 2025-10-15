def col_sums(mat):
    if not mat:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Рваная матрица")
    
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]

mat = [[1, 2, 3], [4, 5, 6]]
print(col_sums(mat))
mat = [[-1, 1], [10, -10]]
print(col_sums(mat))
mat = [[0, 0], [0, 0]]
print(col_sums(mat))
mat = [[1, 2], [3]]
print(col_sums(mat))