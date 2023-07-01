class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        visited=set()
        # n=len(nums)
        for i in nums:
            if(i not in visited):
                visited.add(i)
            else:    
                res.append(i)
                visited.add(i)
        return res