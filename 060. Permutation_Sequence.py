
# Time Limit Exceeded 
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        depth = n
        res = {'order':0, 'list':None}
        order = 1
        self.dfs(nums, [], depth, res, k, order)
        return ''.join([str(i) for i in res['list']])
    
    def dfs(self, nums, arr, depth, res, k, order):
        if res['order'] == k:
            return
        if len(arr) < depth:
            for i, n in enumerate(nums):
                self.dfs(nums[0:i]+nums[(i+1):len(nums)], arr+[n], depth, res, k, order)
        else:
            res['order'] += order
            res['list'] = arr
            # print(res)

# need check how python pass a variable by reference. Need to updated an object within function.
# https://stackoverflow.com/questions/22054698/python-modifying-list-inside-a-function