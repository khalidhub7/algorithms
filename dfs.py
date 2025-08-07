#!/usr/bin/python3
""" depth-first search (dfs) on a graph """

graph = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'Diana'],
    'Charlie': ['Alice'],
    'Diana': ['Bob']
}


def dfs(start_nodes):
    """
    dfs visit all connected nodes deeply before backtracking
    """
    stack = start_nodes
    visited = []

    while len(stack) > 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited


if __name__ == "__main__":
    print(dfs(['Alice']))
