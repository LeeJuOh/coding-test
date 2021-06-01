'''
서로소 집합을 활용한 사이클 판별 알고리즘
1. 각 간선을 확인하면 두 노드의 루트 노드 확인
    1.1 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행
    1.2 루트 노드가 서로 같다면 사이클이 발생한 것이다
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정 반복
'''


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent(parent, x):
    '''
    경로 압축 기법을 사용한 find 함수
    '''
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

cycle = False
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클 발생 o')
else:
    print('사이클 발생 x')
