# 홀짝 연결리스트
# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성
# 공간 복잡도 O(1), 시간 복잡도 O(n)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_List(head: ListNode) -> ListNode:
    # 에외 처리
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next

        even.next = even.next.next
        even = even.next

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head
