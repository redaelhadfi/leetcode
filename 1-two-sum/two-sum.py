class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(nums)):
            y=target-nums[i]
            if y in dic:
                return [dic[y],i]
            else :
              dic[nums[i]]=i