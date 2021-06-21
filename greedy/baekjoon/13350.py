import sys
from typing import List


def solution(N: int, distance: List[int], price: List[int]) -> int:
    total_price = 0
    min_price = sys.maxsize
    for i in range(0, N - 1):
        if price[i] <= min_price:
            min_price = price[i]
        total_price += min_price * distance[i]
    return total_price


input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
print(solution(N, distance, price))