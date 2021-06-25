# 팰린드롬 연결리스트
# 연결 리스트가 팰린드롬 구조인지 판별하라
# Definition for singly-linked list.
from collections import deque
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome_by_deque(head: ListNode) -> bool:
    q: Deque = deque()

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 판별
    while len(q) > 1:
        if q.popleft() != q.pop():  # 인덱스를 지정하여 처음과 끝 값을 비교
            return False

    return True


def is_palindrome_by_runner(head: ListNode) -> bool:
    # 러너 기법 활용
    # fast runner와 slow runner를 각각 출발시키면 빠른 러너가 끝에 도착하면
    # 느린 러너는 중간에 도착, 느린 러너는 중간까지 이동하면서 역순으로 연결리스트 rev를 만들어 나간다
    # 이제 중간에 도달한 느린 러너가 나머지 경로를 이동할 때, 역순으로 만든 연결 리스트의 값들과 일치하는지 확인
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


input = [1, 2, 3, 4]
head = None
prev = None
for data in reversed(input):
    head = ListNode(data, prev)
    prev = head
print(is_palindrome_by_deque(head))
print(is_palindrome_by_runner(head))