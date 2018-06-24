# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        global ans
        ans = 0
        def DFS(node, curr):
            if node:
                curr.append(node.val)
                sum_t = 0
                for n in reversed(curr):
                    sum_t += n
                    if sum_t == sum:
                        global ans
                        ans += 1
                DFS(node.left, curr)
                DFS(node.right, curr)
                curr.pop()
  
        DFS(root, collections.deque([]))
        return ans
