
'''
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용하는 알고리즘
- 시간 복잡도: 노드의 개수가 N개 일때 N번의 단계 수행하며, 단계마다 N^2 연산을 통해 모든 경로 고려, O(N^3)
- 노드 개수의 N번 만큼의 단계를 반복하며 2차원 리스트를 갱신하기 때문에 다이나믹 프로그래밍에 속한다
- 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노르들 선택하는 과정을 반복
    - 각 단계에서는 해당 노드를 거쳐 가는 경우를 고려, ex) A -> 1번 노드 -> B
- 점화식: Dab = min(Dab, Dak + Dkb)
'''


def floyd_warshall(start, size):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for i in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    start_node, end_node, cost = map(int, input().split())
    graph[start_node][end_node] = cost

floyd_warshall(1, n)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
