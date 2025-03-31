class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(nums):
            n = len(nums)

            if n == 1:
                return nums
            m = n // 2
            L = nums[:m]
            R = nums[m:] 

            L = merge_sort(L)
            R = merge_sort(R)
            l, r = 0, 0
            L_len = len(L)
            R_len = len(R)

            sorted_arr = [0] * n
            i = 0

            while l < L_len and r < R_len:
                if L[l] <= R[r]:
                    sorted_arr[i] = L[l]
                    l += 1
                else:
                    sorted_arr[i] = R[r]
                    r += 1
                i += 1
            
            while l < L_len:
                sorted_arr[i] = L[l]
                l += 1
                i += 1
            
            while r < R_len:
                sorted_arr[i] = R[r]
                i += 1
                r += 1

            return sorted_arr

        return merge_sort(nums)