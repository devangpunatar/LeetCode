class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9, just add one to this digit and return the list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and we continue to the next digit
            digits[i] = 0
        
        # If we have gone through all digits and all were 9, we need to add an additional 1 at the beginning
        return [1] + digits
