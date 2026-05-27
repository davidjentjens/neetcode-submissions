class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        window_start = 0
        longest_substring = 0

        for i, char in enumerate(s):
            if char in seen_chars:
                target = seen_chars[char]
                while window_start != target+1:
                    del seen_chars[s[window_start]]
                    window_start += 1
            seen_chars[char] = i
            longest_substring = max(i - window_start + 1, longest_substring)

        return longest_substring
