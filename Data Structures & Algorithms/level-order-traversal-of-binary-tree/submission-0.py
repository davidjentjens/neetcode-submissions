# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        order_traversal = []

        while len(queue) > 0:
            n = len(queue)
            new_level = []
            for _ in range(n):
                node = queue.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child: queue.append(child)
            order_traversal.append(new_level)
            
        return order_traversal