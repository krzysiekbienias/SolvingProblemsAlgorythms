class Solution:


    # Ex. 3
    # Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

    def remove_duplicates(self, li_A:list[int])->int:  # O(n)
        dic = {}
        l = len(li_A)
        i = 0
        while (i <= l - 1):
            if (li_A[i] in dic):
                li_A.remove(li_A[i])
                l -= 1
            else:
                dic.setdefault(li_A[i], 1)
                i += 1
        return len(li_A)




if __name__=="__main__":
    object_solution=Solution()
    two_sum=object_solution.twoSum(nums=[2,5,5,11],target=10)
    print('The end')