# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0, 0
                
            left_rob, left_skip = helper(root.left)
            right_rob, right_skip = helper(root.right)

            rob_node = root.val + left_skip + right_skip
            skip_node = max(left_rob, left_skip) + max(right_rob, right_skip)

            return rob_node, skip_node
        rob, skip = helper(root)
        return max(rob, skip)