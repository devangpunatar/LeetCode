class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices
        res = []

        for i in range(len(nums)):
            # Remove elements out of current window
            if q and q[0] <= i - k:
                q.popleft()

            # Maintain decreasing order in deque
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            q.append(i)

            # Add to result once first window is formed
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
