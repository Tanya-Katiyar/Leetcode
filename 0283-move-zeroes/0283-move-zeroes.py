class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.insert(n,0)
        