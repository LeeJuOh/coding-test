# 정렬되어 있는 두 연결 리스트를 합쳐라

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists_by_recursive(l1: ListNode, l2: ListNode) -> ListNode:
    # 정렬된 리스트므로 병합 정렬에서
    # 마지막 조합시 첫 번째 값부터
    # 차례대로만 비교하면 한 번에 해결되듯이
    # 이 또한 첫 번째부터 비교하면서 리턴하는 풀이
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = merge_two_lists_by_recursive(l1.next, l2)
    return l1


l1 = [1, 2, 4]
l2 = [1, 3, 4]

l1_head = None
prev = None
for data in reversed(l1):
    l1_head = ListNode(data, prev)
    prev = l1_head

l2_head = None
prev = None
for data in reversed(l2):
    l2_head = ListNode(data, prev)
    prev = l2_head

result = merge_two_lists_by_recursive(l1_head, l2_head)
while result.next:
    print(result.val, end=' ')
    result = result.next
print()

