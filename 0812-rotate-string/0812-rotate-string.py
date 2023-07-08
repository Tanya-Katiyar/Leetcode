class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        res=s
        n=len(s)
        if len(s)!=len(goal):
            return False
        else:
            for i in range(n):
                res=res[1:n+1]+res[0]
                print(res)
                if res==goal:
                    return True