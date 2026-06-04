# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_list = []

        def inOrder(node: Optional[TreeNode]):
            if not node: return
            inOrder(node.left)
            ordered_list.append(node.val)
            inOrder(node.right)

        inOrder(root)
        return ordered_list[k-1]