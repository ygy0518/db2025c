graph = [
    [0, 1, 1, 0, 0, 0, 0, 0], # A
    [1, 0, 0, 1, 0, 0, 0, 0], # B
    [1, 0, 0, 1, 0, 0, 0, 0], # C
    [0, 1, 1, 0, 1, 1, 1, 0], # D
    [0, 0, 0, 1, 0, 1, 0, 0], # E
    [0, 0, 0, 1, 1, 0, 0, 0], # F
    [0, 0, 0, 1, 0, 0, 0, 1], # G
    [0, 0, 0, 0, 0, 0, 1, 0]  # H
]

def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A') + i), end=' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


def bfs(g, i, visited):
    pass

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 4, visited_dfs)
print()
bfs(graph, 4, visited_dfs)