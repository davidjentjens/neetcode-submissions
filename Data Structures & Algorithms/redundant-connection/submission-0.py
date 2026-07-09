class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        
        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x

        def union(x,y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]

