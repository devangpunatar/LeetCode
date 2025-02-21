class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        return len(set(nums) - {0})  # Count unique nonzero elements

