'''
Created on Nov 11, 2015

@author: Trader
'''
num=98280

for i in range(1000):
    n = num*i 
    if n>18000000 and n<19000000:
        print n
    
    if n>19000000:
        break