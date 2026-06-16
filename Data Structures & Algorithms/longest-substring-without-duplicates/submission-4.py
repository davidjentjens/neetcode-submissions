class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_count = defaultdict(int)
        l, r = 0, 0
        largest = 0
        
        while r < len(s):
            char_count[s[r]] += 1
            while char_count[s[r]] > 1:
                char_count[s[l]] -= 1
                l += 1
            largest = max(largest, r-l+1)
            r += 1
        
        return largest