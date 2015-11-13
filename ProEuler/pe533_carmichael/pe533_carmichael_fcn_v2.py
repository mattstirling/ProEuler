'''
Created on Nov 10, 2015

from:
http://math-it.org/Mathematik/Zahlentheorie/Carmichael.html

@author: Trader
'''
from __future__ import division
from PE003_Largest_Prime_Factor import pfactordecomp
from PE003_Largest_Prime_Factor import primes
import time

#goal 1, create the first 15 carmichael Values

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
 
def lcm(a, b):
    return a * b // gcd(a, b)

def carmichael_1fact(p,a):
    #calc lambda(p**a)
    if p==2 and a>2:
        return p**(a-2)
    else:
        return (p-1)*p**(a-1)

def carmichael_fact(n):
    #calc lambda(p1**a1 ... pn**an)
    pfd = pfactordecomp(n)
    
    if len(pfd) == 1:
        return carmichael_1fact(pfd[0][0],pfd[0][1])
    else:
        lambda_list = []
        for fact in pfd:
            lambda_list.append(carmichael_1fact(fact[0],fact[1]))
        
        mult = lambda_list[0]
        for i in range (1,len(lambda_list)):
            mult = lcm(mult,lambda_list[i])
        
        return mult

total=100

t0 = time.time()
#get all primes first
primes_list = list(primes(total+1))
#print primes_list
t1 = time.time()
print 'have ' + str(total+1) + ' primes: ' + str(t1-t0)

#have one lambda list, shared by all calculations for Lsub
#initialize the list with lambda(p**a) for a=1
#where we need lambda(p**a) for a>1, we will add these values as needed
lambda_list = []
for i in primes_list:
    lambda_list.append([carmichael_1fact(i,1)])
t2 = time.time()
print 'have ' + str(total+1) + ' lambda(p**1) values: ' + str(t2-t1)

Lsub_list = []
for n in range(2,total+1):
    
    #for each calculation of L[n], iterate through all primes and get the value of the power for the greatest divisor
    #ie, max a s.t n%lambda(p**a) = 0
    #multiple together p**a for each max value of a
    Lsub_list_next = 1
    for i in range(len(primes_list)):
        #lambda(p**a) has a value for all p, where a=1
        a=1
        lambda_of_p_a = lambda_list[i][a-1]
        #find max a, s.t. n%lambda(p**a) = 0
        while n%lambda_of_p_a==0:
            #iterate a, p_a
            a+=1
            if len(lambda_list[i])<a:
                #add lambda(p**a) to our reference list, lambda(p**a)  
                lambda_list[i].append(carmichael_1fact(primes_list[i],a))
            lambda_of_p_a = lambda_list[i][a-1]
        
        #max value is (a-1)
        Lsub_list_next = Lsub_list_next * primes_list[i]**(a-1)
        
        if primes_list[i] > n+1:
            break
    
    #done for this value n, iterate 
    Lsub_list.append(Lsub_list_next)
    
    if n%100000==0:
        print 'done ' + str(n) + ', ~' + "{0:.1%}".format(float(n)/float(total)) 
        print max(Lsub_list)
t3 = time.time()
print 'done for total= ' + str(total) + ': ' + str(t3-t2)

print max(Lsub_list) 
print max(Lsub_list)+1
print str(max(Lsub_list))[-9:] 
print str(max(Lsub_list)+1)[-9:]


folder_out = 'C:/Temp/python/out/'
file_out = 'pe533_output1.txt'
file_w = open(folder_out + file_out,'w')
file_w.write('i,Lsub_i'+'\n')
for i in range(len(Lsub_list)):
    file_w.write(str(i)+',')
    file_w.write(str(Lsub_list[i])+'\n')

#print L_list
L_list = [Lsub_list[0]]
for i in range(1, len(Lsub_list)):
    L_list.append(max(Lsub_list[i],L_list[i-1]))


folder_out = 'C:/Temp/python/out/'
file_out = 'pe533_output2.txt'
file_w = open(folder_out + file_out,'w')
file_w.write('i,Lsub_i,L_i'+'\n')
for i in range(len(Lsub_list)):
    file_w.write(str(i)+',')
    file_w.write(str(Lsub_list[i])+',')
    file_w.write(str(L_list[i])+'\n')

print primes_list
print Lsub_list

print 2**4 * 3**2 * 5**1 * 7**1 * 13*1 
