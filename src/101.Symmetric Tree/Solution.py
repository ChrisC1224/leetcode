# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)
    def isMirror(self, l, r):
        if l == None and r == None:
            return True
        elif l == None or r == None:
            return False
        else:
            return l.val==r.val and self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)
