class Solution:
    def numTilePossibilities(self, tiles):
        tiles = ''.join(sorted(tiles))
        res = []
        cnt = [0]
        self.dfs(tiles, '', cnt)
        return cnt[0]-1
    
    def dfs(self, tiles, arr, cnt):
        cnt[0] += 1
        if len(tiles) > 0:
            for i, c in enumerate(tiles):
                j = i - 1
                if j >= 0 and tiles[j] == tiles[i]:
                    continue
                else:
                    self.dfs(tiles[0:i]+tiles[i+1:], arr+c, cnt)
                