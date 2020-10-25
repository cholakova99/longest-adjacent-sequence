from .create_matrix import create_matrix_from_file

def get_index(cell):
    return str(cell[0]) + str(cell[1])


def get_possible_moves(matrix, row, col):
    moves = []
    if row > 0:
        moves.append([row - 1, col])
    if col > 0:
        moves.append([row, col - 1])
    if row < len(matrix) - 1:
        moves.append([row + 1, col])
    if col < len(matrix[0]) - 1:
        moves.append([row, col + 1])
    return moves


def find_way(matrix, row, col, expected, visited):
    moves = get_possible_moves(matrix, row, col)
    visited.append(get_index([row, col]))
    count = 1
    for x in moves:
        if get_index(x) not in visited:
            if matrix[x[0]][x[1]] == expected:
                count += find_way(matrix, x[0], x[1], expected, visited)
    return count


def find_longest_seq(matrix):
    maximum = -1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            visited = []
            maximum = max(maximum, find_way(matrix, row, col, matrix[row][col], visited))
    return maximum

