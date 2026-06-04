# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest_k = None

        def inOrder(node: Optional[TreeNode]):
            nonlocal k, smallest_k
            if not node or smallest_k is not None: return
            inOrder(node.left)
            k -= 1
            if (k == 0): 
                smallest_k = node.val
                return
            inOrder(node.right)

        inOrder(root)
        return smallest_k