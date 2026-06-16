class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k, n = len(s1), len(s2)

        l, r = 0, 0
        original_count = Counter(s1)
        char_count = defaultdict(int)

        need = len(original_count)
        have = 0

        for i in range(k):
            char_count[s2[i]] += 1
            if char_count[s2[i]] == original_count[s2[i]]:
                have += 1

        if have == need:
            return True
        
        for r in range(k, n):
            l = r - k
            char_count[s2[r]] += 1
            if char_count[s2[r]] == original_count[s2[r]]:
                have += 1
            if char_count[s2[l]] == original_count[s2[l]]:
                have -= 1
            char_count[s2[l]] -= 1
            if have == need:
                return True

        return False