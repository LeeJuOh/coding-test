import sys
from typing import List


def solution(N: int, K: int, sensors: List[int]) -> int:
    sensors.sort()
    difference = []
    for i in range(N - 1):
        difference.append((sensors[i+1] - sensors[i]))
    difference.sort(reverse=True)

    total_length = sensors[-1] - sensors[0]
    return total_length - sum(difference[:K-1])


input = sys.stdin.readline
N = int(input().rstrip())
K = int(input().rstrip())
sensors = list(map(int, input().split()))
print(solution(N, K, sensors))
