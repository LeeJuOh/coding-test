# 자신을 제외한 배열의 곱


from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    # 미리 전체 곱셈 값을 구해놓고 각 항목별로 자기 자신을 나눠서 풀이는 x
    # 자기 자신을 제외하고 왼쪽의 곱셈 결과와 오른쪽의 곱셈 결과를 곱해야 한다.
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]

    p = 1
    # 왼쪽 곱셈 결과를 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out


nums = [-1, 1, 0, -3, 3]
product_except_self(nums)