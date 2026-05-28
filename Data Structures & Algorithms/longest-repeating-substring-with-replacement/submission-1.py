class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        window_frequency = defaultdict(int)

        max_freq = 0
        largest_window = 0
        l, r = 0, 0

        for r in range(n):
            window_frequency[s[r]] += 1

            current_char_freq = window_frequency[s[r]]
            max_freq = max(window_frequency.values())

            # If window is invalid, meaning the window is larger than 
            # k + the repeating char freq...
            # => 
            # Shrink the window by 1, because we're trying to get the
            # longest window.
            # When we shrink the window, we must remove the dynamic
            # frequencies from characters outside the window
            if (r - l + 1) - max_freq > k:
                window_frequency[s[l]] -= 1
                l += 1

            largest_window = max(r - l + 1, largest_window)

        return largest_window