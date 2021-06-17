import sys


def dfs(node: int, target: int, dist: int, max_value: int) -> None:

    visited[node] = True
    if node == target:
        print(dist - max_value)
        exit(0)
    for next_node, cost in graph[node]:
        if not visited[next_node]:
            dfs(next_node, target, dist + cost, max(max_value, cost))


sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = int(1e9)
NODE_COUNT, robot_a, robot_b = map(int, input().split())
visited = [False] * (NODE_COUNT + 1)
dists = [INF] * (NODE_COUNT + 1)
max_values = [-1] * (NODE_COUNT + 1)
graph = [[] for _ in range(NODE_COUNT + 1)]
for _ in range(NODE_COUNT - 1):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node].append((end_node, cost))
    graph[end_node].append((start_node, cost))
dfs(robot_a, robot_b, 0, 0)