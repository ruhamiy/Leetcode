class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        result = []
        p_count = Counter(p)
        s_count = Counter()
        k = len(p)
        for i in range (len(s)):
            s_count[s[i]] += 1
            if i >= k:
                if s_count[s[i-k]] == 1:
                    del s_count[s[i-k]]
                else:
                    s_count[s[i-k]] -= 1
            if s_count == p_count:
                result.append(i-k+1)
        return result