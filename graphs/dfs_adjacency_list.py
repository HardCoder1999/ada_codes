##################################################
# Input Values
##################################################
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6],
    4: [1, 7],
    5: [2],
    6: [3, 5],
    7: [4]
}
start_v = 1

##################################################
# Defined Functions
##################################################
visited = []


def dfs(graph, start_v):
    visited.append(start_v)
    for i in graph[start_v]:
        if i not in visited:
            dfs(graph, i)
    return visited


print(dfs(graph, start_v))
