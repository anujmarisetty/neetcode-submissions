class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        di={}
        l=0
        maxl=0
        freq=0
        for r in range(len(s)):
            di[s[r]]=1+di.get(s[r],0)
            freq=max(freq,di[s[r]])
            while (r-l+1)-freq>k:
                di[s[l]]-=1
                l+=1
            maxl=max(maxl,r-l+1)
        return maxl
                
