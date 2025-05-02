class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        num = 0

        for c in s:
            if c.isdigit():
                num = (num * 10) + int(c)
            elif c == '[':
                stack.append((res, num))
                res = ""
                num = 0
            elif c == ']':
                temp, repeat = stack.pop()
                res = temp + res * repeat
            else:
                res += c
        return res
            