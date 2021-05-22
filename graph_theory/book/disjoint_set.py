'''
서로소 집합은 다양한 알고리즘에 사용 가능
특히 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다는 특징
- 1. 각 간선을 확인하며 두 노드의 루트 노드 확인
    - 1-1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산 수행
    - 1.2. 루트 노드가 서로 같다면 사이클이 발생한 것이다
- 2 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정 반복

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