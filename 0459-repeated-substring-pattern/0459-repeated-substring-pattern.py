class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        rep=''
        for i in range(n//2):
            rep=rep+s[i]
            if(n%len(rep))==0:
                if(rep * (n//len(rep))==s):
                    return True
        return False
            
