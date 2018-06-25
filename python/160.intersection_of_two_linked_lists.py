# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lenA, lenB = 1, 1
        ptrA, ptrB = headA, headB
        while ptrA.next:
            ptrA = ptrA.next
            lenA += 1
        while ptrB.next:
            ptrB = ptrB.next
            lenB += 1
        if ptrA != ptrB:
            return None
        else:
            ptrA, ptrB = headA, headB
            while lenA > lenB:
                ptrA = ptrA.next
                lenA -= 1
            while lenA < lenB:
                ptrB = ptrB.next
                lenB -= 1
            while ptrA != ptrB:
                ptrA, ptrB = ptrA.next, ptrB.next
            return ptrA
