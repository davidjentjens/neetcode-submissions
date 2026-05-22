class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sorted_s, sorted_t = sorted(s), sorted(t)

        for char_s, char_t in zip(sorted_s, sorted_t):
            if char_s != char_t:
                return False
        
        return True
