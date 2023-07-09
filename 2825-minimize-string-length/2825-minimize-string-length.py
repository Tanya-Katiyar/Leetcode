class Solution:
    def minimizedStringLength(self, s: str) -> int:
        rep=[]
        for i in range(len(s)):
            if s[i] not in rep:
                rep.append(s[i])
        return len(rep)