class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # not optimised
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]==0:
        #         nums.remove(nums[i])
        #         nums.insert(n,0)
        
        #optimised
        idx=0
        for num in nums:
            if num!=0:
                nums[idx]=num
                idx+=1
        while idx<len(nums):
            nums[idx]=0
            idx+=1