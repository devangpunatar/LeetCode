class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        l, r = 0, 0
        merged = []

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1

        merged.extend(left[l:])
        merged.extend(right[r:])

        return merged
