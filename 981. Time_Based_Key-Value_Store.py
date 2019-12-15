# Dec 14 2019

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        from bisect import bisect
        if key in self.dic.keys():
            time_list = self.dic[key][0]
            index = bisect(time_list, timestamp)
            self.dic[key][0].insert(index, timestamp)
            self.dic[key][1].insert(index, value)
        else:
            self.dic[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        from bisect import bisect_right
        # binary search based on bisect_right
        if key in self.dic.keys():
            time_list = self.dic[key][0]
            index = bisect_right(time_list, timestamp)
            if index <= len(time_list) and index >= 1:
                return self.dic[key][1][index-1]
            elif index == 0:
                return ''
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)