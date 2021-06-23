from typing import List

# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수


def array_pair_sum_by_me(nums: List[int]):
    nums.sort()
    pair_sum = 0
    for i in range(len(nums)//2):
        pair_sum += min(nums[i], nums[1])
    return pair_sum


def array_pair_sum_by_sort(nums: List[int]):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum


def array_pair_sum_by_even(nums: List[int]):
    # 잘 생각해보면 짝수번째 값의 합이 답
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n
    return sum


def array_pair_sum_by_pythonic_way(nums: List[int]):
    # 파이썬다운 방식
    return sum(sorted(nums)[::2])


nums = [6, 2, 6, 5, 1, 2]
print(array_pair_sum_by_pythonic_way[nums])
