import sys
from typing import List, Tuple


# 동물을 고정하고 사대 이분탐색
def solution(guns: List[int], animals: List[Tuple[int, int]], L: int) -> int:
    guns.sort()
    result = 0
    for x, y in animals:
        if y > L:
            continue
        low, high = 0, len(guns) - 1
        left_target = x + y - L
        right_target = x - y + L
        while low <= high:
            mid = (low + high) // 2
            if left_target <= guns[mid] <= right_target:
                result += 1
                break
            elif guns[mid] < left_target:
                low = mid + 1
            else:
                high = mid - 1
    return result


input = sys.stdin.readline
M, N, L = map(int, input().split())
guns = list(map(int, input().split()))
animals = [tuple(map(int, input().split())) for _ in range(N)]
# print(guns)
# print(animals)
print(solution(guns, animals, L))