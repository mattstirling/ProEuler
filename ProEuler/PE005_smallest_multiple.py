'''
Created on Oct 31, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import prime_fact_decomp
import numpy as np

agg_factors = []
agg_counts = []

for i in range(1,20):
    (factors, counts) = np.unique(prime_fact_decomp(i),return_counts=True)
    print (i, factors, counts)
    for j in range(len(factors)):
        try:
            fact_index = agg_factors.index(factors[j])
        except ValueError:
            fact_index = -1
        
        if fact_index == -1:
            agg_factors.append(factors[j])
            agg_counts.append(counts[j])
        else:
            agg_counts[fact_index] = max(agg_counts[fact_index],counts[j])

print (agg_factors)
print (agg_counts)

small_mult = 1
for i in range(len(agg_factors)):
    small_mult = small_mult * (agg_factors[i] ** agg_counts [i])

print small_mult

'''
#test
for i in range (1,20):
    print small_mult%i
'''