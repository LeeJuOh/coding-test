'''
진입 차수(Indegree)
- 특정한 노드로 들어오는 간선의 개수

위상정렬
- 정렬 알고리즘의 일종
- 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
- 1. 진입 차수가 0인 노드를 큐에 넣는다
- 2. 큐가 빌 때까지 다음의 과정을 반복한다
-   2.1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
-   2.2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
- 위상 정렬의 답안은 여러가지가 될 수 있다.
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단 가능
- 시간 복잡도: O(V + E)
'''


from collections import deque


# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')
    print()


v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
topology_sort()
