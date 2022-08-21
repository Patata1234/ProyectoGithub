mport math
import os
import random
import re
import sys

def miniMaxSum(arr):
    a = sorted(arr)
    print (sum(a[:-1]), sum(a[1:]))
        
if _name_ == '_main_':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
