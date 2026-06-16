# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        right_side_nodes = []

        while len(queue) > 0:
            new_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if child: queue.append(child)
            right_side_nodes.append(node.val)

        return right_side_nodes
                