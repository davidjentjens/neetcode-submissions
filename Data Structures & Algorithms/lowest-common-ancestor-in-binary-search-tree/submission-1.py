# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If either p or q equal the root node, this is our LCA
        if root.val == p.val or root.val == q.val:
            return root

        # If root is between the values of p and q, this is our LCA
        # This is because in a binary tree, lower values become left-sided children,
        # and higher values become right-sided children, meaning the root node is the
        # division point
        if p.val < root.val < q.val or p.val > root.val > q.val:
            return root

        # If p and q are bigger than root, continue the LCA algorithm to the right
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are smaller than root, continue the LCA algorithm to the left
        return self.lowestCommonAncestor(root.left, p, q)