# Dec 23 2019

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # use a hashmap to store the count:[index]
        dic = dict()
        dic[0] = [-1] # deal with case when result is 2
        
        tot = 0
        for i, n in enumerate(nums):
            if n == 1:
                tot += 1
            else:
                tot -= 1
            if tot not in dic.keys():
                dic[tot] = [i]
            else:
                dic[tot].append(i)

        # calculate the length of contiguous subarray based on the indexes of equal count
        res = 0
        for k, v in dic.items():
            res = max(res, v[-1]-v[0])
        return res