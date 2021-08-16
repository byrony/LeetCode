# Aug 15, 2021
# This didn't in the information that the intervals is non-overlapping and sorted initially
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals + [newInterval], key = lambda x: x[0])
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
        

# Aug 15, 2021
# Find the insert location
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:  
        # find the insert location
        left, right = intervals[:], []
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                left = intervals[:i]
                right = intervals[i:]
                break
        res = [newInterval[:]]
        for interval in right:
            pre_interval = res.pop()
            res += self.merge_two(pre_interval, interval)
        return left + res
        
    
    def merge_two(self, a, b):
        if a[0] > b[0]:
            a, b = b, a
        
        if a[1] < b[0]:
            return [a, b]
        elif a[1] >= b[0]:
            return [[a[0], max(a[1], b[1])]]
        


# Aug 15, 2021.
# Passed but slow. 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = sorted(intervals + [newInterval], key = lambda x: x[0])

        i = 0
        while i < len(intervals)-1:
            merge_two_int = self.merge_two(intervals[i], intervals[i+1])
            intervals = intervals[:i] + merge_two_int + intervals[i+2:]
            if len(merge_two_int) == 2:
                i += 1
        return intervals
    
    def merge_two(self, a, b):
        if a[1] < b[0]:
            return [a, b]
        elif a[1] >= b[0]:
            return [[a[0], max(a[1], b[1])]]
