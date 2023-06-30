class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited=set()
        maxlength=0
        for i in range(0,len(nums)):
            if nums[i] not in visited:
                ptr=nums[i]
                length=0
                while(ptr!=nums[i] or length==0):
                    length+=1
                    visited.add(ptr)
                    ptr=nums[ptr]
                maxlength = max(maxlength, length)
        return maxlength


