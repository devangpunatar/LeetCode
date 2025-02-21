class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        
        if not nums:
            return [[lower, upper]] if lower <= upper else []

        if nums[0] > lower:
            res.append([lower, nums[0] - 1])

        first = nums[0]

        for i in range(1, len(nums)):
            interval = []
            if nums[i] - first == 1:
                first = nums[i]
            else:
                interval.append(first + 1)
                interval.append(nums[i] - 1)
                first = nums[i]

            if interval: res.append(interval) 

        if upper > nums[-1]:
            res.append([nums[-1] + 1, upper])
        return res