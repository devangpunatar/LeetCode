class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax <= rightMax:
                w = leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
                if w > 0:
                    res += w
            else:
                w = rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])
                if w > 0:
                    res += w
        return res

            