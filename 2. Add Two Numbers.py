# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Solution 1

        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next

        # Solution 2 (Limited Cases Working)

        if l1.val == 0 and l2.val == 0:
            return ListNode()
        number1=0
        while l1:
            number1*=10
            number1+=(l1.val)
            l1=l1.next
            
        number2=0
        while l2:
            number2*=10
            number2+=(l2.val)
            l2=l2.next
            
        number = number1 + number2
        
        head = curr = ListNode()
        
        while number>0:
            curr.next = ListNode(number%10)
            number = number//10
            curr=curr.next
            
        return head.next
