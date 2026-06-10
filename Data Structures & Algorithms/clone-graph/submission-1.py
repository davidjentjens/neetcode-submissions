"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node_original: Optional['Node']) -> Optional['Node']:
        visited = {}

        if not node_original:
            return None

        def dfs(node: Node) -> Optional['Node']:
            # Node is already visited, we must return it's respective clone
            if node in visited:
                return visited[node]

            # We then need to mark the current node as visited
            copy_node = Node(node.val)
            visited[node] = copy_node

            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor))
            
            return copy_node

        return dfs(node_original)
