from .create_matrix import create_matrix_from_file

# def get_index(cell):
#     return str(cell[0]) + str(cell[1])


# def get_possible_moves(matrix, row, col):
#     moves = []
#     if row > 0:
#         moves.append([row - 1, col])
#     if col > 0:
#         moves.append([row, col - 1])
#     if row < len(matrix) - 1:
#         moves.append([row + 1, col])
#     if col < len(matrix[0]) - 1:
#         moves.append([row, col + 1])
#     return moves


# def find_way(matrix, row, col, expected, visited):
#     moves = get_possible_moves(matrix, row, col)
#     visited.append(get_index([row, col]))
#     count = 1
#     for x in moves:
#         if get_index(x) not in visited:
#             if matrix[x[0]][x[1]] == expected:
#                 count += find_way(matrix, x[0], x[1], expected, visited)
#     return count


# def find_longest_seq(matrix):
#     maximum = -1
#     for row in range(len(matrix)):
#         for col in range(len(matrix[0])):
#             visited = []
#             maximum = max(maximum, find_way(matrix, row, col, matrix[row][col], visited))
#     return maximum


def get_possible_moves(matrix, row, col):
    moves = []
    if row > 0:
        moves.append((row - 1, col))
    if col > 0:
        moves.append((row, col - 1))
    if row < len(matrix) - 1:
        moves.append((row + 1, col))
    if col < len(matrix[0]) - 1:
        moves.append((row, col + 1))
    return moves


def get_longest_seq(matrix):
    maximum = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != -1:
                res = dfs(matrix, r, c, matrix[r][c])
            maximum = max(maximum, res)
    return maximum


def dfs(matrix, row, col, expected):
    stack = []
    stack.append((row, col))
    lenght = 0
    while stack:
        current = stack.pop()
        if matrix[current[0]][current[1]] == expected:
            matrix[current[0]][current[1]] = -1
            lenght += 1
            neighs = get_possible_moves(matrix, current[0], current[1])
            for elem in neighs:
                stack.append(elem)
    return lenght
