# Sep 9, 2021
class Solution:
    def trap(self, height: List[int]) -> int:
        """ Brute force method: The water each idx hold (water above the idx) equals to the min(left largest height - right largest height) - height of the idx
        """
        res = 0
        for i, h in enumerate(height):
            water = min(max(height[:i+1]), max(height[i:])) - h
            if water > 0:
                res += water
        return res

class Solution:
    def trap(self, height: List[int]) -> int:
        # DP: create dictionary which save the left largest height and right largest height for each index
        dic_l = dict()
        dic_r = dict()
        for i in range(len(height)):
            if i == 0:
                dic_l[i] = 0
                max_l = height[i]
            else:
                max_l = max(height[i], max_l)
                dic_l[i] = max_l
        
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                dic_r[i] = 0
                max_r = height[i]
            else:
                max_r = max(height[i], max_r)
                dic_r[i] = max_r
        
        res = 0
        for i, h in enumerate(height):
            water = min(dic_l[i], dic_r[i]) - h
            if water > 0:
                res += water
        return res