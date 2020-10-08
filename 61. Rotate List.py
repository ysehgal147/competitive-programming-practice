# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # Solution 1 (Iterative)

        if head is None:
            return None
        if head.next is None:
            return head
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        k = k % count
        for _ in range(k):
            start = head
            while start:
                if start.next.next is None:
                    start.next.next = head
                    new_start = start.next
                    start.next = None
                start = start.next
            head = new_start
        return head
