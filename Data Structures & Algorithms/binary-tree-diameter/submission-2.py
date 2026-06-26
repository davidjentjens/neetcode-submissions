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
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            
            self.diameter = max(left, right, left+right, self.diameter)

            return max(left, right) + 1

        height(root)
        return self.diameter
