class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(0,len(arr)):
            for j in range(i,len(arr),2):
                s=s+sum(arr[i:j+1])
        return s
