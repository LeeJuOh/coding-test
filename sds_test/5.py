import heapq
import sys
from collections import defaultdict
from typing import Dict, List, Tuple


def mineral_extraction(K: int, minerals: List[List[int]]) -> int:
    area = 0
    left_top, right_top = 0, 0
    left_bottom, right_bottom = 0, 0

    for i in range(K):
        minerals[i].sort(key=lambda x:x[0])
        print(minerals[i])

    return area


def main():
    input = sys.stdin.readline
    total_input_data = []
    T = int(input().rstrip())
    for _ in range(T):
        N, K = map(int, input().split())
        minerals = [[] for _ in range(K)]
        print(minerals)
        for _ in range(N):
            input_data = list(map(int, input().split()))
            minerals[input_data[2] - 1].append((input_data[0], input_data[1]))
        total_input_data.append((K, minerals))
    print(total_input_data)

    for i, data in enumerate(total_input_data):
        print(data)
        result = mineral_extraction(data[0], data[1])
        print(f'#{i} {result}')


main()