class Solution:
    def numSquares(self, n: int) -> int:
        all_sq = [i**2 for i in range(1, int(n**0.5)+1)]
        curr_level = [0]
        l = 0
        
        run = True
        while run:
            print(curr_level)
            next_level = []
            for i in all_sq:
                for j in curr_level:
                    if j + i == n:
                        run = False
                        return l+1
                    elif j + i < n:
                        next_level.append(j + i)
            curr_level = list(set(next_level))
            l += 1
        
            
        