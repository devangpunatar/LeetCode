class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashSet = set()
        res = []
        for n in nums1:
            if n in hashSet:
                continue
            else:
                hashSet.add(n)
        
        for n in nums2:
            if n in hashSet:
                res.append(n)
                hashSet.remove(n)
            else:
                continue
        return res