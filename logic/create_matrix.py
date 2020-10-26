def create_matrix_from_file(file_name):
    with open(file_name, 'r') as file:
        list_with_info = file.readlines()
    for i in range(len(list_with_info)):
        list_with_info[i] = list_with_info[i][:-1]
    first_line = list_with_info[0].split()
    rows = int(first_line[0])
    # cols = int(first_line[1])
    created_matrix = []
    helper = []
    for i in range(rows + 1):
        helper = list_with_info[i].split()
        created_matrix.append(helper)
        helper = []
    created_matrix = created_matrix[1:]
    if check_matrix_correct(created_matrix, len(created_matrix), len(created_matrix[0])) is not True:
        raise ValueError('Wrong input!')
    return created_matrix


def check_matrix_correct(matrix, rows, cols):
    for r in range(rows):
        if len(matrix[r]) != cols:
            raise ValueError('Wrong input!')
        for c in range(cols):
            if matrix[r][c] != 'R' and matrix[r][c] != 'G' and matrix[r][c] != 'B':
                raise ValueError('Wrong input!')
    return True
