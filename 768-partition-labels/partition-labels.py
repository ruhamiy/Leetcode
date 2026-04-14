class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {ch: i for i, ch in enumerate(s)}
        result = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])  
            if i == end:  
                result.append(end - start + 1)
                start = i + 1

        return result