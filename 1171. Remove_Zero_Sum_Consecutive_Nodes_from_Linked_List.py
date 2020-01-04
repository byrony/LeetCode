# Jan 3 2020

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        # find the indexes for each cumulative sum, which is used to find zero sum sequences
        cumsum = 0
        dic = {cumsum:[-1]}
        i = 0
        while i < len(arr):
            cumsum += arr[i]
            if cumsum not in dic.keys():
                dic[cumsum] = [i]
                i += 1
            else:
                del arr[dic[cumsum][0]+1 : i+1]
                i = 0
                cumsum = 0
                dic = {cumsum:[-1]}

        # convert arr to linked list
        cur = dummy = ListNode(0)
        for a in arr:
            cur.next = ListNode(a)
            cur = cur.next
        return dummy.next
