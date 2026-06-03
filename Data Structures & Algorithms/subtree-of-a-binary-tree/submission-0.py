# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeIsEqual(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if root.val != subRoot.val: return False
        # Continue comparing the root and subRoots children
        return self.treeIsEqual(root.left, subRoot.left) and self.treeIsEqual(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the root is None, it means we reached the end of the tree and found no subtrees
        if not root: return False

        # We need to check if the current tree is equal
        # If not, we continue checking its subtrees
        return self.treeIsEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


            