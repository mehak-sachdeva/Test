# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://www.youtube.com/watch?v=13m9ZCB8gjw
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            print("None")
        else:
            print(root.val)

        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left == None:
            if right is None:
                print("returning None from right")
            else:
                print("return from right", right.val)
            return right
        if right == None:
            if left is None:
                print("returning None from left")
            else:
                print("return from left", left.val)
            return left
        print("returning root", root.val)
        return root

s = Solution()
t = TreeNode(3)
t.left = TreeNode(6)
t.right = TreeNode(8)
t.left.left = TreeNode(2)
t.left.right = TreeNode(11)
t.left.right.left = TreeNode(9)
t.left.right.right = TreeNode(5)
t.right.right = TreeNode(13)
t.right.right.left = TreeNode(7)

x = s.lowestCommonAncestor(t, t.left.left, t.left.right.right)
print(x.val)