class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            maxH = min(height[l], height[r]) * (r - l)
            res = max(res, maxH)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res