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
    primes.sort()
    return primes   

print (prime_fact_decomp(8))
    
