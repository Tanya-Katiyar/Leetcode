class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res=[nums[0]]
        for i in range(1,len(nums)):
            if(nums[i-1]<nums[i]):
                res[-1]=res[-1]+nums[i]
            else:
                res.append(nums[i])
        return max(res)
