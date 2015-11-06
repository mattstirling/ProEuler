'''
Created on Nov 5, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import prime_fact_decomp

#didn't finish first time... try again
#i=999, tri_num=499500

for i in range(9,12):
    print i


tri_num = 499500
max_prod = 0
for i in range(999+1,2000):
    prod = 1
    tri_num += i
    pfd = prime_fact_decomp(tri_num)
    for factor in pfd:
        prod = prod * (1+factor[1]) 
    
    if prod > max_prod:
        max_prod = prod
    
    if prod > 500:
        print i, tri_num
        break
    
    if i%100 == 0:
        print '\n'
        print i, tri_num, max_prod
        print pfd
        print prod
