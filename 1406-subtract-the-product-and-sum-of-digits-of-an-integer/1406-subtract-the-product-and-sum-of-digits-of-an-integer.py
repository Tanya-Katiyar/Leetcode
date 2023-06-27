class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp=[]
        add=0
        prod=1
        while n>0:
            temp.append(n%10)
            n=n//10
        for i in range(len(temp)):
            prod=prod*temp[i]
            add=add+temp[i]
        res=prod-add
        return res