class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        # 1. Build adjacency list and in-degree count
        for a,b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1

        print(adj, in_degree)
        
        # 2. Seed queue with all nodes that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        # 3. Process queue
        count = 0
        while len(queue):
            node = queue.popleft()
            count += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 4. If count == numCourses, no cycle
        return count == numCourses
