'''
Created on Nov 12, 2015

@author: Trader
'''
from math import log,floor
from PE003_Largest_Prime_Factor import primes, divisorGen
from PE003_Largest_Prime_Factor import factorGen
from PE003_Largest_Prime_Factor import prime_fact_decomp
from numpy import prod

def comboListGen(chose_n_list):
    len_n_list = [x+1 for x in pfd_ceil_pow]
    num_combo = prod(len_n_list)
    len_n = len(len_n_list)
    base_n_list = []
    
    this_num = num_combo
    for i in xrange(len_n):
        this_num = this_num / len_n_list[i]
        base_n_list.append(this_num) 
    
    for i in xrange(num_combo):
        combo = []
        this_num=i
        for j in range(len_n):
            combo.append(this_num/base_n_list[j])
            this_num = this_num % base_n_list[j]
        yield combo

b_get_pfd_ceil_pow = 1
b_create_combos = 1
b_list_combos = 0
b_run_main = 0

#get R for 2*3*5*7
n = 2*3*5*7


pfd = prime_fact_decomp(n)
pfd_list = [a for (a,b) in pfd]
p_list = [x for x in primes(n) if x not in pfd_list]
p_list.sort(reverse=True)
print len(p_list)

if b_get_pfd_ceil_pow:
    pfd_ceil_pow = []
    #get min a st p**a > n
    for p in p_list:
        pfd_ceil_pow.append(int(floor(log(n,p))))
#print len(pfd_ceil_pow)

if b_create_combos:

    all_combo = []
    len_n_list = [x+1 for x in pfd_ceil_pow]
    
    this_num = 1
    for i in len_n_list:
        this_num = this_num * i 
    num_combo = this_num
    print num_combo
    
    len_n = len(len_n_list)
    base_n_list = []
    
    this_num = num_combo
    for i in range(len_n):
        this_num = this_num / len_n_list[i]
        base_n_list.append(this_num) 
    
    r_count = 0
    i=0
    for m in xrange(num_combo):
        
        if not i < num_combo:
            break
        
        #create the combo
        combo=[]
        this_num=i
        for j in range(len_n):
            combo.append(this_num/base_n_list[j])
            this_num = this_num % base_n_list[j]
        
        #check the number for this combo
        this_num = 1
        for j in range(len_n):
            this_num = this_num * p_list[j]**combo[j]
        
        print this_num, combo
        if this_num < n:
            #print i, this_num, p_list, combo 
            r_count+=1
            i+=1
        else:
            
            #print i, this_num, p_list, combo, -99 
            for j in range(len_n-1,-1,-1):
                #print i, j, combo[j], combo[0], base_n_list[0], combo[1], base_n_list[1]
                if not combo[j]==0:
                    
                    #jump i up - don't check higher multiples of this failed number
                    i_jump = 0
                    for k in range(j):
                        i_jump = i_jump + combo[k] * base_n_list[k]
                    i_jump = i_jump + base_n_list[j-1]
                    i = i_jump
                    #print i
                    break
    #
    #r_count -= 1
            
    print r_count, n
    print n
    print float(r_count)/float(n-1)
    print float(4)/float(11)
    print float(15499)/float(94744)
    #print sorted(good_list)
        
        
        
if b_list_combos:
    folder_out = 'C:/Temp/python/out/'
    file_out = 'pe243_output.txt'
    file_w = open(folder_out + file_out,'w')
    
    for i in xrange(num_combo):
        file_w.write(str(all_combo[i]) + '\n') 

if b_run_main:
    
    print n
    print float(n-1-r_count)/float(n-1)
    print float(4)/float(11)
    print float(15499)/float(94744)
    #print sorted(good_list)
    



