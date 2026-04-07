"""bubble sort """
"""class Solution(object):
    def sortPeople(self, names, heights):
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
    
        n = len(names)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
        
        return names"""


"""selection sort """
"""class Solution(object):
    def sortPeople(self, names, heights):
    
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
    
        n = len(names)
        for i in range(n):
            max_index = i
            for j in range(i + 1, n):
                if heights[j] > heights[max_index]:
                    max_index = j
            heights[i], heights[max_index] = heights[max_index], heights[i]
            names[i], names[max_index] = names[max_index], names[i]
        
        return names"""

        
"""insertion sort 
 class Solution(object):
    def sortPeople(self, names, heights):
       
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        
        n = len(names)
       
        for i in range(1, n):
            key_height = heights[i]
            key_name = names[i]
            j = i - 1
            
            while j >= 0 and heights[j] < key_height:
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j -= 1
            
            heights[j + 1] = key_height
            names[j + 1] = key_name
        
        return names"""



"""counting sort"""
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        maximum = max(heights)
        count = [[] for _ in range(maximum + 1)]
        for name, height in zip(names, heights):
            count[height].append(name)
        
        result = []
        for h in range(maximum, -1, -1):
            for name in count[h]:
                result.append(name)
        
        return result