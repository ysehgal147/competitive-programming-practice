# 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        # Solution 1 (Hare-Tortoise)

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

        # Solution 2 (Array Based)

        arr = []
        while head:
            arr.append(head)
            head = head.next
        return arr[len(arr)//2]
