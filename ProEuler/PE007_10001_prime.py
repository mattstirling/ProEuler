'''
Created on Oct 31, 2015

@author: Trader
'''

prime_flag = 1
primes = [2]
max_prime = max(primes)

for i in range(4000):
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
            #print (m)
            break
            
#print (primes)
print (max_prime)

def first_n_primes(n):
    prime_flag = 1
    primes = [2]
    max_prime = max(primes)
    
    for i in range(n-1):
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
                break
    
    return primes        

print len(first_n_primes(100))