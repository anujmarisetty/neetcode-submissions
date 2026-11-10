class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        di={')':'(','}':'{',']':'['}
        for i in s:
            if i in di.values():
                stack.append(i)
            elif i in di:
                if not stack or di[i]!=stack.pop():
                    return False
        return not stack
            