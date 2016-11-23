
# Dynamic programming: bottom up， iterative
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = {}
        ways[0] = 1
        ways[1] = 1
        ways[2] = 2
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
        return ways[n]

result = Solution()
print(result.climbStairs(10))

# Dynamic programming: top down, recursive
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = {}
        ways[1] = 1
        ways[2] = 2
        return self.climbStairs_memo(n, ways)

    def climbStairs_memo(self, n, ways):
        if n in ways:
            return ways[n]
        else:
            if n - 1 not in ways and n - 2 not in ways:
                ways[n] = self.climbStairs_memo(n - 1, ways) + self.climbStairs_memo(n - 2, ways)
            elif n - 1 not in ways and n - 2 in ways:
                ways[n] = self.climbStairs_memo(n - 1, ways) + ways[n - 2]
            elif n - 1 in ways and n - 2 not in ways:
                ways[n] = ways[n - 1] + self.climbStairs_memo(n - 2, ways)
            else:
                ways[n] = ways[n - 1] + ways[n - 2]
            return ways[n]
