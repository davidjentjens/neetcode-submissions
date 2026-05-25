class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers_set = set(nums)
        biggest_sequence = 0

        for num in numbers_set:
            if num - 1 not in numbers_set:
                current_sequence = 0
                while num in numbers_set:
                    current_sequence += 1
                    num += 1
                biggest_sequence = max(current_sequence, biggest_sequence)
            
        return biggest_sequence
