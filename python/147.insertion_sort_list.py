# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        ptr = out = ListNode(head.val)
        head = head.next
        
        while head:
            ins = ListNode(head.val)
            if head.val > ptr.val:
                while ptr:
                    if not ptr.next or ptr.next.val > head.val:
                        break
                    ptr = ptr.next
                ins.next = ptr.next
                ptr.next = ins
            elif head.val > out.val:
                ptr = out
                while ptr:
                    if not ptr.next or ptr.next.val > head.val:
                        break
                    ptr = ptr.next
                ins.next = ptr.next
                ptr.next = ins
            else:
                ins.next = out
                out = ins
            ptr = ins
            head = head.next
            
        
        return out
