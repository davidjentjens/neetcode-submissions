[1,2,3,3]


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        sorted_nums = sorted(nums)
        previous_num = None

        for num in sorted_nums:
            if num == previous_num: 
                return True
            previous_num = num
        
        return False
            