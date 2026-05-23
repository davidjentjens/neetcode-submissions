class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = {}

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in sorted_anagrams:
                sorted_anagrams[sorted_str].append(string)
            else:
                sorted_anagrams[sorted_str] = [string]

        return list(sorted_anagrams.values())