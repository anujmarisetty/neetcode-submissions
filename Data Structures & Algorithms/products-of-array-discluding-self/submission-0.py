class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[1]*len(nums)
        for i in range(1,len(nums)):
            r[i]=r[i-1]*nums[i-1]
        p=1
        for i in range(len(nums)-1,-1,-1):
            r[i]*=p
            p*=nums[i]
        return r