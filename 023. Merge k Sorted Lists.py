# Aug 28, 2021
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        res = ListNode()
        curr = res
        
        lists = [(l, i) for i, l in enumerate(lists)]
        
        # curr_list keeps the first node of each of the k lists
        curr_list = []
        for l, i in lists:
            if l is not None:
                curr_list.append((l.val, i))
        heapq.heapify(curr_list)

        while len(curr_list) > 0:
            small_ele, which_list_pop = heapq.heappop(curr_list)
            
            # update the list that popped smallest number
            lists[which_list_pop] = (lists[which_list_pop][0].next, which_list_pop)
            if lists[which_list_pop][0] is not None:
                heapq.heappush(curr_list, (lists[which_list_pop][0].val, which_list_pop))
                
            curr.next = ListNode(small_ele)
            curr = curr.next
        return res.next
        
        