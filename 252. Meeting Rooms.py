# Sep 11 2021
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals)-1):
            j = i + 1
            if intervals[i][1] > intervals[j][0]:
                return False
        return True