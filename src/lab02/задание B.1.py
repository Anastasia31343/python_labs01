def transpose(mat):
    new_mat = []
    if len(mat) == 0:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Рваная матрица")
    
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]

mat = [[1, 2, 3]]
print(transpose(mat))
mat = [[1], [2], [3]]
print(transpose(mat))
mat = [[1, 2], [3, 4]]
print(transpose(mat))
mat = []
print(transpose(mat))
mat = [[1, 2], [3]]
print(transpose(mat))