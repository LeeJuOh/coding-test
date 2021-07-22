import sys
import heapq


def solution(graph, candidates, edge_cost: int) -> str:
    global s, h, g

    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            cost, now = heapq.heappop(q)
            if dist[now] < cost:
                continue

            for adj_cost, adj_node in graph[now]:
                new_cost = cost + adj_cost
                if new_cost < dist[adj_node]:
                    dist[adj_node] = new_cost
                    heapq.heappush(q, (new_cost, adj_node))
        return dist

    result = []
    dist_by_start = dijkstra(s)
    dist_by_h = dijkstra(h)
    dist_by_g = dijkstra(g)
    for candidate in sorted(candidates):
        min_dist = dist_by_start[candidate]
        hg_dist = dist_by_start[h] + edge_cost + dist_by_g[candidate]
        gh_dist = dist_by_start[g] + edge_cost + dist_by_h[candidate]

        if min_dist == min(hg_dist, gh_dist):
            result.append(candidate)

    return ' '.join(map(str, result))


INF = int(1e9)
input = sys.stdin.readline
T = int(input().rstrip())

results = []
for _ in range(T):
    # 노드 수, 간선 수, 목적지 후보 수
    n, m, t = map(int, input().split())
    # 출발노드, 지나간 간선 node1, node2
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        if {start, end} == {g, h}:
            edge_cost = cost
        graph[start].append((cost, end))
        graph[end].append((cost, start))
    # 후보 노드
    candidates = []
    for _ in range(t):
        candidates.append(int(input().rstrip()))
    results.append(solution(graph, candidates, edge_cost))

for result in results:
    print(result)
