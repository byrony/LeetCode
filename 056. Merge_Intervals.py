# Aug 15, 2021
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            else:
                pre_interval = res.pop()
                res += self.merge_two(pre_interval, interval)
        return res
    
    def merge_two(self, a, b):
        if a[1] < b[0]:
            return [a, b]
        elif a[1] >= b[0]:
            return [[a[0], max(a[1], b[1])]]
        
        
        



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        init = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            res += self.merge_two(init, intervals[i])
            if i < len(intervals)-1:
                init = res.pop() 
        return res
    
    def merge_two(self, a, b):
        # print(a,b)
        # a[0] is smaller than b[0] after sort
        if a[1] < b[0]:
            return [a, b]
        elif a[1] >= b[0] and a[1] <= b[1]:
            return [[a[0], b[1]]]
        elif a[1] > b[0] and a[1] > b[1]:
            return [a]
        