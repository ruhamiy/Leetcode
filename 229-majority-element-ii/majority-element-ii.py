from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        count = Counter(nums)
        return [num for num, freq in count.items() if freq > n // 3]        