class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = (len(A) + len(B))
        half = total // 2

        if len(B) < len(A): # if B is smaller, we swap them, that way always A is smaller
            A, B = B, A 
        
        l, r = 0, len(A) - 1

        while True:
            midA = (l + r) // 2 # gives the mid index (left index) of A
            midB = half - midA - 2 # gives the mid index (left index) of B

            Aleft = A[midA] if midA >= 0 else float('-inf')
            Aright = A[midA + 1] if (midA + 1) < len(A) else float('inf')
            Bleft = B[midB] if midB >= 0 else float('-inf')
            Bright = B[midB + 1] if (midB + 1) < len(B) else float('inf')


            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Bleft > Aright:
                l = midA + 1
            else:
                r = midA - 1

