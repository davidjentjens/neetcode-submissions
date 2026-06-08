class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        seen_elements = set()

        def dfs(combination, combination_sum):
            if combination_sum == target:
                combination_tuple = tuple(sorted(combination))
                if combination_tuple not in seen_elements:
                    ans.append(combination[:])
                    seen_elements.add(combination_tuple)
                return
            for num in nums:
                if combination_sum + num > target:
                    continue
                combination.append(num)
                combination_sum += num
                dfs(combination, combination_sum)
                combination.pop()
                combination_sum -= num
        dfs([], 0)
        return ans