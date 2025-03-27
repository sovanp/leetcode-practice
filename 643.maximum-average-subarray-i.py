#
# @lc app=leetcode id=643 lang=python
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # Step 1: sum the first window of size k
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Step 2: slide the window
        for i in range(k, len(nums)):
            # Add next num, remove first num
            window_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, window_sum)
            
        # Step 3: return the average
        return float(max_sum) / k
        
# @lc code=end

