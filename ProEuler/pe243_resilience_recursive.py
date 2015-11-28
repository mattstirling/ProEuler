'''
Created on Nov 24, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import primes,factorGen

b_try1 = 0
b_try2 = 1

target = float(15499)/float(94744)
print float(15499)/float(94744)
p_list = list(primes(100))
#print p_list
print ''
print 2*3, 1-float(4-1)/float(2*3-1)
print 2*3*5, (4*5-1) + (2), float(2*3*5 - (4*5-1 + 2)-1)/float(2*3*5-1)
print float(8)/float(29)
print ''

if b_try1:
    this_num = 2*3
    this_divs = 4
    this_p_list =[2,3] 
    
    for i in p_list[2:100]:
        this_p_count = this_num - this_divs
        this_divs = (this_divs * i) + this_p_count 
        this_num = this_num*i
        this_R = float(this_num - this_divs) / float(this_num-1)
        print i,this_p_count,this_divs,this_num,this_R
        if this_R < target:
            break 
    
if b_try2:
    
    this_num = 223092870
    this_divs = 186597510
    last_divs = this_divs
    for i in xrange(2,29):
        this_p_count = 0
        this_divs = (last_divs * i - 1) + this_p_count 
        #this_num = this_num*i
        #this_p_list.append(i)
        this_R = float(this_num*i - this_divs-1) / float(this_num*i-1)
        print i,this_p_count,this_divs,this_num*i,this_R
        if this_R < target:
            break 
    
    this_num = 223092870
    this_divs = 186597510
    last_divs = this_divs
    for i in xrange(29,30):
        this_p_count = this_num - this_divs
        this_divs = (last_divs * i - 1) + this_p_count 
        #this_num = this_num*i
        #this_p_list.append(i)
        this_R = float(this_num*i - this_divs-1) / float(this_num*i-1)
        print i,this_p_count,this_divs,this_num*i,this_R


def totient(x):
    t = x
    for (k,l) in factorGen(x):
        t -= t // k
    return t

def r(x):
    return float(totient(x)) / float(x - 1)

x = 2 * 2 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23

print(x, r(x))


    