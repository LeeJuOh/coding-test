# 원형 데크 디자인
# MyCircularDeque(k): Constructor, set the size of the deque to be k.
# insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
# insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
# deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
# deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
# getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
# getRear(): Gets the last item from Deque. If the deque is empty, return -1.
# isEmpty(): Checks whether Deque is empty or not.
# isFull(): Checks whether Deque is full or not.


# 이중 연결리스트 구현
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head, self.tail = ListNode(None), ListNode(None)

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """