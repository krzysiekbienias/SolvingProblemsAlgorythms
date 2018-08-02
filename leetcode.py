class Solution:
# Ex.1
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
    def twoSum(self,nums,target):
        """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                temp_sum=nums[i]+nums[j]
                if (temp_sum==target):
                    return [i,j]

    def myPower(self,x,n):
        """
                :type x: float
                :type n: int
                :rtype: float
                """


object_solution=Solution()

two_sum=object_solution.twoSum(nums=[2,5,5,11],target=10)