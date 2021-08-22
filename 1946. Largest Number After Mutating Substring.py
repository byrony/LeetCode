# Aug 20 2021
# Note for the first letter of substring, if num[i]=change[int(num[i])], no need to change 
# for the following letters after the first letter, change if num[i]=change[int(num[i])] to extend the substring
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = [n for n in num]
        for i in range(len(num)):
            if int(num[i]) < change[int(num[i])]:
                num[i] = str(change[int(num[i])])
                for j in range(i+1, len(num)):
                    if int(num[j]) <= change[int(num[j])]:
                        num[j] = str(change[int(num[j])])
                    else:
                        break
                break
        return ''.join(num)
                
        
