class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int)

        dp[0] = 1 # (0 sum) -> 1 way

        for i in range(len(nums)):
            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp
        return dp[target]




        '''
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # (0 elements, 0 sum) -> 1 way

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count

        return dp[len(nums)][target]

        
        memoization

        dp = {} # (index, cur_sum) -> number of ways

        def backtrack(i, cur_sum):
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]

            if i == len(nums):
                return 1 if cur_sum == target else 0

            dp[(i, cur_sum)] = (
                backtrack(i + 1, cur_sum + nums[i]) +
                backtrack(i + 1, cur_sum - nums[i])
                )
            return dp[(i, cur_sum)]

        return backtrack(0, 0)
        '''