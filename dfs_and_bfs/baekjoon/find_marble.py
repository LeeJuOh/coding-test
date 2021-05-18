def my_solution(N, M, graphs):
    global count

    result = 0
    mid = (N + 1) / 2
    for graph in graphs:
        for i in range(1, N + 1):
            count = 0
            visited = [False] * (N + 1)
            get_heavier_or_lighter_marble_count(graph, i, visited)
            if count >= mid:
                result += 1
    return result


def get_heavier_or_lighter_marble_count(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            count += 1
            get_heavier_or_lighter_marble_count(graph, i, visited)


N, M = map(int, input().split())
count = 0
heavy_relation_graph = [[] for _ in range(N + 1)]
light_relation_graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    heavy_relation_graph[y].append(x)
    light_relation_graph[x].append(y)
print(my_solution(N, M, [heavy_relation_graph, light_relation_graph]))
