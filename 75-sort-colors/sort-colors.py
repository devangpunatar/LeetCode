class Solution:
    def sortColors(self, nums: List[int]) -> None:

        i, l, r = 0, 0, len(nums) - 1
        
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
        
        

            