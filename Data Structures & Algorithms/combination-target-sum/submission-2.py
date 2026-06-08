class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        # Sort the nums array in order to use an optimization later on
        nums.sort()

        def dfs(start_index, combination, combination_sum):
            # Stop if we've reached a leaf, i.e. reached the target
            if combination_sum == target:
                ans.append(combination[:])
                return
            # If not, try branching from the current node to explore other options
            for i in range(start_index, len(nums)):
                # Prune if possible, since backtracking is expensive
                # The pruning in this case is to stop if we reached the target
                if combination_sum + nums[i] > target:
                    # We can break here, because in a sorted nums array, all
                    # subsequent numbers will breach the target
                    break
                # Append the current number to the combination and add to sum
                combination.append(nums[i])
                combination_sum += nums[i]
                # Continue recursion until target is reached for this node
                dfs(i, combination, combination_sum)
                # Backtrack and remove num from combination
                combination.pop()
                combination_sum -= nums[i]

        dfs(0, [], 0)
        return ans
