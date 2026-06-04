# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate(self, root: Optional[TreeNode], min_val: int, max_val: int) -> bool:
        if not root: return True
        if not (min_val < root.val < max_val): return False
        return self.validate(root.left, min_val, root.val) and self.validate(root.right, root.val, max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))
            