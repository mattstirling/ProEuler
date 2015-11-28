'''
Created on Nov 23, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import prime_fact_decomp
str_list = []
list_upper = 100

for i in range(2,list_upper+1):
    pfd = prime_fact_decomp(i)
    
    for j in range(2,list_upper+1):
        
        str_pfd = ''
        for k in pfd:
            str_pfd += str(k[0])+'^'+str(j*k[1])+'_'
        str_list.append(str_pfd)

#for i in str_list:
    #print i

unique_list = list(set(str_list))

print len(str_list)
print len(unique_list)