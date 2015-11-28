'''
Created on Nov 22, 2015

@author: Trader
'''

from math import factorial

def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n / 10
    return r

def fact_sum_digits(n):
    #calculated [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880] manually
    r = 0
    while n:
        r, n = r + [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880][n % 10], n / 10
    return r

b_test_max_num = 0
b_get_fact_nums = 0
b_run_main = 1
b_debug = 0
#print len(str(10**6))

if b_test_max_num:
    #this taught me that 7-digit numbers cannot pass this test
    for i in range(0,20):
        #assume least number is 1000000
        this_ave = 10**i / (i+1)
        print i+1, this_ave, 10**i  
        if this_ave > 362880:
            break

if b_get_fact_nums:
    fact_list = []
    for i in range(9+1):
        fact_list.append(factorial(i))
    print fact_list
    
if b_run_main:    
    
    good_list = []
    #test all numbers that are less than 8 digits
    #exclude 1,2 per instructions
    for i in xrange(10,10**7):
        if i==fact_sum_digits(i):
            good_list.append(i)
    
    print good_list
    print sum(good_list)        
    
    if b_debug:
        for i in good_list:
            str_num = str(i)
            for j in str_num:
                print i, j, fact_list[int(j)]

print 'done'
    
    