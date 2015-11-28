'''
Created on Nov 22, 2015

https://projecteuler.net/problem=21

@author: Trader
'''
from PE003_Largest_Prime_Factor import divisorGen

d_list=[0,1]

for i in range(2,10000+1):
    d_list.append(sum(divisorGen(i))-i)

a_list = []
for i in range(2,10000+1):
    if i not in a_list:
        if i<>d_list[i]:
            if d_list[i] <10001:
                
                
                if d_list[d_list[i]]==i:
                    a_list.append(i)
                    a_list.append(d_list[i])

print a_list
print sum(a_list)
