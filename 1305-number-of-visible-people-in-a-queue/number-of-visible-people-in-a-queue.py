class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            if stack:
                count += 1  # see one more taller person
            res[i] = count
            stack.append(heights[i])
        
        return res




















        '''
        final = []
        for i in range(len(heights)):
            res = 0
            for j in range(i + 1, len(heights)):
                if heights[j] >= heights[i]:
                    res += 1
                    break
                elif heights[j] < heights[i]:
                    if j - 1 == i:
                        res += 1
                    if heights[j] > heights[j - 1]:
                        res += 1
                else:
                    res = 1
            final.append(res)
        return final
        '''