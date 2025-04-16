class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        hashMap = {}
        for i in nums1:
            for j in nums2:
                hashMap[i + j] = hashMap.get(i + j, 0) + 1 

        for k in nums3:
            for l in nums4:
                if -(k + l) in hashMap:
                    res += hashMap.get(-(k + l), 0)
        return res