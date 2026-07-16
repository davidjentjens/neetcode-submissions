class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (num, den), value in zip(equations, values):
            if num not in graph:
                graph[num] = {}
            graph[num][den] = value
            if den not in graph:
                graph[den] = {}
            graph[den][num] = 1/value

        visited = set()
        def dfs(node, target, acc):
            if node == target:
                return acc
            if node not in graph or node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                found = dfs(neighbor, target, acc * graph[node][neighbor])
                if found is not None:
                    return found
            return None

        result = []
        for query in queries:
            visited = set()
            if query[0] not in graph:
                result.append(-1)
                continue
            div_eval = dfs(query[0], query[1], 1)
            result.append(div_eval if div_eval is not None else -1)

        return result

