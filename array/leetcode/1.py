# 두 수의 합
# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
# 매우 간단하지만 최적화할 수 있는 여러 가지 방법이 숨어져있어서 높은 빈도 출제

from typing import List


def two_sum_by_brute_force(nums: List[int], target: int) -> List[int]:
    # 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인
    # 무차별 대입 방식인 브루트 포스

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_by_in_keyword(nums: List[int], target: int) -> List[int]:
    # 모든 조합을 비교하지 않고 타겟에서 첫번째 값을 뺀 값이 존재하는지 탐색
    # 똑같이 O(n^2)이지만 in 연산이 훨씬 빠르다.

    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [i, nums[i + 1:].index(complement) + (i + 1)]


def two_sum_by_dict(nums: List[int], target: int) -> List[int]:
    # 첫 번째 수를 뺀 결과 키조회
    # O(1) ~ O(n)

    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


def two_sum_by_dict2(nums: List[int], target: int) -> List[int]:
    # 첫 번째 수를 뺀 결과 키조회
    # 하나의 for문으로 통합

    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


nums = [2, 7, 11, 15]
target = 26
print(two_sum_by_brute_force(nums, target))
print(two_sum_by_in_keyword(nums, target))
print(two_sum_by_dict(nums, target))
print(two_sum_by_dict2(nums, target))