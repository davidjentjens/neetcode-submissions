# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        # Get top node, first on the preorder list
        head_val = preorder[0]
        head_index = inorder.index(head_val)

        # Get left nodes array of top node, to the left of head node in the inorder tree
        inorder_left_arr = inorder[:head_index]
        # Get right nodes array of top node, to the right of head node in the inorder tree
        inorder_right_arr = inorder[head_index+1:]

        # Get left nodes array of top node, to the left of head node in the preorder tree
        preorder_left_arr = preorder[1:len(inorder_left_arr)+1]
        # Get right nodes array of top node, to the right of head node in the preorder tree
        preorder_right_arr = preorder[-len(inorder_right_arr):]

        # Build left tree from divided preorder and inorder arrays
        leftTree = self.buildTree(preorder_left_arr, inorder_left_arr)
        # Build left right from divided preorder and inorder arrays
        rightTree = self.buildTree(preorder_right_arr, inorder_right_arr)

        return TreeNode(head_val, leftTree, rightTree)