'''
Created on Nov 12, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import primes, divisorGen
from PE003_Largest_Prime_Factor import factorGen
from skimage.viewer.plugins.color_histogram import pct_total_area
from numpy import prod

all_p_list = list(primes(10000))

n_list = range(30,500)
n_list = [2*3*5*7*11*13*17,2*3*5*7*11*13*17*19,2*3*5*7*11*13*17*19*23, 2*3*5*7*11*13*17*19*23*29,2*3*5*7*11*13*17*19*23*29*31]

'''
n_list_mult = [2,3,5,7,11,13]
n_list_mult = [1]
for i in n_list_mult:
    n_list.append(i*2*3*5*7*11*13)
'''
 
#for i in xrange(len(p_list)):
for n in n_list:
    #looking for a fraction less than 15499/94744
    #once we find the fraction, look for the true lowest denom in the range
    all_p_list = list(primes(n))
    
    #get divisors for prod
    div_list = [a for (a,b) in factorGen(n)]
    #print div_list
    
    #create list of resilient fractions based on primes (to the power of 1 only):
    #does not include divisors of n
    #must be less than n
    p_list = []
    for p in all_p_list:
        if p >= n: break  
        if not p in div_list:
            p_list.append(p)
    
    all_list=[]
    new_list = p_list
    while len(new_list)>0:
        last_list = new_list
        new_list = []
        for j in last_list:
            if j*p_list[0]>n: break   
            #num_r+=1
            #print i,num_r,j,1
            for k in p_list:
                if k*j > n: break
                if k*j not in all_list: 
                    all_list.append(k*j)
                    new_list.append(k*j)
                    #num_r+=1
                    #print i,num_r,j,k
    
    #count the number of primes (and combinations of primes) less than n
    #1 is always resilient
    #primes are resilient
    #multiples of primes (no sharing divisors with n) are resilient
    num_r = 1
    num_r += len(p_list)
    num_r += len(all_list)
    print p_list
    print all_list
    
    print n, num_r, float(num_r)/float(n)
    if float(num_r)/float(n) < float(15499)/float(94744):
        print 'broke small limit'
        print list(factorGen(n))
        break
        
print 'done'
print float(15499)/float(94744)
print list(factorGen(150150))
print 11**3
