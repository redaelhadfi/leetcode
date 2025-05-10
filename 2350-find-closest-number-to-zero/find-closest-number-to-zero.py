class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        f=nums[0]
        for item in nums:
            if abs(item) < abs(f) :
                f=item
            elif abs(item)==abs(f):
                f=max(item,f)
        
        return f
        
      
           