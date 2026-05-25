class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product, product_without_0 = 1, 1
        modified_arr = [None] * n
        zero_num = 0

        if n == 1:
            return [1]

        for num in nums:
            if num != 0:
                product_without_0 *= num
            else: 
                zero_num += 1
            product *= num

        if zero_num > 1:
            return [0] * n

        for i, num in enumerate(nums):
            if num == 0:
                modified_arr[i] = int(product_without_0)
                continue
            modified_arr[i] = int(product/num)
        return modified_arr