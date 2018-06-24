# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        history = {}
        while ptr:
            if history.get(ptr, None):
                return ptr
            else:
                history[ptr] = True
                ptr = ptr.next
        return None
