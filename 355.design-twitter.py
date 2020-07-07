#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start

from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followers = defaultdict(set)
        self.posts = defaultdict(list)


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.posts[userId].append(tweetId)
        # print("postTweet ", userId, tweetId, self.posts)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        allPosts = []
        allPosts.extend(self.posts.get(userId, []))
        for follower in self.followers[userId]:
            allPosts.extend(self.posts.get(follower, []))
        
        
        maxIndex = min(10, len(allPosts))
        allPosts.sort(reverse=True)

        # print(userId, allPosts)

        return allPosts[:maxIndex]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.followers[followerId].add(followeeId)
        # print("follow ", followerId, followeeId, self.followers)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        currFollowers = self.followers[followerId]
        if followeeId in currFollowers:
            self.followers[followerId].remove(followeeId)
        # print("unfollow ", followerId, followeeId, self.followers)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(1,5)
# param_2 = obj.getNewsFeed(1)
# # print(param_2)
# obj.postTweet(2, 6)
# obj.follow(1,2)
# param_2 = obj.getNewsFeed(1)
# # print(param_2)
# obj.unfollow(1,2)
# param_2 = obj.getNewsFeed(1)
# # print(param_2)
# @lc code=end

