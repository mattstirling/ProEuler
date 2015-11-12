'''
Created on Oct 31, 2015

@author: Trader
'''
import numpy as np

#number = 600851475143
'''
number = 20
number_unfactored = number

max_loops_i = int(np.floor(np.sqrt(number)))
max_loops_j = max_loops_i
primes = []

for i in range(2, max_loops_i+1):
    for j in range(2, max_loops_j+1):
        if number_unfactored%j ==0:
            primes.append(j)
            number_unfactored = number_unfactored / j  
            max_loops_j = int(np.floor(np.sqrt(number_unfactored)))
            break
primes.append(number_unfactored)

print (primes)    
'''         


def prime_fact_decomp_list(number):
    number_unfactored = number
    max_loops_i = int(np.floor(np.sqrt(number)))
    max_loops_j = max_loops_i
    primes = []
    for i in range(2, number):
        for j in range(2, max_loops_j+1):
            if number_unfactored%j ==0:
                primes.append(j)
                number_unfactored = number_unfactored / j  
                max_loops_j = int(np.floor(np.sqrt(number_unfactored)))
                break
    primes.append(number_unfactored)
    primes.sort()
    return primes   



def prime_fact_decomp(number):
    number_unfactored = number
    max_loops_i = int(np.floor(np.sqrt(number)))
    max_loops_j = max_loops_i
    primes = []
    for i in range(2, number):
        for j in range(2, max_loops_j+1):
            if number_unfactored%j ==0:
                primes.append(j)
                number_unfactored = number_unfactored / j  
                max_loops_j = int(np.floor(np.sqrt(number_unfactored)))
                break
    primes.append(number_unfactored)
    unique, counts = np.unique(np.array(primes), return_counts=True)
    return np.asarray((unique, counts)).T


#print (prime_fact_decomp(99999))
    
def primes(n):
    if n < 2: return
    yield 2
    plist = [2]
    for i in range(3,n+1):
        test = True
        for j in plist:
            if j>n**0.5:
                break
            if i%j==0:
                test = False
                break
        if test:
            plist.append(i)
            yield i

def powers_of_2(n):
    if n < 1: return
    plist = 2
    while plist < n:
        yield plist
        plist = plist * 2
        

def pfactors(n):
    for p in primes(n):
        while n%p==0:
            yield p
            n=n//p
            if n==1: return

def pfactordecomp(n):
    unique, counts = np.unique(np.array(list(pfactors(n))), return_counts=True)
    return np.asarray((unique, counts)).T

from math import ceil, sqrt

def max_pow(n, x):
    if n%x == 0:
        return max_pow(n/x, x)+1
    else:
        return 0

def factorGen(n):
    if n <= 1: return
    prime = next((x for x in xrange(2, int(ceil(sqrt(n))+1)) if n%x == 0), n)
    prime_max_pow = max_pow(n, prime)
    yield (prime,prime_max_pow)
    for p in factorGen(n//prime**prime_max_pow):
        yield p
        
    '''
    number_unfactored = number
    max_loops_i = int(np.floor(np.sqrt(number)))
    max_loops_j = max_loops_i
    primes = []
    for i in range(2, number):
        for j in range(2, max_loops_j+1):
            if number_unfactored%j ==0:
                primes.append(j)
                number_unfactored = number_unfactored / j  
                max_loops_j = int(np.floor(np.sqrt(number_unfactored)))
                break
    primes.append(number_unfactored)
    unique, counts = np.unique(np.array(primes), return_counts=True)
    '''

def divisorGen(n):
    factors = list(factorGen(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in xrange(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


#print sum(factorGen(1000000))
#print sum(divisorGen(100))
#print factorGen(100)
#print divisorGen(100)
#print prime_fact_decomp_list(100)

#for i in list(divisorGen(2)):
#    print i

#for i in powers_of_2(100):
#    print i

#print pfactordecomp(76576500)
#print 3*3*4*2*2*2*2
#print pfactordecomp(48)

