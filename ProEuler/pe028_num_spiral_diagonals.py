'''
Created on Nov 23, 2015

@author: Trader
'''

#notice the pattern +2 *4, +4 *4, +6 *4, etc
diag_size=1001
incr_size = 2

#initialize last_num and the sum
diag_sum = 1
this_num = 1

#need (diag_size-1) * 2 in total
for i in xrange(diag_size):
    
    for j in xrange(4):
        this_num = this_num + incr_size
        #print this_num
        diag_sum += this_num
        
    incr_size += 2
    if incr_size > diag_size:
        break

print diag_sum