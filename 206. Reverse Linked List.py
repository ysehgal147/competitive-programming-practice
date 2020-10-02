# 206. Reverse Linked List

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # Solution 1 (Iteratively)

        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

        # Solution 2 (Recursively)

        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
