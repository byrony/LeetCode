# Aug 22 2021
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.score_dic = dict()
        
        score_1 = self.Score(nums, 0, len(nums)-1, 1)
        score_2 = self.Score(nums, 0, len(nums)-1, 2)
        
        # print(score_1, score_2)
        # print(self.score_dic)
        return score_1 >= score_2
    
    
    def Score(self, nums, l, r, turn):
        if (l, r, turn) in self.score_dic.keys():
            return self.score_dic[(l,r,turn)]
        
        if r-l <= 1:
            if turn == 1:
                self.score_dic[(l,r,turn)] = max(nums[l:r+1])
                return self.score_dic[(l,r,turn)]
            else:
                self.score_dic[(l,r,turn)] = min(nums[l:r+1])
                return self.score_dic[(l,r,turn)]

        if turn == 1:
            self.score_dic[(l,r,turn)] = max(nums[l] + self.Score(nums, l+1, r, 2), nums[r] + self.Score(nums, l, r-1, 2))
        elif turn == 2:
            self.score_dic[(l,r,turn)] = min(self.Score(nums, l+1, r, 1), self.Score(nums, l, r-1, 1))
        return self.score_dic[(l,r,turn)]
        
                       