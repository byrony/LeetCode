# Feb 2 2020

# without stack, O(k*n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # from left to right, remove the first peak, loop k times
        arr = [int(n) for n in num]
        while k and arr:
            idx = 0
            while idx < len(arr):
                if idx == len(arr)-1 or arr[idx]>arr[idx+1]:
                    del arr[idx]
                    k -= 1
                    idx += 1
                    break
                else:
                    idx += 1
        if not arr:
            return '0'
        else:
            return str(int(''.join([str(n) for n in arr])))



# with stack, O(n)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr = [int(n) for n in num]
        stack = []
        while k and arr:
            a = arr.pop(0)
            if not stack:
                stack.append(a)
            elif stack[-1] > a:
                while k and stack and stack[-1] > a:
                    stack.pop()
                    k -= 1
                stack.append(a)
            elif stack[-1] <= a:
                stack.append(a)
            # print(k, a, stack, arr)
        if k > 0:
            if len(stack) - k > 0:
                return ''.join([str(n) for n in stack[:len(stack)-k]])
            else:
                return '0'
        elif arr:
            return str(int(''.join([str(n) for n in stack + arr])))
        else:
            return str(int(''.join([str(n) for n in stack])))


# with stack, O(n). Optimized
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
            # print(k, stack)
            
        if k > 0:
            if len(stack) - k > 0:
                return str(int(''.join(stack[:len(stack)-k])))
            else:
                return '0'
        return str(int(''.join(stack)))

