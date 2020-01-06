# Jan 5 2020

class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        com = ''
        for a in s:
            if a == '1':
                com += '0'
            else:
                com += '1'
        com = '0b' + com
        return int(com, 2)
        