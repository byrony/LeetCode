# Jan 5 2020

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = dict()
        for i, n in enumerate(nums2):
            dic[n] = i
        
        res = []
        for n1 in nums1:
            i = dic[n1] + 1
            while i < len(nums2):
                if nums2[i] > n1:
                    res.append(nums2[i])
                    break
                else:
                    i += 1
            if i == len(nums2):
                res.append(-1)
        return res
            