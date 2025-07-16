class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l=len(nums)
      
        ma=s=nums[0]
       
        for i in range(1,l):

            s=max(nums[i],s+nums[i])               
           
            ma=max(s,ma)   
        return ma



        