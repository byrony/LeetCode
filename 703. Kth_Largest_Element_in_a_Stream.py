class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.k = k
        self.pool = nums
        heapq.heapify(self.pool)
        while k < len(self.pool):
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        else:
            if self.pool[0] < val:
                heapq.heapreplace(self.pool, val)
        return self.pool[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)