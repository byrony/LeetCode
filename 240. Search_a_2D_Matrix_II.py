class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        row = len(matrix)-1
        col = len(matrix[0])
        for i in range(row, -1, -1):
            if matrix[i][0] > target:
                continue
            else:
                if self.binarySearch(matrix[i], target):
                    return True
        return False
        
    def binarySearch(self, nums, target):
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return True
        return False