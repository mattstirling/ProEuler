'''
Created on Oct 31, 2015

@author: Trader
'''
import numpy as np

#number = 600851475143
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


print (prime_fact_decomp(99999))
    
def primes(n):
    if n < 2: return
    yield 2
    plist = [2]
    for i in range(3,n):
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

def pfactors(n):
    for p in primes(n):
        while n%p==0:
            yield p
            n=n//p
            if n==1: return

def pfactordecomp(n):
    unique, counts = np.unique(np.array(list(pfactors(n))), return_counts=True)
    return np.asarray((unique, counts)).T

print pfactordecomp(76576500)
print 3*3*4*2*2*2*2
