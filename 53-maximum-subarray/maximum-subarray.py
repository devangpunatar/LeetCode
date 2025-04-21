class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float('-inf')

        for n in nums:
            curSum += n
            maxSum = max(maxSum, curSum)

            if curSum < 0:
                curSum = 0
        
        return maxSum
