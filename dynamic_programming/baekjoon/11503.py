import sys
from bisect import bisect_left
from typing import List


# using binary search
# only length
def solution(size: int, nums: List[int]) -> None:
    result = [nums[0]]
    for i in range(size):
        if nums[i] > result[-1]:
            result.append(nums[i])
            # print('append', result)
        else:
            # print('before', result)
            idx = bisect_left(result, nums[i])
            result[idx] = nums[i]
            # print('after', result)

    print(len(result))


input = sys.stdin.readline
N = int(input().rstrip())
nums = list(map(int, input().split()))
solution(N, nums)
