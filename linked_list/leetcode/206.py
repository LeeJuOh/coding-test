# 역순 연결리스트
# 연결리스트를 뒤집는 문제

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_by_recursive(self, head: ListNode) -> ListNode:
    # 재귀 방식, node가 None이 될 때까지 재귀호출하면서
    # node.next에는 이전 prev 리스트를 계속 연결해준다.
    # 마지막에는 백트래킹되면서 연결 리스트가 거꾸로 연결된다.
    # 맨 처음에 리턴되는 prev는 뒤집힌 연결리스트의 첫 번째 노드
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


def reverse_list_by_iterative(self, head: ListNode) -> ListNode:
    # 반복문 이용
    node, prev = head, None
    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev