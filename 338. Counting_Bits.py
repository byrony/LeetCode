# Dec 21 2019

class Solution:
    def countBits(self, num: int) -> List[int]:            
        # wikipedia: https://en.wikipedia.org/wiki/Bit_numbering
        # In computing, the least significant bit (LSB) is the bit position in a binary integer giving the units value, that is, determining whether the number is even or odd.
        # Please note the fact that: n&(n-1) always eliminates the least significant 1
        res = [0]
        for n in range(1, num+1):
            cnt = 0
            while n >= len(res):
                n &= (n-1)
                cnt += 1
            res.append(cnt + res[n])
        return res

# If only return the number of 1 in binary representation of num
class Solution:
    def countBits(self, num: int) -> List[int]:
        # dic saves the number of 1 in the binary representation of 0<=i<=num
        dic = dict()
        dic[0] = 0
        return self.dp(num, dic)
    
    def dp(self, num, dic):
        if num in dic.keys():
            return dic[num]
        else:
            tmp = self.dp(num & (num-1), dic) + 1
            dic[num] = tmp
        return tmp