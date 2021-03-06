import copy
from collections import deque


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


n = int(input())
time = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    input_data = list(map(int, input().split()))
    time[i] = input_data[0]
    for data in input_data[1:-1]:
        indegree[i] += 1
        graph[data].append(i)
topology_sort()
