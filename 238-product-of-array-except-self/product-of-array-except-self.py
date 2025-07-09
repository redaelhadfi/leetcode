class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)
        resu = [1] * n
       
        prefix_product = 1
        for i in range(n):
            resu[i] = prefix_product
            prefix_product *= nums[i]
            

        suffix_product = 1
        for i in range(n - 1, -1, -1):
            resu[i] *= suffix_product
            suffix_product *= nums[i]
        return resu