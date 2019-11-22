# Nov 21 2019

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
                
        if len(nums) == 0:
            return None
        max_n = -float('Inf')
        idx = 0
        for i in range(len(nums)):
            if nums[i] > max_n:
                max_n = nums[i]
                idx = i
        node = TreeNode(max_n)
        left = nums[:idx]
        right = nums[idx+1:]
        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)
        return node
                