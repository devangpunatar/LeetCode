class Solution:
    def sumDistance(self, nums, s, d):
        MOD = 10**9 + 7
        n = len(nums)
        final_positions = []

        for i in range(n):
            if s[i] == 'L':
                final_positions.append(nums[i] - d)
            else:
                final_positions.append(nums[i] + d)

        final_positions.sort()
        
        # Efficiently compute sum of pairwise distances using prefix sum trick
        prefix_sum = 0
        result = 0
        for i in range(n):
            result = (result + (final_positions[i] * i - prefix_sum)) % MOD
            prefix_sum = (prefix_sum + final_positions[i]) % MOD

        return result
