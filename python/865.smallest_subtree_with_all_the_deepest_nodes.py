# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def dfs(ptr, depth):
            l = (depth, ptr)
            r = (depth, ptr)
            if ptr.left:
                l = dfs(ptr.left, depth + 1)
            if ptr.right:
                r = dfs(ptr.right, depth + 1)
            
            if l[0] == r[0]:
                return (l[0], ptr)
            else:
                return l if l[0] > r[0] else r
            
        return dfs(root, 0)[1]
