class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(start_index, combination, combination_sum):
            if combination_sum == target:
                ans.append(combination[:])
                return
            for i in range(start_index, len(nums)):
                if combination_sum + nums[i] > target:
                    continue
                combination.append(nums[i])
                combination_sum += nums[i]
                dfs(i, combination, combination_sum)
                combination.pop()
                combination_sum -= nums[i]
        dfs(0, [], 0)
        return ans