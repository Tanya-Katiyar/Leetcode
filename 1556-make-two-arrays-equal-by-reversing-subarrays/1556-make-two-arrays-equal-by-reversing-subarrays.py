class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr.sort(reverse=True)
        target.sort(reverse=True)
        if target==arr:
            return True
        return False