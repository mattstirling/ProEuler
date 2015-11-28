'''
Created on Nov 22, 2015

https://projecteuler.net/problem=25

@author: Trader
'''

last_num = 1
last_last_num = 1
for i in xrange(3,1000000):
    num = last_num + last_last_num
    
    #if len(str(num)) > 999:
    if num+1 > 10**(1000-1):
        print i
        break
    
    last_last_num = last_num
    last_num = num
