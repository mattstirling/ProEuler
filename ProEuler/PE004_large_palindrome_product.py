'''
Created on Oct 31, 2015

@author: Trader
'''
done = 0

import numpy as np

def isPalin(num):
    str_num = str(num)
    num_len =len(str_num)
    for i in range(num_len/2):
        if not str_num[i]==str_num[num_len-1-i]:
            return 0
            break
    return 1

'''
for i in range(999,-1,-1):
    for j in range(900,999):
        if isPalin(i*j):
            print (i,j,i*j)
            done = 1
            break
    
    if done:
        break
'''
#(993, 913, 906609)

max_num = 906609

for i in range(913,999):
    for j in range(913,999):
        if isPalin(i*j):
            print (i,j,i*j)
            if i*j>max_num:
                max_num = i*j
print max_num
print ('done')
