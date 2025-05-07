class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ["+", "-", "*", "/"]:
                x = stack.pop()
                y = stack.pop()
                if c == "+": 
                    z = y + x
                elif c == "-":
                    z = y - x
                elif c == "*":
                    z = y * x
                elif c == "/":
                    z = int(y / x)
                stack.append(z)
            else:
                stack.append(int(c))

        return stack[0]
                
        