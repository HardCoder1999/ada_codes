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
def bfs(graph, start_v):
    visited = []
    queue = []
    queue.append(start_v)
    while(queue != []):
        v = queue.pop(0)
        visited.append(v)
        for i in graph[v]:
            if i not in queue and i not in visited:
                queue.append(i)
    return visited


print(bfs(graph, start_v))
