# 두 수의 덧셈
# 역순으로 저장딘 연결리스트의 숫자를 더하라

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers_by_full_adder(l1: ListNode, l2: ListNode) -> ListNode:
    # 논리 회로의 전가산기와 유사한 형태로 구현
    # 이진법이 아니라 십진법이라는 차이만 있을 뿐, 자리올림수(carry)를 구하는 것까지
    # 가산기의 원리와 거의 동일
    #   - 입력값 a,b 이전의 carry in 3가지 입력으로 sum과 다음 carry out 여부를 결정
    #   - xor: 숫자가 같지않을 때 참(배타적일때 참), 더해서 mod 2를 구하는 것과 동일

    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next
