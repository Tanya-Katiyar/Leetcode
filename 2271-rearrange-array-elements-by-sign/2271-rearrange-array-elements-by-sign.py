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
        m=len(nums)//2
        for j in range(m):
            ans.append(pos[j])
            ans.append(neg[j])
        return ans       