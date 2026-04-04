class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new=[]
        for x in nums:
            if x not in new:
                new.append(x)
            else:
                return True
        return False
        