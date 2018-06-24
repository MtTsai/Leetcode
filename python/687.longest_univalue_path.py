# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.ans = 0
        def DFS(node):
            if node:
                llen = DFS(node.left)
                rlen = DFS(node.right)
                if node.left and node.left.val == node.val and node.right and node.right.val == node.val:
                    self.ans = max(self.ans, llen + rlen + 2)
                    return max(llen + 1, rlen + 1)
                elif node.left and node.left.val == node.val:
                    self.ans = max(self.ans, llen + 1)
                    return llen + 1
                elif node.right and node.right.val == node.val:
                    self.ans = max(self.ans, rlen + 1)
                    return rlen + 1
                else:
                    return 0
            else:
                return 0
        
        DFS(root)
        return self.ans
