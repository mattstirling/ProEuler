'''
Created on Nov 7, 2015

@author: Trader
'''

print 2**1000

str_num = str(2**1000)
n_sum = 0
for i in str_num:
    n_sum += int(i)

print n_sum