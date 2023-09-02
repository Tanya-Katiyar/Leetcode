class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        neg=[]
        pos=[]
        ans=[]
        for i in range(n):
            if(nums[i]<0):
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for j in range(len(pos)):
            ans.append(pos[j])
            ans.append(neg[j])
        return ans       