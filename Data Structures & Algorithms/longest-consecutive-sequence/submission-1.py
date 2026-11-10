class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        l=0
        for i in n:
            if (i-1) not in n:
                lent=1
                while(i+lent) in n:
                    lent+=1
                l=max(l,lent)
        return l 