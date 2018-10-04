# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.ans = None
        def dfs(ptr):
            if ptr.right:
                dfs(ptr.right)
            
            t = self.ans
            self.ans = TreeNode(ptr.val)
            self.ans.right = t
            
            if ptr.left:
                dfs(ptr.left)
                
        
        
        dfs(root)
        
        return self.ans
