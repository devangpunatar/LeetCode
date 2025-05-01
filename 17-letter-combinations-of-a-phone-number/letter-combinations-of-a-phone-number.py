class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_char = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        res = []
        path = []

        def backtrack(index):
            if index == len(digits):
                res.append("".join(path))
                return

            for char in digit_to_char[digits[index]]:
                path.append(char)
                backtrack(index + 1)
                path.pop()  # backtrack

        backtrack(0)
        return res
