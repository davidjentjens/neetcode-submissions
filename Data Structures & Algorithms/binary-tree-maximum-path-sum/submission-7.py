# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        max_val = float('-inf')

        def helper(root: Optional[TreeNode]) -> int:
            nonlocal max_val

            # We reached the end of the path, return -infinity, because the maximum path 
            # of a "None" node is -infinity
            if not root: return 0

            # Get the maximum path sum of both left and right subtrees
            leftPathSum = helper(root.left)
            rightPathSum = helper(root.right)

            # Get the maximum path sum between the permutations of the "non-bend" paths
            # Root
            # Left Sum + Root
            # Right Sum + Root
            non_bend_paths = max(
                root.val,
                leftPathSum + root.val,
                rightPathSum + root.val,
            )
            
            # Compare that with the bended path, to get the maximum value
            bend_path = max(non_bend_paths, leftPathSum + rightPathSum + root.val)

            # Do not propagate it upwards, because a path can only have one bend
            # Save it to the max_val variable instead, to use later
            max_val = max(max_val, bend_path)

            # Propagate only the non-bended paths, so the algorithm can "extend"
            # the path upwards
            return non_bend_paths
        
        helper(root)

        return max_val