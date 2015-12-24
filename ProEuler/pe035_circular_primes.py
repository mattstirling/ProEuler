'''
Created on Dec 13, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import primes
from numpy  import log10

def allDigitsOdd(n):
    str_num = str(n)
    for i in str_num:
        if int(i)%2 == 0:
            return False
    return True

def circleList(n):
    if n<10:
        return [n]
    
    circ_list = []
    circ_list.append(n)
    
    #len_num is actually 1 less than the length
    len_num = int(log10(n)//1)
    this_num = n
    for i in xrange(len_num):
        this_num = 10*(this_num%(10**len_num)) + (this_num//(10**len_num))
        circ_list.append(this_num)
    
    return circ_list
    
#total = 1000000
total = 1000000

#get all primes first
primes_list = []
for i in primes(total):
    if allDigitsOdd(i):
        primes_list.append(i)


count_circ = 0
for i in primes_list:
    b_all_circ_prime = 1
    for j in circleList(i):
        if not j in primes_list:
            b_all_circ_prime = 0
            break
    
    if  b_all_circ_prime:
        count_circ +=1

#we've excluded 2, so add that back
print count_circ + 1