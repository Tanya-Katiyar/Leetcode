class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            c=i*i
            res.append(c)
        res.sort()
        return res