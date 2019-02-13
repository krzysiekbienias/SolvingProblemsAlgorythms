from typing import List

class Solution:
    # Ex.1
    # Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    # You may assume that each input would have exactly one solution, and you may not use the same element twice.
    def twoSum(self,li_x: List[int],i_target:int )->List[int]:

        for i in range(0,len(li_x)):
            for j in range(i+1,len(li_x)):
                temp_sum=li_x[i]+li_x[j]
                if (temp_sum==i_target):
                    return [i,j]

    #Ex. 2
    #Write a program that takes as input a sorted array and a given target value and determines if there are two entries in the array
    #(not necessarily distinct) that add up tp that value

    def has_two_sum(self,li_A:List[int],i_target:int)->bool:
        i:int=0
        j:int=len(li_A)-1
        while i<=j:
            if li_A[i]+li_A[j]==i_target:
                return True
            elif li_A[i]+li_A[j]<t:
                i+=1
            else:
                j-=1
        return False

    #Ex. 3
    #Compute the maximum water trapped by pair of verical lines
    def get_max_trapped_water(self,heights:List[int])->int:
        i=0
        j=len(heights)-1
        max_watter=0
        while i<j:
            width=j-i
            max_watter=max(max_watter,width*min(heights[i],heights[j]))
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return max_watter

if __name__=="__main__":
    o_solution=Solution()
    two_sum=o_solution.twoSum(li_x=[2,5,5,11],i_target=10)
    print('The end')