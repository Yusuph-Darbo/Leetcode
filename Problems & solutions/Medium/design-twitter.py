# Approach:
# Store each user's tweets with a timestamp count so newer tweets have priority.
# For the news feed, add the latest tweet from each followed user into a heap,
# then repeatedly pop the newest tweet and add that user's next most recent tweet.
#
# Time: O(f log f)
# Space: O(f)


class Twitter:

    def __init__(self):
        self.count = 0
        # userId holds a list of (count, tweetId)
        self.tweetMap = defaultdict(list)
        # userId holds a set of followIds
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)

        for followId in self.followMap[userId]:
            if followId in self.tweetMap:
                index = len(self.tweetMap[followId]) - 1
                count, tweetId = self.tweetMap[followId][index]

                heapq.heappush(minHeap, (count, tweetId, followId, index - 1))

        while minHeap and len(res) < 10:
            count, tweetId, followId, index = heapq.heappop(minHeap)

            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followId][index]

                heapq.heappush(minHeap, (count, tweetId, followId, index - 1))

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
