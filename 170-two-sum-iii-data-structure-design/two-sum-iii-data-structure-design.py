class TwoSum:

    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        self.nums[number] = 1 + self.nums.get(number, 0)

    def find(self, value: int) -> bool:
        for n in self.nums.keys():
            diff = value - n
            if n != diff:
                if diff in self.nums:
                    return True
            elif self.nums[n] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)