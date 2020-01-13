# Jan 12 2020

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # edge case
        if len(gas) == 1 and len(cost) == 1:
            return 0 if gas[0] >= cost[0] else -1
        
        i = 0
        loop = 2
        while i < len(gas) and loop:
            if gas[i] <= cost[i]:
                i += 1
                continue
                
            # check if starting from i works
            tot = 0
            start = i
            while (i < len(gas) or i < start) and loop :
                # print(i, start, '***', tot)
                tot += gas[i]-cost[i]
                if tot < 0:
                    break
                i += 1
                if i == len(gas):
                    i = 0
                    loop -=1
                if (i == start-1 or start==0 and i==len(gas)-1 ) and tot + gas[i] >= cost[i]:
                    return start
                
            # if i doesn't work, find next starting index
            i -= 1
            j = i+1 if i<len(gas)-1 else 0
            new_gas = gas[i] - cost[i] + gas[j]
            if new_gas < cost[j]:
                while i < len(gas) and gas[i] > cost[i]:
                    i += 1
                while i < len(gas) and gas[i] < cost[i]:
                    i += 1
                    
        return -1
                    
        