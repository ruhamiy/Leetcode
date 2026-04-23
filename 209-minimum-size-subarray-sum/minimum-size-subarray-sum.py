class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        cur_sum = 0 
        min_len = float('inf')
        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len= min(min_len, right-left+1)
                cur_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else  min_len