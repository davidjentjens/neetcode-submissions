class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        r, l = 0, 0
        t_set = set(t)
        window_counter = defaultdict(int)
        t_counter = Counter(t)

        found_valid_window = False
        minimum_substring = s

        def valid_window() -> bool:
            for c in t_set:
                if window_counter[c] < t_counter[c]: 
                    return False
            return True

        for r in range(n):
            if s[r] in t_set: 
                window_counter[s[r]] += 1
            while valid_window():
                if s[l] in t_set: window_counter[s[l]] -= 1
                found_valid_window = True
                minimum_substring = min(s[l:r+1], minimum_substring, key=len)
                l += 1
        
        return minimum_substring if found_valid_window else ""
            