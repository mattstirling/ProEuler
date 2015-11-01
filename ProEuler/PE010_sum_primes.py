'''
Created on Nov 1, 2015

@author: Trader
'''

prime_flag = 1
primes = [2]
max_prime = max(primes)
primes_sum = 2

for i in range(1000000):
    for m in range(max_prime,max_prime*2):
        prime_flag = 1
        for j in range(len(primes)):
            if m%primes[j]==0:
                prime_flag = 0
                break
        
        #if we found a new prime, append and iterate
        if prime_flag:
            primes.append(m)
            max_prime = m
            primes_sum += m
            print m
            break
    
    if max_prime >2000000:
        primes_sum -= max_prime
        break     
            
#print (primes)
print (max_prime)
print primes_sum