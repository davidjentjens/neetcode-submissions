# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Saved position map of inorder array, for a O(1) index lookup further in the problem
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(preorder_start, inorder_start, inorder_end):
            # If start of the inorder array is bigger than the end, it means we've reached
            # the last indexes of the array, so we can return None as the child of the
            # previous node
            if inorder_start > inorder_end: return None

            # Get top node, first on the preorder list
            # PREORDER => [(5)] | 4, 2, 1, 3 | 7, 6, 8
            head_val = preorder[preorder_start]

             # Find its index in the inorder array
            # INORDER => 1, 2, 3, 4 | [(5)] | 6, 7, 8
            head_inorder_index = inorder_map[head_val]

            # Get left nodes array of top node, +1 to the preorder start
            # PREORDER => (5) | [4, 2, 1, 3] | 7, 6, 8
            left_preorder_start = preorder_start + 1
            # Get right nodes array of top node, +size of the left array +1 to the preorder start
            # PREORDER => (5) | 4, 2, 1, 3 | [7, 6, 8]
            left_size = head_inorder_index - inorder_start
            right_preorder_start = preorder_start + left_size + 1

            # Get left nodes range of top node, to the left of head node in the inorder tree
            # INORDER => [1, 2, 3, 4] | (5) | 6, 7, 8
            left_inorder_start = inorder_start
            left_inorder_end = head_inorder_index - 1

            # Get right nodes range of top node, to the right of head node in the inorder tree
            # INORDER => 1, 2, 3, 4 | (5) | [6, 7, 8]
            right_inorder_start = head_inorder_index + 1
            right_inorder_end = inorder_end

            # Build left tree recursively from divided preorder and inorder arrays
            leftTree = helper(left_preorder_start, left_inorder_start, left_inorder_end)
            # Build left right recursively from divided preorder and inorder arrays
            rightTree = helper(right_preorder_start, right_inorder_start, right_inorder_end)
    
            return TreeNode(head_val, leftTree, rightTree)
        
        # Start with the full arrays for the first recursion, which will get updated
        # downstream
        return helper(0, 0, len(preorder)-1)

        