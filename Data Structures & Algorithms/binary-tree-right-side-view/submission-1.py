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
        levels = []
        while len(queue) > 0:
            new_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child: queue.append(child)
            levels.append(new_level)

        return [level[-1] for level in levels]
                