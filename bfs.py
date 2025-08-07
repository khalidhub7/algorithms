#!/usr/bin/python3
""" breadth-first search (bfs) on a graph """

from collections import deque

graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Diana'],
    'Charlie': ['Alice'],
    'Diana': ['Bob']
}


def bfs(start_nodes):
    """
    bfs visit all connected nodes level by level
    """
    queue = deque(start_nodes)
    visited = []

    while len(queue) > 0:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


if __name__ == "__main__":
    print(bfs(['Alice']))
