# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head or not k:
            return head

        n = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            n += 1

        rotate = k % n
        if rotate == 0:
            return head

        ptr.next = head
        
        ptr = head
        for _ in range(n - rotate - 1):
            ptr = ptr.next
            
        head = ptr.next
        ptr.next = None
        
        return head
