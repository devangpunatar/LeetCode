class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if stack and i == '+':
                stack.append(stack[-1] + stack[-2])
            elif stack and i == 'D':
                stack.append(stack[-1] * 2)
            elif stack and i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
        
        return sum(stack)
        
        