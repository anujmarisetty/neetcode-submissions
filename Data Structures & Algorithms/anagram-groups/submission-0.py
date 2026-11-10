class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sr=''.join(sorted(s))
            res[sr].append(s)
        return list(res.values())