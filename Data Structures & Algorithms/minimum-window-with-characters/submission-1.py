class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        r, l = 0, 0
        window_counter = defaultdict(int)
        t_counter = Counter(t)

        have, need = 0, len(t_counter)

        found_valid_window = False
        minimum_substring = s

        for r in range(n):
            # Increment window to the right, adjusting the "have" var as needed
            if s[r] in t_counter: 
                window_counter[s[r]] += 1
                if window_counter[s[r]] == t_counter[s[r]]:
                    have += 1
            
            # If the window is valid, keep shrinking it from the left, to find the minimum
            while have == need:
                minimum_substring = min(s[l:r+1], minimum_substring, key=len)
                found_valid_window = True
                # If a "t" char is removed and counts no longer match, decrement the "have" var
                if s[l] in t_counter: 
                    window_counter[s[l]] -= 1
                    if window_counter[s[l]] < t_counter[s[l]]:
                        have -= 1
                l += 1
        
        return minimum_substring if found_valid_window else ""
            