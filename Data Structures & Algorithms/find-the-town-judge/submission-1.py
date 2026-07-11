class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for a,b in trust:
            graph[a].append(b)
            in_degree[b] += 1

        for node in range(1, n+1):
            # If node has all nodes pointing to it and points to no nodes, it is the judge
            if in_degree[node] == n-1 and len(graph[node]) == 0:
                return node

        return -1