# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        self.maxdepth = 0
        def dfs(ptr, depth):
            is_leaf = True
            if ptr.left:
                dfs(ptr.left, depth + 1)
                is_leaf = False
            if ptr.right:
                dfs(ptr.right, depth + 1)
                is_leaf = False
            if is_leaf:
                self.maxdepth = max(self.maxdepth, depth)

        dfs(root, 1)
        return self.maxdepth
