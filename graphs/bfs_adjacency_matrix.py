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


def bfs_matrix(matrix, start_v):
    queue = []
    visited = []
    queue.append(start_v)
    while queue != []:
        v = queue.pop(0)
        visited.append(v)
        for i in range(len(matrix[v])):
            if matrix[v][i] == 1 and i not in visited:
                queue.append(i)
    return visited


print(bfs_matrix(matrix, start_v_))
