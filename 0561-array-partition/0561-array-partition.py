class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s=0
        nums.sort()
        for i in range(0,len(nums),2):
            s+=min(nums[i],nums[i+1])
        return s

