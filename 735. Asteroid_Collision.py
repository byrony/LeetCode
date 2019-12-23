# Dec 15 2019

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            add = True
            while stack and add:
                if stack and stack[-1] > 0 and a < 0:
                    if abs(a) < stack[-1]:
                        add = False
                        break
                    elif abs(a) == stack[-1]:
                        stack.pop()
                        add = False
                    else:
                        stack.pop()
                elif stack and stack[-1] < 0 and a < 0:
                    stack.append(a)
                    add = False
                elif a > 0:
                    stack.append(a)
                    add = False
            if add:
                stack.append(a)
        return stack
                