# 역순 연결 리스트2
# 인덱스 m에서 n까지를 역순으로 만들어라, m은 1부터 시작


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    #  예외 처리
    if not head or left == right:
        return head

    root = start = ListNode(None)
    root.next = head

    # start, end 지정
    for _ in range(m - 1):
        start = start.next
    end = start.next

    # 반복하면서 노드 차례대로 뒤집기
    for _ in range(left - right):
        tmp = start.next
        start.next = end.next
        end.next = end.next.next
        start.next.next = tmp
    return root.next