'''
Created on Nov 12, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import primes
from PE003_Largest_Prime_Factor import divisorGen
from skimage.viewer.plugins.color_histogram import pct_total_area

p_list = list(primes(100000))

prod =1
#for i in xrange(len(p_list)):
for i in range(5):

    #looking for a fraction less than 15499/94744
    #once we find the fraction, look for the true lowest denom in the range
    prod = prod * p_list[i]
    
    #count the number of primes between i and prod
    #1 is always resilient
    num_r = 1
    for j in p_list[i+1:]:
        if j > prod: break
        num_r+=1
    
    print float(num_r)/float(prod), p_list[i], num_r
    if float(num_r)/float(prod) < float(15499)/float(94744):
        print 'broke small limit'
        break
        
print 'done'
print float(15499)/float(94744)
print 2*3*5*7
print 2*3*5*7*11

'''
for i in xrange(100,1200):
    num_r = i-sum([1 for n in divisorGen(i)])
    pct = float(num_r) / float(i)
    print i, pct
    if float(num_r)/float(i) < float(15499)/float(94744):
        print 'broke small limit'
        break
'''
prod = 2*3*5*7
try_list = [1, 2,3,5,7]
for i in try_list:
    
    prod = prod * i
    
    num_r = 1
    for j in p_list[4:]:
        if j > prod: break
        num_r+=1
    
    print float(num_r)/float(prod), i, num_r
    if float(num_r)/float(prod) < float(15499)/float(94744):
        print 'broke small limit'
        break

print 2*3*5*3
print 2*3*5*7*3

prod = 2*3*5*3
try_list = [1,2,3,4,5,7]
for i in try_list:
    
    prod = prod * i
    
    num_r = 1
    for j in p_list[3:]:
        if j > prod: break
        num_r+=1
    
    print float(num_r)/float(prod), i, num_r
    if float(num_r)/float(prod) < float(15499)/float(94744):
        print 'broke small limit'
        break
print 2*3*5*3
print 2*3*5*3*5
