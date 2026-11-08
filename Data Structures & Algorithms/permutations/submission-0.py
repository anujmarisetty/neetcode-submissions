class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(sub):
            if len(sub)==len(nums):
                res.append(sub[:])
                return
            for num in nums:
                if num not in sub:
                    sub.append(num)
                    back(sub)
                    sub.pop()
        back([])
        return res