# 문자열 뒤집기 문제
# 리턴없이 리스트 내부 조작

from typing import List


def reverse_string_by_two_point(s: List[str]) -> None:
    # 전통적인 투포인트 방식
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverse_string_by_pythonic_way(s: List[str]) -> None:
    # 파이썬다운 방식
    # s.reverse()
    s = s[::-1]
