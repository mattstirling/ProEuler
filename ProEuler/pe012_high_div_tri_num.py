'''
Created on Nov 5, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import pfactordecomp

#didn't finish first time... try again
#i=999, tri_num=499500
#i=1900 1805950 
#2900 4206450
#5000 12502500

tri_num = 49009950
max_prod = 0
for i in range(9900+1,20000):
    prod = 1
    tri_num += i
    pfd = pfactordecomp(tri_num)
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
