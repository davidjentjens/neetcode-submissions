# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        left_serialized = self.serialize(root.left)
        right_serialized = self.serialize(root.right)
        left_size = len(left_serialized)

        if left_serialized or right_serialized:
            return str(root.val) + f'#{left_size}' + '{' + left_serialized + '|' + right_serialized + '}'

        return str(root.val)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        n = len(data)
        if data == '':
            return None

        # Get root val and index => [1]#1-11 { 2 | 3#1-2{4|5} }
        # Go until either:
        # 1: We find a opening '#' char, which signifies we'll have to continue a tree
        # 2: We reach the end of the data string, which means we have a leaf node
        i = 0
        root_val = []
        while i < n and data[i] != '#':
            root_val.append(data[i])
            i += 1
        root_val = int(''.join(root_val))
        if i == n: return TreeNode(root_val, None, None)

        # Now we need to fetch the mid and end positions to get the left and right
        # sides of the subtree from the root node (we'll need to skip the '#' character)
        i += 1
        mid_pos_val = []
        while data[i] != '{':
            mid_pos_val.append(data[i])
            i += 1
        mid_pos_val = int(''.join(mid_pos_val))
        sub_nodes_str = data[i+1:-1]

        left_node = self.deserialize(sub_nodes_str[:mid_pos_val])
        right_node = self.deserialize(sub_nodes_str[mid_pos_val+1:])

        return TreeNode(root_val, left_node, right_node)
