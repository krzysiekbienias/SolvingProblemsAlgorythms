class Solution():
# Ex 1
# Pascal triangle.
    def generate_pascal_triangle(self, rows_num):
        if (rows_num == 0):
            return []
        else:
            result = [[1]]
            for i in range(1, rows_num):
                result.append([0] * (i + 1))
                for k in range(i + 1):
                    if k == 0 or k == i:
                        result[i][k] = 1
                    else:
                        result[i][k] = result[i - 1][k - 1] + result[i - 1][k]
                        y=sum([2,3])
            return result


#Ex. 11
#Calculate the sum of two integers but you are not allowed to use operator + and -
    def get_sum_using_list(self,a,b):
        result=[a,b]
        return sum(result)

    def get_sum_using(self,a,b):
        return a.__add__(b)

#Ex.
#For a given array find all subsets of the set.
    def all_subsets(self,a_list):
        if len(a_list)==0:
           return [[]]
        else:
            subsets=self.all_subsets(a_list[1:])
            return subsets+[[a_list[0]]+x for x in subsets]


    def subsets_of_k_elements(self,a_list,k):
        all_sub=self.all_subsets(a_list)

        new_list=[]

        for x in range(len(all_sub)):
            if (len(all_sub[x])==k):
                temp=all_sub[x]
                new_list.append(temp)
        return new_list

# Ex 19
    # Given an integer x, find square root of it. If x is not a perfect square, then return floor(√x).
    # Algorithm:
    # 1) Start with 'start' = 0, end = 'x',
    # 2) Do following while 'start' is smaller than or equal to 'end'.
         # a) Compute 'mid' as (start + end)/2
         # b) compare mid*mid with x.
         # c) If x is equal mid*mid, return mid
         # d) If x is greater do binary search between mid+1 and end
         # e) If x is smaller, do binary search between start and mid-1 GfG

    def sqrt_by_binary_search(self,x):
        if (x==0 or x==1):
            return x
        start=1
        end=x
        while(start<=end):
            mid=(start+end)//2
            if (mid*mid==x): #case for perfect square
                return mid
            if(mid*mid<x):
                start=mid+1
                result=mid
            else:
                end=mid-1
        return result

# Ex (Missing numbers)
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

    def missing_number(self,nums):#mu solution submitted
        sum_given=sum(nums)
        all_numbers=range(0,len(nums)+1)
        sn=sum(all_numbers)
        missing_num=sn-sum_given
        return missing_num


    def missingNumber_lc_solution(self, nums):#lc_solution =solution from leetcode
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if nums[i] != expected_num:
                return expected_num

    def missing_number_gauss_approach(self,nums):
        expected_sum=len(nums)*(len(nums)+1)/2
        actual_sum=sum(nums)
        return expected_sum-actual_sum

    def count_primes(self,n):
        primes=[1,2,3,4,5,6,7,8,9,10]
        x=primes[3:10:2]
        primes[3:10:2]=[0]*len(primes[3:10:2])
        return

#Ex
#The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the
# set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

    def find_duplicated_number(self,nums):#TODO it doesn't work for [1,1],[2,2]

        s_n=sum(nums)
        remove_duplicated=set(nums)
        duplicated_number=s_n-sum(remove_duplicated)
        i=nums[0]
        normal_sequence=[i for i in range(nums[0],nums[-1]+1)] #sequence
        missing_num=sum(normal_sequence)-sum(remove_duplicated)
        return [duplicated_number,missing_num]





if __name__ == "__main__":

    o_solution=Solution()
    sqrt_binary=o_solution.sqrt_by_binary_search(x=7)
    i_missing_numb=o_solution.missing_number(nums=[9,6,4,2,3,5,7,0,1])
    erastosthenes=o_solution.count_primes(10)
    set_mismatch=o_solution.find_duplicated_number(nums=[2,2])

    print('The End')