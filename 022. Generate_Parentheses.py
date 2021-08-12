class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr_paren = ''
        res = []
        self.allParen(n, n, curr_paren, res)
        return set(res)
    
    def allParen(self, n, m, curr_paren, res):
        """ recurison function: n: number of "("; m: number of ")"
        f(n, m) = f(n-1, m) + "(" + f(n, m-1) + ")"
        Note: to generate valid parentheses, we always start with (, n<=m is 
        always true till end
        """
        if n == 0 and m == 0:
            res.append(curr_paren)
        elif n <= m and n >= 0:
            self.allParen(n, m-1, curr_paren+')', res)
            self.allParen(n-1, m, curr_paren+'(', res)


        