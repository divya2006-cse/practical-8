def dfs(graph):
    V = len(graph)

    visited = [False] * V
    result = []

    source = int(input("Enter source vertex: "))

    stack = []

    visited[source] = True
    stack.append(source)

    while stack:
        current = stack.pop()

        result.append(current)

        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

    return result


V = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacent vertices for each vertex:")
for i in range(V):
    neighbours = list(map(int, input(f"Vertex {i}: ").split()))
    graph.append(neighbours)

result = dfs(graph)

print("DFS Traversal:", end=" ")
for vertex in result:
    print(vertex, end=" ")
