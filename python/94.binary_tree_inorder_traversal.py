# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        self.out = []
        
        def dfs(ptr):
            if ptr.left:
                dfs(ptr.left)
            self.out.append(ptr.val)
            if ptr.right:
                dfs(ptr.right)
        
        dfs(root)
        return self.out
