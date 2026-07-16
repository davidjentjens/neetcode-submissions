class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs, key=lambda log: log[0])
        parent = [i for i in range(n)]
        connected_components = n

        def find(x):
            if parent[x] != x:
                parent[x] = parent[find(parent[x])]
            return parent[x]

        def union(x, y):
            parent_x, parent_y = find(x), find(y)
            if parent_x == parent_y:
                return False
            parent[parent_y] = parent_x
            return True

        for timestamp, x, y in logs:
            if union(x, y):
                connected_components -= 1
            if connected_components == 1:
                return timestamp

        return -1