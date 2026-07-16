class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for equation, value in zip(equations, values):
            if equation[0] not in graph:
                graph[equation[0]] = {}
            graph[equation[0]][equation[1]] = value
            if equation[1] not in graph:
                graph[equation[1]] = {}
            graph[equation[1]][equation[0]] = 1/value
        print(graph)

        visited = set()
        div_eval = -1
        def dfs(node, target, path_multiplier):
            nonlocal div_eval
            print(f'GOING FROM NODE {node} to {target} -> MULTIPLIER {path_multiplier}')
            if node == target:
                div_eval = path_multiplier
                return
            if node not in graph or node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor, target, path_multiplier * graph[node][neighbor])

        result = []
        for query in queries:
            visited = set()
            div_eval = -1
            print(f'\nORIGIN: {query[0]} TARGET: {query[1]}')
            if query[0] not in graph:
                result.append(-1)
                continue
            dfs(query[0], query[1], 1)
            result.append(div_eval)

        return result

