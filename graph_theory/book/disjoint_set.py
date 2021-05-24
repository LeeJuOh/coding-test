'''
- 서로소 집합: 공통 원소가 없는 두 집합을 의미

- 서로소 집합 자료구조: 서로 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
    - union 과 find 2개의 연산으로 조작 가능, union-find 자료구조라고 불리기도 한다
    - union: 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
    - find: 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산
    - 트리 자료구조를 이용하여 집합을 표현

- 서로서 집합 계산 알고리즘
    1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다
        1.1. A와 B의 루트 노드 A', B'를 각각 찾는다
        1.2. A'를 B'의 부모 노드로 설정한다(B'가 A'를 가리키도록 한다)
    2. 모든 union 연산을 처리할 때까지 1번 과정 반복

- 서로소 집합은 다양한 알고리즘에 사용 가능
참고) 방향 그래프에서의 사이클 여부는 DFS 이용하여 판별 가능
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
    시간 복잡도: O(V)
    '''
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent_by_path_compression(parent, a, b):
    a = find_parent_by_path_compression(parent, a)
    b = find_parent_by_path_compression(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_parent_by_path_compression(parent, x):
    '''
    경로 압축 기법을 사용한 find 함수
    '''
    if parent[x] != x:
        return find_parent_by_path_compression(parent, parent[x])
    return parent[x]


v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent_by_path_compression(parent, a, b)
print(parent)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent_by_path_compression(parent, i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')
print()


# v, e = map(int, input().split())
# parent = [0] * (v + 1)

# for i in range(1, v + 1):
#     parent[i] = i

# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

# print('각 원소가 속한 집합: ', end='')
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=' ')
# print()

# print('부모 테이블: ', end='')
# for i in range(1, v + 1):
#     print(parent[i], end=' ')
# print()