'''
신장 트리
- 그래프 알고리즘 문제로 자주 출제되는 문제 유형
- 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재 하지 않는 부분 그래프

크루스칼 알고리즘
- 대표적인 최소 신장 트리 알고리즘
- 그리디 알고리즘으로 분류
    1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다
    2. 간선을 하나씩 확인하여 현재의 간선이 사이클을 발생시키는지 확인한다
        2.1. 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다
        2.2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다
    3 모든 간선에 대하여 2번의 과정을 반복한다
- 시간 복잡도: ElogE (E: 간선의 개수)
'''


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

# 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 원소를 비용으로 설정
    edges.append((cost, a, b))
edges.sort()
print(edges)

# 간선 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
