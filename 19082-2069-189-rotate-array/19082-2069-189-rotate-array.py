class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        n = len(nums)
        k = k % n  # Ensure k is within bounds
        
        reverse(0, n - 1)   # Reverse the entire array
        reverse(0, k - 1)   # Reverse the first k elements
        reverse(k, n - 1)   # Reverse the remaining elements