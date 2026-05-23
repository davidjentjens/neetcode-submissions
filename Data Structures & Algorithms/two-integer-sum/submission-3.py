class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        visited = {}

        for i in range(n):
            complement = target - nums[i]
            if complement in visited:
                return [visited[complement], i]
            visited[nums[i]] = i

        return []