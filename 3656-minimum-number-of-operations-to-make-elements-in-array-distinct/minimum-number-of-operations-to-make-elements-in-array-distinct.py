import math

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashSet = set()
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in hashSet:
                hashSet.add(nums[i])
            else:
                res = i + 1
                break
        
        res = math.ceil(res / 3)
        return res
            
