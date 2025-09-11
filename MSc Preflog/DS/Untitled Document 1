def is_valid_matrix(m):
    return isinstance(m, list) and all(isinstance(row, list) and len(row) == len(m[0]) for row in m)

def can_multiply(a, b):
    return len(a[0]) == len(b)

def multiply_matrices(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result


x = [[1, 2],
     [3, 4],
     [5, 6]]

y = [[7, 8, 9, 10],
     [11, 12, 13, 14]]


if is_valid_matrix(x) and is_valid_matrix(y):
    if can_multiply(x, y):
        result = multiply_matrices(x, y)
        for row in result:
            print(row)
    else:
        print("Cannot multiply: columns in x must equal rows in y.")
else:
    if not is_valid_matrix(x):
        print("x is not a valid matrix.")
    if not is_valid_matrix(y):
        print("y is not a valid matrix.")
