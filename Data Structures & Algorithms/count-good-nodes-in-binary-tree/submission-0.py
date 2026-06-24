# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def biggestValueNode(node: TreeNode, biggest_val: int):
            nonlocal good_nodes
            if not node:
                return
            if node.val >= biggest_val:
                good_nodes += 1
            biggestValueNode(node.left, max(biggest_val, node.val))
            biggestValueNode(node.right, max(biggest_val, node.val))

        biggestValueNode(root, root.val)
        
        return good_nodes

