def row_sums(mat):
    if not mat:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if len(row) != row_length:
            raise ValueError("Рваная матрица")
    
    return [sum(row) for row in mat]

mat = [[1, 2, 3], [4, 5, 6]]
print(row_sums(mat))
mat = [[-1, 1], [10, -10]]
print(row_sums(mat))
mat = [[0, 0], [0, 0]]
print(row_sums(mat))
mat = [[1, 2], [3]]
print(row_sums(mat))