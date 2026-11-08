class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        def back(i,sub):
            if i>=len(nums):
                if sub[:] not in res:
                    res.append(sub[:])
                return
            sub.append(nums[i])
            back(i+1,sub)
            sub.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            back(i+1,sub)
        back(0,[])
        return res
            
