class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        char_count = defaultdict(int)
        largest = 0

        while r < len(s):
            window_size = r-l+1
            char_count[s[r]] += 1
            max_freq = max(char_count.values())
            while window_size - max_freq > k:
                char_count[s[l]] -= 1
                l += 1
                window_size = r-l+1
                max_freq = max(char_count.values())
            largest = max(largest, window_size)
            r += 1

        return largest