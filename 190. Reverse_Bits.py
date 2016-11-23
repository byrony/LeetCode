class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        temp = str(bin(n)[2:])[::-1]
        s = '0b' +  temp + '0' * (32-len(temp))
        return int(s,2)

result = Solution()
test = result.reverseBits(43261596)
print(test)