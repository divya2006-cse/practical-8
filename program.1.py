from collections import deque

def bfs(graph):
    V = len(graph)

    visited = [False] * V
    result = []

    source = int(input("Enter source vertex: "))

    q = deque()

    visited[source] = True
    q.append(source)

    while q:
        current = q.popleft()

        result.append(current)

        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return result

V = int(input("Enter number of vertices: "))
graph = []
print("Enter adjacent vertices for each vertex:")
for i in range(V):
    neighbours = list(map(int, input(f"Vertex {i}: ").split()))
    graph.append(neighbours)
result = bfs(graph)
print("BFS Traversal:", end=" ")
for vertex in result:
    print(vertex, end=" ")