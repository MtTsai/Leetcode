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
        v1 = []
        v2 = []
        while l1 or l2:
            if l1:
                v1.append(l1.val)
                l1 = l1.next
            if l2:
                v2.append(l2.val)
                l2 = l2.next

        i1 = len(v1) - 1
        i2 = len(v2) - 1
        carry = 0
        ans = []
        while i1 >= 0 or i2 >= 0:
            v1_t = v1[i1] if i1 >= 0 else 0
            v2_t = v2[i2] if i2 >= 0 else 0
            i1 -= 1
            i2 -= 1
            ans.append((v1_t + v2_t + carry) % 10)
            
            carry = (v1_t + v2_t + carry) / 10
        
        if carry:
            ans.append(1)

