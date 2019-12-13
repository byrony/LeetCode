# Dec 11 2019

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            if c == ']':
                # find the str between "[" and "]"
                tmp_s = '' 
                stack.pop()
                while stack[-1] != '[':
                    tmp_s = stack.pop() + tmp_s
                    
                stack.pop()
                
                # find the str of digits before "["
                tmp_n = ''
                while stack and stack[-1].isdigit():
                    tmp_n = stack.pop() + tmp_n
                
                stack += int(tmp_n)*tmp_s
            # print(stack)
        return ''.join(stack)