class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates=sorted(candidates)
        def back(i,sub,total):
            if total==target and sub[:] not in res:
                res.append(sub[:])
                return 
            if i>=len(candidates) or total>target:
                return
            sub.append(candidates[i])
            back(i+1,sub,total+candidates[i])
            sub.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            back(i+1,sub,total)
        back(0,[],0)
        return res