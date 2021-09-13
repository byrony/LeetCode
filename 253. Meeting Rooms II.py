# Sep 11 2021
# Drop the meetings that can use one room. For the rest meetings, repeat the process.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        inters = sorted(intervals, key=lambda x: x[0])
        rooms = 0
        
        run = True
        while run:
            arr = []
            i = 0
            while i < len(inters) and len(inters) > 0:
                if len(arr) == 0 or arr[-1][1] <= inters[i][0]:
                    inter = inters.pop(i)
                    arr.append(inter)
                else:
                    i += 1
            
            rooms += 1
            if len(inters) == 0:
                run = False
                    
        return rooms

# Use heap
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq
        inters = sorted(intervals, key=lambda x:x[0])
        
        # a min heap which keeps the meeting end time, the meetings are in different rooms
        arr = []
        heapq.heappush(arr, inters[0][1])
        for i in range(1, len(inters)):
            # if current meeting end time is earlier than next meeting start time, update the end time to be the end time of next meeting
            # Otherwise, push the new meeting end time to the heap. Means it need another room
            if arr[0] <= inters[i][0]:
                heapq.heappop(arr)
            heapq.heappush(arr, inters[i][1])
        
        return len(arr)
            
                
