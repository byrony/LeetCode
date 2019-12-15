# Dec 13 2019

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # check all non-overlap cases
        l = rec1[2]<=rec2[0]
        r = rec1[0]>=rec2[2]
        d = rec1[3]<=rec2[1] 
        u = rec1[1]>=rec2[3]
        
        return not(l or r or d or u)