"""
416. Partition Equal Subset Sum
Solved
Medium

Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        n = len(nums)
        dp = [[0]*(W+1) for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, W+1):
                if wt[i-1] < j:
                    dp[i][j] = max(val[i-1] + dp[i][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][W]
        """
        if sum(nums)%2 != 0:
            return False
        n = len(nums)
        sum_ = sum(nums)//2
        dp = [[False]*(sum_+1) for i in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(sum_+1):
                if nums[i-1]<=sum_:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]



                    
        
