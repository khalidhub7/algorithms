#!/usr/bin/python3
""" breadth-first search (BFS) on a graph """
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}


def bfs(key):
    """ visit all connected nodes
    level by level from start node """
    queue = deque(key)
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


print(bfs(['A']))  # ['A', 'B', 'C', 'D']
