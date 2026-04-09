class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_num = sorted(nums)
        result =[]
        for num in nums:
            result.append(sorted_num.index(num))
        return result