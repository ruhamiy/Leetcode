class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos += 1
        while pos < len(nums):
            nums[pos] = 0
            pos += 1
        