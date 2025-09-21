def transpose (mat: list[list[float | int]])->list[list[float | int]] | None:
    if not mat: # Проверка на пустую матрицу
        return None
    row_length = len(mat[0])
# Проверка на "рваную" матрицу
    if any(len(row) != row_length for row in mat):
        raise ValueError("Матрица должна быть прямоугольной (одинаковая длина строк)")
# Транспонирование матрицы
    return [[mat[j][i] for j in range(len(mat))] for i in range(row_length)]
def row_sums(mat: list[list[float| int]]) -> list[float]:
    if not mat:
        return []
    row_length = len(mat[0])
# Проверка на "рваную" матрицу
    if any(len(row) != row_length for row in mat):
        raise ValueError("Матрица должна быть прямоугольной (одинаковая длина строк)")
    return [sum(row) for row in mat]
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return [] 
    row_length =len(mat[0])
# Проверка на "рваную" матрицу
    if any(len(row) != row_length for row in mat):
        raise ValueError("Матрица должна быть прямоугольной (одинаковая длина строк)")
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(row_length)]
print(transpose([[1, 2, 3],[4,5,6]])) # [[1, 4], [2, 5], [3, 6]]
print(row_sums([[1, 2, 3], [4, 5, 6]])) # [6, 15]
print(col_sums([[1, 2, 3], [4, 5, 6]])) # [5, 7, 9] 