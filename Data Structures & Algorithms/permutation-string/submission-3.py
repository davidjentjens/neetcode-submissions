class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k, n = len(s1), len(s2)

        l, r = 0, 0
        original_count = Counter(s1)
        char_count = defaultdict(int)

        def sameCount():
            print(original_count, char_count)
            for c in original_count:
                if original_count[c] != char_count[c]:
                    return False
            return True

        for i in range(k):
            char_count[s2[i]] += 1
        
        if sameCount():
            return True

        for r in range(k, n):
            l = r - k
            char_count[s2[r]] += 1
            char_count[s2[l]] -= 1
            if sameCount():
                return True

        return False


        

        