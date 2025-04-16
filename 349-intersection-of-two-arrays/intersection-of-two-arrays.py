class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashSet = set()
        res = []
        for n in set(nums1):
            hashSet.add(n)
        
        for n in set(nums2):
            if n in hashSet:
                res.append(n)
            else:
                continue
        return res