import heapq
import sys


def my_solution():
    count = 0
    max_distance = 0
    dijkstra(start)

    for dist in distance:
        if dist != INF:
            count += 1
            max_distance = max(max_distance, dist)
    print(count - 1, max_distance)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for end_node, cost in graph[now]:
            new_cost = dist + cost
            if new_cost < distance[end_node]:
                distance[end_node] = new_cost
                heapq.heappush(q, (new_cost, end_node))


INF = int(1e9)
input = sys.stdin.readline

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node].append((end_node, cost))
my_solution()
