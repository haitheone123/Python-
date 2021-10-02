import numpy as np

visited = set()
def dfs (set,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph(node):
            dfs(visited,graph,neighbour)
dfs(visited,graph,'5')



