class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return -res