# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def mirror_cmp(lnode, rnode):
            if lnode == None and rnode == None:
                return True
            if not lnode or not rnode or lnode.val != rnode.val:
                return False
            return mirror_cmp(lnode.left, rnode.right) and mirror_cmp(lnode.right, rnode.left)
    
        return mirror_cmp(root, root)
