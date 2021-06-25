# 페어의 노드 스왑
# 연결리스트를 입력받아 페어 단위로 스와하라.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs_by_swap_value(self, head: ListNode) -> ListNode:
    # 연결리스트의 노드를 변경하는게 아닌
    # 노드 구조는 그대로 유지하고 값만 변경
    # 실용성과는 거리가 멀다. 대개 연결리스트는 복잡한 구조체로 되어있고
    # 사실상 값만 바꾸는 것은 매우 어려운 일
    # 하지만 이 문제한정으론 간단하다.

    cur = head
    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next
    return head


def swap_pairs_by_iterative(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next
    return root.next


def swap_pairs_by_recursive(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = swap_pairs_by_recursive(p.next)
        p.next = head
        return p
    return head
