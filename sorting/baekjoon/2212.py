import sys
from typing import List


# 총 센서 길이(max - min)에서 두 센서간 길이의 차이가 가장 큰 것들을 k-1개 빼면 된다고 생각
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
