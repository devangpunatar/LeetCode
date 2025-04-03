class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userId -> list of [time, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of followedId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # Ensure user follows themselves
        self.followMap[userId].add(userId)

        # For each followee, push their most recent tweet (if any)
        for followeeId in self.followMap[userId]:
            tweets = self.tweetMap[followeeId]
            if tweets:
                time, tweetId = tweets[-1]
                idx = len(tweets) - 1
                heapq.heappush(minHeap, [time, tweetId, followeeId, idx - 1])

        # Pop most recent tweets, and push next older tweet from same user
        while minHeap and len(res) < 10:
            time, tweetId, uid, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweetMap[uid][idx]
                heapq.heappush(minHeap, [time, tweetId, uid, idx - 1])

        return res

    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
    

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)