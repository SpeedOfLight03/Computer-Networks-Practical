import sys
def find_all_paths(graph, src, dest, visited=None, path=None):
    # Create a list to store the visited nodes if it doesn't exist
    if visited is None:
        visited = [False] * len(graph)
    
    # Create a list to store the current path if it doesn't exist
    if path is None:
        path = []
    
    # Mark the current node as visited and add it to the path
    visited[src] = True
    path.append(chr(src + ord('A')))
    
    # If the current node is the destination, print the path
    if src == dest:
        print(path)
    else:
        # If the current node is not the destination, recurse on all its adjacent nodes
        for i in range(len(graph)):
            if graph[src][i] != sys.maxsize and not visited[i]:  # Check if there is an edge from src to i and i is not visited
                find_all_paths(graph, i, dest, visited, path)
    
    # Remove the current node from the path and mark it as not visited, so it can be used in other paths
    path.pop()
    visited[src] = False

def print_solution(dist, parent, src, dest):
    print("Shortest Path from", src, "to", dest, ":")
    print_path(parent, src, dest)
    print("\nShortest distance:", dist[ord(dest) - ord('A')])

def print_path(parent, src, dest):
    if src == dest:
        print(src, end=' ')
        return
    if parent[ord(dest) - ord('A')] == -1:
        print("No path exists from", src, "to", dest)
        return
    print_path(parent, src, chr(parent[ord(dest) - ord('A')] + ord('A')))
    print(dest, end=' ')

def bellman_ford(graph, src, dest):
    nodes = len(graph)
    INFINITY = sys.maxsize
    dist = [INFINITY] * nodes
    dist[ord(src) - ord('A')] = 0
    parent = [-1] * nodes

    for _ in range(nodes - 1):
        for u in range(nodes):
            for v in range(nodes):
                if graph[u][v] != INFINITY and dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    parent[v] = u

    # Check for negative weight cycles
    for u in range(nodes):
        for v in range(nodes):
            if graph[u][v] != INFINITY and dist[u] + graph[u][v] < dist[v]:
                print("Graph contains negative weight cycle")
                return

    print_solution(dist, parent, src, dest)

def main():
    adjacency_matrix = [
        [0, 2, sys.maxsize, 3, sys.maxsize, 4, sys.maxsize, 1],
        [2, 0, 4, 1, 5, sys.maxsize, 1, sys.maxsize],
        [sys.maxsize, 4, 0, 6, 1, 3, 1, 3],
        [3, 1, 6, 0, 5, sys.maxsize, sys.maxsize, 2],
        [sys.maxsize, 5, 1, 5, 0, 4, 5, 2],
        [4, sys.maxsize, 3, sys.maxsize, 4, 0, 3, sys.maxsize],
        [sys.maxsize, 1, 1, sys.maxsize, 5, 3, 0, sys.maxsize],
        [1, sys.maxsize, 3, 2, 2, sys.maxsize, sys.maxsize, 0]
    ]

    bellman_ford(adjacency_matrix, 'A', 'E')
    print("all the possible paths are")
    find_all_paths(adjacency_matrix, 0, 4)

if __name__ == "__main__":
    main()