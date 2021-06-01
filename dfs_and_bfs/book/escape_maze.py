from collections import deque


def my_solution(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
print(my_solution(0, 0))
