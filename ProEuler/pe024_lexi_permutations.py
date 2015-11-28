'''
Created on Nov 22, 2015

@author: Trader
'''
import math

print math.factorial(10)
print math.factorial(9)

num_total = math.factorial(10)
place = 1000000-1

num_list = range(10)

div_list = []
out_list = []
for i in range(9,0,-1):
    div = place/math.factorial(i)
    print div
    div_list.append([i,math.factorial(i),place/math.factorial(i),place%math.factorial(i)])
    place = place%math.factorial(i)
    out_list.append(num_list[div])
    num_list = [x for x in num_list if x not in out_list]
    print num_list

out_list.append(num_list[0])
    
for i in div_list:
    print i
  

str_out = ''
for i in out_list:
     str_out = str_out + str(i)

print str_out 