'''
Created on Oct 31, 2015

@author: Trader
'''

for i in range(1,1000):
    for j in range(1,1000):
        if i+j>1000:
            break
        
        k = 1000 - i - j
        
        if k**2 - i**2 - j**2 == 0:
            print (i,j,k,i*j*k)