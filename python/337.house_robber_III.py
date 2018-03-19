# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        class RobNode(object):
            def __init__(self):
                self.T_robm = -1
                self.F_robm = -1
                self.left = None
                self.right = None

        def robtree(ptr, rptr, is_rob):
            if not ptr:
                return 0

            if not rptr.left:
                rptr.left = RobNode()
            if not rptr.right:
                rptr.right = RobNode()

            if not is_rob and rptr.F_robm != -1:
                return rptr.F_robm

            if is_rob and rptr.T_robm != -1:
                return rptr.T_robm

            if is_rob:
                rptr.T_robm = ptr.val + robtree(ptr.left, rptr.left, False) + robtree(ptr.right, rptr.right, False)
                return rptr.T_robm
            else:
                rob_money = 0
                rob_money = max(rob_money, robtree(ptr.left, rptr.left, True)  + robtree(ptr.right, rptr.right, True))
                rob_money = max(rob_money, robtree(ptr.left, rptr.left, True)  + robtree(ptr.right, rptr.right, False))
                rob_money = max(rob_money, robtree(ptr.left, rptr.left, False) + robtree(ptr.right, rptr.right, True))
                rob_money = max(rob_money, robtree(ptr.left, rptr.left, False) + robtree(ptr.right, rptr.right, False))

                rptr.F_robm = rob_money
                return rptr.F_robm

        rob_root = RobNode()
        return max(robtree(root, rob_root, True), robtree(root, rob_root, False))

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)
    root.right.right = TreeNode(1)

    ans = 9
    out = Solution().rob(root)
    if out != ans:
        print "Wrong Answer"
        print "Expect: {}".format(ans)
        print "Output: {}".format(out)

    print "Done"
