import re
from collections import deque
from typing import Deque

# 팰린드롬 문제
# .isalpha(): 문자열이 영어 혹은 한글로 되어있으면 true
# .isalnum(): 영어, 한글, 숫자


def is_palindrome_by_list(s: str) -> bool:
    # 리스트로 변환해서 푸는 방법
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True


def is_palindrome_by_deque(s: str) -> bool:
    # 데크로 최적화
    strs: Deque = deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


def is_palindrome_by_slicing(s: str) -> bool:
    # 슬라이싱 사용
    # 슬라이싱은 다른 기능, loop, 재귀보다 처리속도가 빠르다.
    # 정규식 사용

    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


s = "A man, a plan, a canal: Panama"
print(is_palindrome_by_list(s))
print(is_palindrome_by_deque(s))
print(is_palindrome_by_slicing(s))
