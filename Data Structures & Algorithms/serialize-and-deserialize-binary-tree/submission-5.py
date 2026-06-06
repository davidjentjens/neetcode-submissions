# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return 'N'
        return f'{root.val},{self.serialize(root.left)},{self.serialize(root.right)}'
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(',')
        i = 0

        def helper() -> Optional[TreeNode]:
            nonlocal i
            if nodes[i] == 'N':
                i += 1
                return None

            root_val = int(nodes[i])
            i += 1
            left_node = helper()
            right_node = helper()
            
            return TreeNode(root_val, left_node, right_node)

        return helper()