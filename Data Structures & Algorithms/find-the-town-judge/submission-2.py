class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1   # trusting someone disqualifies you
            score[b] += 1   # being trusted counts toward judge
        for node in range(1, n + 1):
            if score[node] == n - 1:
                return node
        return -1