# Oct 30, 2019

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = self.slope(coordinates[0][0], coordinates[0][1],
                          coordinates[1][0], coordinates[1][1])
        
        for i in range(2, len(coordinates)):                
            if slope != self.slope(coordinates[0][0], coordinates[0][1],
                                   coordinates[i][0], coordinates[i][1]):
                return False
            else:
                continue
        return True
    
    def slope(self, x1, y1, x2, y2):
        if y1 == y2:
            slope = float('Inf')
        elif x1 == x2:
            slope = 0
        else:
            slope = (y2-y1)/(x2-x1)
        return slope