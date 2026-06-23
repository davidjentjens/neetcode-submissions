class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1
        int_sum = numbers[l] + numbers[r]

        while int_sum != target:
            if int_sum > target:
                r -= 1
            else:
                l += 1
            int_sum = numbers[l] + numbers[r]

        return [l+1,r+1]