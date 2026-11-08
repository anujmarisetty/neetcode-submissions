class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        def check(piles,mid,h):
            tot=0
            for i in piles:
                tot+=(i+mid-1)//mid
            return tot<=h
        while low<high:
            mid=(low+high)//2
            hrs=check(piles,mid,h)
            if hrs:
                high=mid
            else:
                low=mid+1
        return low
