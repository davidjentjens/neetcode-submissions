class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def findParent(x):
            if x != parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(x,y):
            px, py = findParent(x), findParent(y)
            if px == py:
                return
            parent[px] = py

        for a,b in edges:
            union(a,b)

        return sum(1 for i in range(n) if parent[i] == i)