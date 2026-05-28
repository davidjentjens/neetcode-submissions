class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        n = len(s)
        window_frequency = defaultdict(int)
        largest_window = 0
        
        l, r = 0, 0

        while r != n:
            window_frequency[s[r]] += 1

            current_char_freq = window_frequency[s[r]]
            max_freq = max(window_frequency.values())

            if (r - l + 1) - max_freq > k:
                window_frequency[s[l]] -= 1
                l += 1
            r += 1
            largest_window = max(r - l, largest_window)

        return largest_window