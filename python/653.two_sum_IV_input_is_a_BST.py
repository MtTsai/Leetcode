# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        remains = {}
        
        def post_order_traverse(node):
            if node.left:
                if post_order_traverse(node.left):
                    return True

            if node.val not in remains.keys():
                remains[k - node.val] = ''
            else:
                return True

            if node.right:
                if post_order_traverse(node.right):
                    return True
                    
            return False


