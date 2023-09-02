class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadanes algorithm
        res=nums[0]
        sum=0
        for i in nums:
            sum=sum+i
            res=max(res,sum)
            if sum<0:
                sum=0
        return res 