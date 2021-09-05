# Sep 5 2021
class Solution:
    def reorganizeString(self, S: str) -> str:
        import heapq
        
        dic = dict()
        for s in S:
            if s not in dic:
                dic[s] = 1
            else:
                dic[s] += 1
        arr = []
        for s, cnt in dic.items():
            arr.append((-cnt, s))
            
        heapq.heapify(arr)
        
        # reconstruct a string
        res = ''
        while len(arr) >=2 :
            # pop the two most frequent character
            cnt1, s1 = heappop(arr)
            cnt2, s2 = heappop(arr)
            
            res += (s1+s2)*1
            cnt1 +=1
            cnt2 += 1
            
            # push the first character back to heap, note the count is negative
            if -1*cnt1 > 0:
                heappush(arr, (cnt1, s1))
            if -1*cnt2 > 0:
                heappush(arr, (cnt2, s2))
            
        # print(res, arr, '===')
        if len(arr) == 1:
            if -1*arr[0][0] >= 2:
                return ''
            else:
                res += arr[0][1] * (-1*arr[0][0])
        return res
            