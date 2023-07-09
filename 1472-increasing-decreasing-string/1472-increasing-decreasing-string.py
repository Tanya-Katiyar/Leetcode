class Solution:
    def sortString(self, s: str) -> str:
        result=''
        s=list(s)       
        while s:
            for letter in sorted(set(s)):
                s.remove(letter)
                result += letter
            for letter in sorted(set(s), reverse=True):
                s.remove(letter)
                result += letter
        return result