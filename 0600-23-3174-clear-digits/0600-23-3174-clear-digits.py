class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        for i in range(len(s)):
            if (ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')):
                stack.append(s[i])
            else:
                stack.pop()
            
        return "".join(stack)