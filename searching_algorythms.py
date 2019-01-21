import pandas as pd
import numpy as np

class SearchingAlgorythm():
    #iterative implementation
    def binary_search(self,target: int,a_list:list[int])->int:
        first = 0
        last = len(a_list) - 1

        while first <= last:
            midpoint = first + (last-first) // 2 # Note that (first + last) // 2 used offen is an error the error that can lead to the overflow
            if a_list[midpoint]<target:
                first=midpoint+1
            elif a_list[midpoint]==target:
                return midpoint
            else:
                last=midpoint-1
        return -1






