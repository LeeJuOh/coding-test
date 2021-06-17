# 방향 그래프의 사이클 찾는 문제같았음
# 하지만 사이클이 판단되어지는 조건 & 정점 찾는법을 떠올리지 못함


def dfs(node: int) -> None:
    visited[node] = True
    next_node = array[node]
    if not visited[next_node]:
        parent[next_node] = node
        dfs(next_node)
    elif not finished[next_node]:
        find_cycle_node(node, next_node)
    finished[node] = True


def find_cycle_node(node: int, next_node: int) -> None:
    result.append(node)
    if node == next_node:
        return
    find_cycle_node(parent[node], next_node)


N = int(input())
array = [int(input()) for _ in range(N)]
array.insert(0, 0)
visited = [False] * (N + 1)
finished = [False] * (N + 1)
parent = [i for i in range(N + 1)]

result = []
for i in range(1, N + 1):
    dfs(i)
print(len(result))
for i in sorted(result):
    print(i)
