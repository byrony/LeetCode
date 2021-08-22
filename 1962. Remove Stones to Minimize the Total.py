# Aug 20 2021
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq
        
        piles.sort()
        stone_cnt = sum(piles)
        
        # create a heap to save the pile that has removed stone for one time
        piles_hp = []
        heapq.heapify(piles_hp)
        
        stone_rm = 0
        while k > 0:
            if len(piles_hp) == 0:
                p = piles.pop()
            elif len(piles) == 0:
                p = -1*heapq.heappop(piles_hp)
            elif piles[-1] >= piles_hp[0]*(-1):
                p = piles.pop()
            elif piles[-1] < piles_hp[0]*(-1):
                p = -1*heapq.heappop(piles_hp)
            
            k -= 1
            p_rm = int(p/2)
            stone_rm += p_rm
            
            heapq.heappush(piles_hp, -1*(p-p_rm))
        return stone_cnt - stone_rm