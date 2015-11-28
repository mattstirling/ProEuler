'''
Created on Nov 12, 2015

@author: Trader
'''
from math import log,floor
from PE003_Largest_Prime_Factor import primes, divisorGen
from PE003_Largest_Prime_Factor import factorGen
from PE003_Largest_Prime_Factor import prime_fact_decomp
from numpy import prod
from audioop import reverse

b_get_pfd_ceil_pow = 1
b_create_combos = 1
b_list_combos = 1
b_run_main = 1

#get R for 2*3*5*7
n = 3*5*7
pfd = prime_fact_decomp(n)
p_list = [a for (a,b) in pfd]
p_list.sort(reverse=True)
print p_list

if b_get_pfd_ceil_pow:
    pfd_ceil_pow = []
    #get min a st p**a > n
    for p in p_list:
        pfd_ceil_pow.append(int(floor(log(n,p))))

if b_create_combos:

    all_combo = []
    len_n_list = [x+1 for x in pfd_ceil_pow]
    num_combo = prod(len_n_list)
    len_n = len(len_n_list)
    base_n_list = []
    
    this_num = num_combo
    for i in range(len_n):
        this_num = this_num / len_n_list[i]
        base_n_list.append(this_num) 

    for i in xrange(num_combo):
        all_combo.append([])
        this_num=i
        for j in range(len_n):
            all_combo[i].append(this_num/base_n_list[j])
            this_num = this_num % base_n_list[j]

if b_list_combos:
    folder_out = 'C:/Temp/python/out/'
    file_out = 'pe243_output.txt'
    file_w = open(folder_out + file_out,'w')
    
    for i in xrange(num_combo):
        file_w.write(str(all_combo[i]) + '\n') 

if b_run_main:
    
    good_list = []
    not_r_count = 0
    for i in xrange(num_combo):
        
        this_num = 1
        for j in range(len_n):
            this_num = this_num * pfd[j][0]**all_combo[i][j]
        
        if this_num < n:
            print all_combo[i],this_num
            not_r_count+=1
            good_list.append(this_num)
            if this_num < 0:
                print pfd
                break
    print n
    print float(n-1-not_r_count)/float(n-1)
    print float(4)/float(11)
    print float(15499)/float(94744)
    print sorted(good_list)
    



