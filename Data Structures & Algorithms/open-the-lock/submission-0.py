from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends: return -1

        start_combination = [0,0,0,0]

        def strCombination(combination):
            return ''.join(str(i) for i in combination)

        def getValidNeighbors(combination):
            possible_combinations = [
                [(combination[0] + 1) % 10, combination[1], combination[2], combination[3]],
                [(combination[0] - 1) % 10, combination[1], combination[2], combination[3]],
                [combination[0], (combination[1] + 1) % 10, combination[2], combination[3]],
                [combination[0], (combination[1] - 1) % 10, combination[2], combination[3]],
                [combination[0], combination[1], (combination[2] + 1) % 10, combination[3]],
                [combination[0], combination[1], (combination[2] - 1) % 10, combination[3]],
                [combination[0], combination[1], combination[2], (combination[3] + 1) % 10],
                [combination[0], combination[1], combination[2], (combination[3] - 1) % 10],
            ]
            valid_neighbors = []
            for neighbor in possible_combinations:
                if strCombination(neighbor) not in deadends:
                    valid_neighbors.append(neighbor)
            return valid_neighbors

        queue = deque([[0,0,0,0]])
        visited = {strCombination([0,0,0,0])}
        steps = 0

        while queue:
            for _ in range(len(queue)):
                combination = queue.popleft()
                if strCombination(combination) == target:
                    return steps
                for neighbor in getValidNeighbors(combination):
                    neighbor_str = strCombination(neighbor)
                    if neighbor_str not in visited:
                        visited.add(neighbor_str)
                        queue.append(neighbor)
            steps += 1

        return -1
            
            

        