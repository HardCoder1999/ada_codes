##################################################
# Input Values
##################################################
matrix = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

start_v_ = 0

##################################################
# Defined Functions
##################################################
visited_ar = []


def dfs_matrix(matrix, start_v_):
    visited_ar.append(start_v_)
    for i in range(len(matrix[start_v_])):
        if matrix[start_v_][i] == 1 and i not in visited_ar:
            dfs_matrix(matrix, i)
    return visited_ar


print(dfs_matrix(matrix, start_v_))
