class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            if s[i]=='0':
                zero=0
                one=0
                while i in range(len(s)) and s[i]=='0':
                    i+=1
                    zero+=1
                while i in range(len(s)) and s[i]=='1':
                    i+=1
                    one+=1
                i-=1
                length=min(zero,one)
                ans=max(ans, 2*length)
        return ans

