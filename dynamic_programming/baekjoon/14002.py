import sys
from typing import List


# using dp
def solution(size: int, nums: List[int]) -> None:
    dp = [1]*N
    for i in range(1, N):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp))
    order = max(dp)
    lst = []
    for i in range(N-1, -1, -1):
        if dp[i] == order:
            lst.append(nums[i])
            order -= 1
    lst.reverse()
    print(' '.join(map(str, lst)))


input = sys.stdin.readline
N = int(input().rstrip())
nums = list(map(int, input().split()))
solution(N, nums)
