class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        seen = set()
        for i, n in enumerate(self.nums):
            diff = value - n
            if diff in seen:
                return True
            else:
                seen.add(n)
        return False
        
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)