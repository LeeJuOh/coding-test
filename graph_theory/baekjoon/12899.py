import sys
from typing import List, Set, Tuple
from bisect import bisect_left


def solution(
    queries: List[Tuple[int, int]],
    nums: Set[int]
) -> None:
    global T, X

    def update(left: int, right: int, node: int, index: int, diff: int) -> None:
        if left <= index <= right:
            tree[node] += diff
            if left != right:
                mid = (left + right) // 2
                update(left, mid, node * 2, index, diff)
                update(mid + 1, right, node * 2 + 1, index, diff)

    def query(left: int, right: int, node: int, count: int) -> int:
        tree[node] -= 1
        if left == right:
            return left

        mid = (left + right) // 2
        if tree[node * 2] >= count:
            return query(left, mid, node * 2, count)
        else:
            return query(mid + 1, right, node * 2 + 1, count - tree[node * 2])

    s = 1
    while(s < len(nums)):
        s *= 2
    tree = [0] * (s * 2)

    nums.add(0)
    nums = sorted(list(nums))
    for type, value in queries:
        if type == 1:
            index = bisect_left(nums, value)
            update(1, s, 1, index, 1)
        else:
            index = query(1, s, 1, value)
            update(1, s, 1, index, -1)
            print(nums[index])


input = sys.stdin.readline
N = int(input().rstrip())
nums = set()
queries = []
for i in range(N):
    T, X = map(int, input().split())
    if T == 1:
        nums.add(X)
    queries.append((T, X))
solution(queries, nums)
