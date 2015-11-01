'''
Created on Oct 31, 2015

@author: Trader
'''
#import numpy as np

sum_squares = 0
sum_num = 0
list_num = []

for i in range(1,101):
    list_num.append(i)
    sum_num += i 
    sum_squares += i**2 
    
diff = sum_num**2 - sum_squares

print sum_num
print sum_num**2
print sum_squares
print diff

print list_num

