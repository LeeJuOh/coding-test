import sys
from typing import List, Tuple
import time


def solution(
    queries: List[Tuple[int, int]]
) -> None:
    global T, X, MAX

    def update(left: int, right: int, node: int, index: int, diff: int) -> None:
        if left <= index <= right:
            tree[node] += diff
            if left != right:
                mid = (left + right) // 2
                update(left, mid, node * 2, index, diff)
                update(mid + 1, right, node * 2 + 1, index, diff)

    def query(left: int, right: int, node: int, count: int) -> int:
        if left == right:
            return left

        mid = (left + right) // 2
        if tree[node * 2] >= count:
            return query(left, mid, node * 2, count)
        else:
            return query(mid + 1, right, node * 2 + 1, count - tree[node * 2])

    s = 1
    while(s < MAX):
        s *= 2
    tree = [0] * (s * 2)

    for type, value in queries:
        if type == 1:
            update(1, s, 1, value, 1)
        else:
            index = query(1, s, 1, value)
            update(1, s, 1, index, -1)
            print(index)


start_time = time.time()
input = sys.stdin.readline
MAX = 2000000
N = int(input().rstrip())
queries = []
for i in range(N):
    T, X = map(int, input().split())
    queries.append((T, X))
solution(queries)
end_time = time.time()
print('time', end_time - start_time)