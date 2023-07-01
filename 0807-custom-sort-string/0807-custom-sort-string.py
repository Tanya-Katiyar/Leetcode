class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s1=Counter(s)
        o1=Counter(order)
        res=''
        for i in order:
            # o.append(i)
            if i in s1:
                res+=i*s1[i]
        for ss in s:
            if ss not in o1:
                res+=ss
        return res
