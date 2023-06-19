class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]
        count=0
        for i in range(len(gain)):
            count=count+gain[i]
            res.append(count)
        return max(res)