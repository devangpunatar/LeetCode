class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        maxProd, minProd = nums[0], nums[0]
        res = maxProd
        for i in range(1, len(nums)):
            curr = nums[i]
            tempMax = max(curr, max(maxProd * curr, minProd * curr))
            minProd = min(curr, min(maxProd * curr, minProd * curr))

            maxProd = tempMax
            res  = max(res, maxProd)

        return res