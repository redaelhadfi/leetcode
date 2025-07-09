class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        l=len(nums)
        left=[]
        right=[]
        resu=[]
        if l==2:
            return [nums[1],nums[0]]
        left.append(nums[0])
        r=nums[0]
        for i in range(1,l):
            
            left.append(r*nums[i])
            r=left[i]
        print(left)


        r=nums[l-1]
        right.insert(0,nums[l-1])
        for i in range(1,l):
            right.insert(0, r*nums[l-i-1])
            r=right[0]
        print(right)
        
        for i in range(l):
           if i==0:
              resu.append(right[1])
           elif i==l-1:
              resu.append(left[i-1])
           else:
               resu.append(left[i-1]*right[i+1])
        return resu