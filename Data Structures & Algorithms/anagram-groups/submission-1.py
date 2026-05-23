class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = defaultdict(list)

        for string in strs:
            sorted_str = "".join(sorted(string))
            sorted_anagrams[sorted_str].append(string)

        return list(sorted_anagrams.values())