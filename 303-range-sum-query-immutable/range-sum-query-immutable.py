class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0] * len(nums)
        self.start = 0
        for i in range(len(nums)):
            self.prefix[i] = self.start
            self.start += nums[i]

    def sumRange(self, left: int, right: int) -> int:
        x = self.nums[right] + (self.prefix[right] - self.prefix[left])
        return x
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)