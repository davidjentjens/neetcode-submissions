# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return max(self.maxHeight(node.left), self.maxHeight(node.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(
            self.maxHeight(root.left), 
            self.maxHeight(root.right), 
            self.maxHeight(root.left) + self.maxHeight(root.right),
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )