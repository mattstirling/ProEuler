'''
Created on Nov 22, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import divisorGen

a_list = []
#for i in range(11,28123+1):
for i in range(11,28123+1):
    if 2*i < sum(divisorGen(i)):
        a_list.append(i)
print 'done abundant list'
print len(a_list)
print max(a_list)

sum_list = []
for i in xrange(len(a_list)):
    for j in xrange(i, len(a_list)):
        if not i+j in sum_list: 
            sum_list.append(i+j)
print 'done the sum list'
print len(sum_list)

not_sum_list = []
for i in range(28123):
    if not i in sum_list:
        not_sum_list.append(i)

print sum(not_sum_list)