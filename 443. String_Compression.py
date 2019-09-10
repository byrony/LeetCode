class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        length = len(chars)
        while i < length-1:
            j = i    
            while j < length and chars[j]==chars[i]:
                j += 1
            
            if j-1-i >= 1:
                tmp = str(j - i)
                chars[(i+1):(i+len(tmp)+1)] = [t for t in tmp]
                del chars[(i+len(tmp)+1):j]
                # print(chars)
            
                # check next different character
                i += len(tmp) + 1
                length = len(chars)
            else:
                i += 1
                length = len(chars)
        return len(chars)
