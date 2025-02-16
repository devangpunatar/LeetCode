class Solution:
    def dailyTemperatures(self, temps):
        res = [0] * len(temps)
        stack = [] # pair [temp, index]

        for i, t in enumerate(temps):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res