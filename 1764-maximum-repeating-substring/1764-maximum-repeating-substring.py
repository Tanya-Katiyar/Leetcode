class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n=len(sequence)
        ans=0
        k=1
        if(n<len(word)):
            return 0
        while(word*k in sequence):
            ans+=1
            k+=1
        return ans


        