class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr=[0]
        count=1
        if 1 not in nums:
            return 0
        else:
            if len(nums)==1 and nums[0]==1:
                return 1
            else:
                for i in range(len(nums)-1):
                    if nums[i]==1 and nums[i+1]==1:
                        count+=1
                    else:
                        count=1
                    arr.append(count)
        return max(arr)
        
        
        