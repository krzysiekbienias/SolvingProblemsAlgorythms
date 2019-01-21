import string
class Solution():
#Ex.2
# Longest consecutive character
# You are given a string and the problem here is writing a function that takes this string as the input
# and finds the longes subsequence within the string consisting of single character. The return format over your function
# should be dictionary with the character as the key and lenght as a value
    def longest(self, seq):
        max_count=0
        max_char=''
        prev_char=''
        for ch in seq:
            if prev_char==ch:
                count+=1
            else:
                count=1
            if count>max_count:
                max_count=count
                max_char=ch
            prev_char=ch
        return {max_char:max_count}


#Ex. 16
#Finds the first character that does not repeat anywhere in the input string.

    def find_first_non_repeting(self, str):
        dic = {}
        for ch in str:
            dic[ch] = dic.get(ch, 0) + 1

        for ch in str:

            if dic[ch] == 1:
                return ch


#Ex
# Take a string and return first recurring character in it.
    def first_recuring(self,a_string):
        dic={}
        for ch in a_string:
            if ch in dic:
                return ch
            else:
                dic[ch]=1
        return None




#Ex. 18

#Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
#If the last word does not exist, return 0.
        #:type s: str
        #:rtype: int
        #"""
    def length_of_the_last_word(self, s):
        splited_sentence=s.split() #split sequence of strings into list with seperate strings
        last_word=splited_sentence[-1]
        if (last_word==[]):
            return 0
        else:
            return len(last_word)


# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent
# A mapping of digit to letters is similar like on the telephone buttons. Note that 1 does not map to any letters.
    def letter_combinations_ver1(self,digits):

       digit_map={'1':'','2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
       '  8':['t','u','v'],'9':['w','x','y','z']}
       if digits=='':
           return []
       if digits==1:
           return digit_map[digits]
       else:
           L=[]
           for i in digit_map[digits[0]]:
               for j in Solution.letter_combinations(self,digits[1:]):
                   L.append(i+j)
           return L
# Ex 3
# Given a string, write a function to determine if it is a palidrome

    def is_palidorme(self, a_str):
           a_str = a_str.lower()
           a_str = a_str.translate(string.punctuation)  # to able to handle with sentence
           a_str = a_str.replace(" ", "")
           return a_str == a_str[::-1]
    #another version
    def is_palidromic(self,a_str:str)->bool:
        return all(a_str[i]==a_str[~i] for i in range(len(a_str)//2))

    #Ex 4 Interconverter strings and integers
    #implement an integer to string conversion funtion and a string to integer function. You cannot use library functions
    #  like int in Python

    #The functools module is for higher-order functions: functions that act on or return other functions.
    # In general, any callable object can be treated as a function for the purposes of this module.

    #The ord() method returns an integer representing Unicode code point for the given Unicode character.

    def int_to_string(x:int)->str:
        b_is_negative=False
        if x<0:
            x=-x
            b_is_negative=True
        s=[]
        while True:
            s.append(chr(ord('0')+x%10))
            x//=10
            if x==0:
                break
        return ('-' if b_is_negative else ''+'').join(reversed(s))










#Ex 5
# Given two strings s1 and s2 as input, the task is to merge them alternatively. We take the first charater from the
# first string then second character from
#second string and so on.
    def merge_alternatively(self,s1,s2):
        result=""
        s1_split=list(s1)
        s2_split=list(s2)
        len_s1=len(s1_split)
        len_s2=len(s2_split)
        if(len_s1>=len_s2):
            for i in range(len_s2):
                s1_split.insert(2*i+1,s2_split[i])
            result="".join(s1_split)

        else:
            for i in range(len_s1):
                s2_split.insert(2*i,s1_split[i])
            result="".join(s2_split)
        return result
#Ex 6
# You are given a string representing an attendance record for a student. The record only contains the following three characters:
# 1. 'A' Absent
# 2. 'L' Late
# 3. 'P' Present'
#
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
# You need to return whether the student could be rewarded according to his attendance record.

    def check_record(self,a_string):
        if a_string.find("LLL") != -1:
            return False
        num_ofAs=0
        for i in range(len(a_string)):
            if(a_string[i]=='A'):
                num_ofAs+=1
                if num_ofAs>1:
                   return False
        return True

# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

    def num_jew_in_stones(self,J,S):

        l_jewelery=[S.count(i) for i in J]

        return l_jewelery


if __name__ == "__main__":
    object_solution = Solution()

    longest = object_solution.longest(seq='aabcddbbbea')
    first_repeting=object_solution.first_recuring(a_string='dbcaba')
    b_present_record=object_solution.check_record("PLLAPLLAP")
    i_jew_in_stones=object_solution.num_jew_in_stones(J='aA',S='aAAbbbbbaa')



    print('The end')

