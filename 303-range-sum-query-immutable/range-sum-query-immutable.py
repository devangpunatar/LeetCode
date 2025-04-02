class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for n in nums:
            curr += n
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            return self.prefix[right] - self.prefix[left - 1]
        else:
            return self.prefix[right] 

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)