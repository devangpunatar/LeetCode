class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)
        
        for r in range(len(ratings) - 1):
            if ratings[r + 1] > ratings[r]:
                res[r + 1] = res[r] + 1
        for r in range(len(ratings) - 1, 0, -1):
            if ratings[r - 1] > ratings[r]:
                if res[r] + 1 > res[r - 1]:
                    res[r - 1] = res[r] + 1 
        print(res)
        return sum(res)