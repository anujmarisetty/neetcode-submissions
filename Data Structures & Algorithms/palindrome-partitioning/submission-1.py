class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        sub=[]
        def back(i):
            if i>=len(s):
                res.append(sub[:])
                return
            for j in range(i,len(s)):
                if ispali(s,i,j):
                    sub.append(s[i:j+1])
                    back(j+1)
                    sub.pop()
        def ispali(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        back(0)
        return res
