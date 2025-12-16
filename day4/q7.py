matrix_list = [
    [1, 2, 3, 4],
    [4, 5, 7, 8],
    [9, 10, 11, 12]
]

matrix_tuple = (
    (9, 10, 11, 12),
    (4, 5, 7, 8),
    (1, 2, 3, 4)
)

def add_sub_matrices(m1, m2):
    addition = []
    subtraction = []

    for i in range(len(m1)):
        add_row = []
        sub_row = []
        for j in range(len(m1[0])):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        addition.append(add_row)
        subtraction.append(sub_row)

    return addition, subtraction

add_result, sub_result = add_sub_matrices(matrix_list, matrix_tuple)
print("Addition Matrix:")
for row in add_result:
    print(row)
print("Subtraction Matrix:")
for row in sub_result:
    print(row)
