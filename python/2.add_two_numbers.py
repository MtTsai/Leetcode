# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans_root = ListNode(0)
        ans_ptr = None
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            result = v1 + v2 + carry
            
            carry = result / 10
            if ans_ptr:
                ans_ptr.next = ListNode(result % 10)
                ans_ptr = ans_ptr.next
            else:
                ans_ptr = ans_root = ListNode(result % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            ans_ptr.next = ListNode(1)
        return ans_root
