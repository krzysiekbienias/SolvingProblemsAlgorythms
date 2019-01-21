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

        # Ex. 17
        # Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

        def remove_duplicates(self, nums):  # O(n)
            dic = {}
            l = len(nums)
            i = 0
            while (i <= l - 1):
                if (nums[i] in dic):
                    nums.remove(nums[i])
                    l -= 1
                else:
                    dic.setdefault(nums[i], 1)
                    i += 1
            return len(nums)




if __name__=="__main__":
    object_solution=Solution()
    two_sum=object_solution.twoSum(nums=[2,5,5,11],target=10)
    print('The end')