# Sep 10 2021
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        import bisect
        if stones[1] - stones[0] > 1:
            return False
        
        self.dic = dict()
        return self.dp(stones, 1, 1)
    
    def dp(self, stones, i, k):
        # conditions need stop: 1) no index found, which returns -1, 2) step is <=0
        if i < 0:
            return
        if k <= 0:
            return
        
        # note the key of dictionary is (index, step), since there could be multiple different step(speed) at the same index
        if (i,k) in self.dic.keys():
            return self.dic[(i,k)]
                
        if i < 0 or i >= len(stones):
            self.dic[(i, k)] = False
            return False
        elif i == len(stones)-1:
            self.dic[(i, k)] = True
            return True
        
        i_1 = self.bins_index(stones, stones[i]+k-1)
        i_2 = self.bins_index(stones, stones[i]+k)
        i_3 = self.bins_index(stones, stones[i]+k+1)
        
        # print(i_1, i_2, i_3, k, '===')
        self.dic[(i, k)] = self.dp(stones, i_1, k-1) or self.dp(stones, i_2, k) or self.dp(stones, i_3, k+1)
        return self.dic[(i, k)]
        
    def bins_index(self, a, x):
        i = bisect.bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        else:
            return -1