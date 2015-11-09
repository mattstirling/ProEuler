'''
Created on Nov 7, 2015

@author: Trader
'''
from PE007_10001_prime import first_n_primes

#create list of primes
#guess that n**2 - 79*n + 1601 is the biggest prime we need, for n=80
n=80
print n**2 - 79*n + 1601  
primes = first_n_primes(5000)
max_prime = max(primes)
max_iteration = [0,0,0]
print max(primes)

#iterate over -999,999 for a,b
#first use a=-79, b=1601
a=-79
b=1601

for a in range(-999,999+1):
    for b in range(-999,999+1):
        
        if a%10 == 0 and b%1000==0:
            print a,b, max_iteration
                
        for i in range(1000):
            this_num = i**2 + a*i + b
            
            #check if we need more primes
            if this_num > max_prime:
                print 'passed the highest prime: ' + str(this_num) + ' is bigger than ' + str(max_prime)
            
            #iterate until we have a non-prime
            if this_num not in primes:
                
                #compare the length of the list versus the max length
                if i > max_iteration[2]:
                    max_iteration = [a,b,i]
                break
    
print max_iteration
print max_iteration[0]*max_iteration[1]