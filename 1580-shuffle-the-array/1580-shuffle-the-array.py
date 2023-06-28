class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        b=[]
        res=[]
        for i in range(n):
            a.append(nums[i])
        for i in range(n, 2*n):         
            b.append(nums[i])  
        for i in range(n):
            res.append(a[i])
            res.append(b[i])
        return res