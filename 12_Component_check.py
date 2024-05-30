import sys

def dfs(graph, visited, node, component):
    visited[node] = True
    component.append(chr(node + ord('A')))

    for neighbour in range(len(graph)):
        if graph[node][neighbour] != sys.maxsize and not visited[neighbour]:
            dfs(graph, visited, neighbour, component)

def connected_components(graph):
    visited = [False] * len(graph)
    components = []

    for node in range(len(graph)):
        if not visited[node]:
            component = []
            dfs(graph, visited, node, component)
            components.append(component)

    return components

def main():
    adjacency_matrix = [
        [0, 2, sys.maxsize, 3, sys.maxsize, 4, sys.maxsize, 1],
        [2, 0, 4, 1, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize],
        [sys.maxsize, 4, 0, 6, sys.maxsize, 3, sys.maxsize, 3],
        [3, 1, 6, 0, sys.maxsize, sys.maxsize, sys.maxsize, 2],
        [sys.maxsize, 5, 1, 5, sys.maxsize, 4, sys.maxsize, 2],
        [4, sys.maxsize, 3, sys.maxsize, sys.maxsize, 0, sys.maxsize, sys.maxsize],
        [sys.maxsize, 1, 1, sys.maxsize, sys.maxsize, 3, sys.maxsize, sys.maxsize],
        [1, sys.maxsize, 3, 2, sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]

    components = connected_components(adjacency_matrix)

    # print(components)

    if len(components) == 1:
        print("The graph is connected.")
    else:
        print("The graph is disconnected.")
        for i, component in enumerate(components, 1):
            print("Component", i, ":", component)

if __name__ == "__main__":
    main()
