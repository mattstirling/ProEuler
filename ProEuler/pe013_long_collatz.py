'''
Created on Nov 6, 2015

@author: Trader
'''
import operator

max_len = 0

def next_collatz(n):
    if n%2==0:
        return n/2
    else:
        return n*3+1

collatz_len = {1:1}

for j in xrange(1000000,0,-1):
    #num_start = 13
    num= j
    if j%1000==0:
        print j
    count = 0
    for i in range(1000000):
        #print num
        count_left = collatz_len.get(num)
        if not count_left:
            num = next_collatz(num)
            count+=1
        else:
            collatz_len[j]=count+count_left
            break
    
        
#print num_start,count
#print collatz_len
print max(collatz_len.iteritems(), key=operator.itemgetter(1))
