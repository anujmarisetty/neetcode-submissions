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
            back(i+1,sub,total)
        back(0,[],0)
        return res