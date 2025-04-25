class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        temp = 0
        leftMax = len(height) * [0]
        rightMax = len(height) * [0]

        for i in range(len(height)):
            leftMax[i] = temp
            temp = max(temp, height[i])
        
        temp = 0
        for i in range(len(height) - 1, -1 , -1):
            rightMax[i] = temp
            temp = max(temp, height[i])
        
        for i in range(len(height)):
            if min(leftMax[i], rightMax[i]) > height[i]:
                res += min(leftMax[i], rightMax[i]) - height[i]

        return res
        