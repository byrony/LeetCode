# Jan 8 2020

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.p = image[sr][sc]
        self.newColor = newColor
        if newColor == self.p:
            return image
        self.dfs(image, sr, sc)
        return image
    
    def dfs(self, image, sr, sc):
        if sr < 0 or sr >=len(image) or sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] != self.p:
            return
        else:
            image[sr][sc] = self.newColor
            if sr < len(image)-1:
                self.dfs(image, sr+1, sc)
            if sr > 0:
                self.dfs(image, sr-1, sc)
            if sc < len(image[0])-1:
                self.dfs(image, sr, sc+1)
            if sc > 0:
                self.dfs(image, sr, sc-1)
        