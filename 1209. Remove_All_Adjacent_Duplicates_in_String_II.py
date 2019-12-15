# Dec 12 2019

# Exceeded Time Limit
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [i for i in s[0:k]]
        for c in s[k:]:
            # print(stack)
            if len(stack) < k-1:
                stack.append(c)
                continue
            for i in range(1,k):
                if c != stack[-i]:
                    stack.append(c)
                    break
            else:
                del stack[len(stack)-k+1 : len(stack)]
        return ''.join(stack)


# Accepted
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        for c in s[1:]:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                del stack[-1]
            # print(stack)
        return ''.join([i[0]*i[1] for i in stack])