class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        h={}

        for i in range(l):
            if nums[i] in h:
                return True
            h[nums[i]]=0 
        return False