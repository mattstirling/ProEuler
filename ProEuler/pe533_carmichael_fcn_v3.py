'''
Created on Nov 10, 2015

from:
http://math-it.org/Mathematik/Zahlentheorie/Carmichael.html

@author: Trader
'''
from __future__ import division
from PE003_Largest_Prime_Factor import divisorGen, powers_of_2
from PE003_Largest_Prime_Factor import pfactordecomp
from PE003_Largest_Prime_Factor import primes
from PE003_Largest_Prime_Factor import max_pow
import time
import math
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

total=20000000

t0 = time.time()
#get all primes first
#primes_list = list(primes(total+1))
t1 = time.time()
#print 'have sub-' + str(total+1) + ' primes: ' + str(t1-t0)
#print primes_list

powers_of_2_list = list(powers_of_2(total))
print len(powers_of_2_list)
t2 = time.time()
print 'have sub-' + str(total+1) + ' powers of 2: ' + str(t2-t1)

#have one lambda list, shared by all calculations for Lsub
#initialize the list with lambda(p**a) for a=1
#where we need lambda(p**a) for a>1, we will add these values as needed
#lambda_list = []
#for i in primes_list:
    #lambda_list.append([carmichael_1fact(i,1)])
    #lambda_list.append(carmichael_1fact(i,1))
t3 = time.time()
print 'have ' + str(total+1) + ' lambda(p**1) values: ' + str(t3-t2)
#print lambda_list
t5 =t3
#begin Lsub_list at 0 
Lsub_list = [0,2,24,2]
Lsub_pfd = [[],[(2,1)],[(2,3),(3,1)],[(2,1)]]
for n in range(4,total+1):
    #for each calculation of L_sub[n], iterate through all divisors of n
    #for each divisor, get the prime factor decomposition (pfd) st. L_sub[divisor] = p1**a1 * .. * pn**an
    #for each prime, p get the max value a, s.t. a = max(a_divisor1, ..., a_divisor_n)
    #if n+1 is prime, then include (n+1)**1 in the pdf for L_sub[n]
    
    #if not prime, attach (2,1) ... this saves us from using an "if statement" as we iterate below
    Lsub_pfd.append([(2,1)])
    #if (n+1) in primes_list:
    if sum(1 for div in divisorGen(n+1)):
        #first look if n+1 is prime, if yes add 
        Lsub_pfd[n].append((n+1,1)) 
    
    if n in powers_of_2_list:
        #also check if this new value is a power of 2
        Lsub_pfd[n].append((2,2+int(math.log(n,2))))
    #print Lsub_pfd
    
    divisors = list(divisorGen(n))
    
    #aggregate the prime fact decomps of the max_pfd for each divisor
    #merge like primes by keeping the max value for a
    p_list = []
    a_list = []
    for i in divisors:
        for p_a in Lsub_pfd[i]:
            if p_a[0] in p_list:
                p_list_id = p_list.index(p_a[0]) 
                a_list[p_list_id] = max(a_list[p_list_id],p_a[1])
            else:
                p_list.append(p_a[0]) 
                a_list.append(p_a[1])
    #print p_list
    #print a_list
    
    #check if any primes further divide n
    #also we calc Lsub[n] by iteratively multiplying by p**a as we determine the max power for a
    Lsub_list_next = 1
    for i in xrange(len(p_list)):
        #we know p**a divides n
        #check if p**(a+1) divides n
        #or just find b s.t. p**b divides (n/ p**a), so then max power is a+b
        if not p_list[i]==2:
            #p=2 has a different formula
            a_list[i] = max_pow( n / carmichael_1fact(p_list[i],a_list[i]) ,p_list[i]) + a_list[i]
        
        Lsub_list_next = Lsub_list_next * p_list[i]**a_list[i]
    Lsub_list.append(Lsub_list_next)
    
    #save the max_pfd
    Lsub_pfd[n]=[]
    for i in xrange(len(p_list)):
        Lsub_pfd[n].append((p_list[i],a_list[i]))
    
    if n%10000==0:
        print '\n' + 'done ' + str(n) + ', ~' + "{0:.1%}".format(float(n)/float(total)) 
        print len(str(max(Lsub_list)))
        
        last_time = t5
        t5 = time.time()
        print t5-t3
        print t5-last_time
         
t4 = time.time()
print 'iterating for total= ' + str(total) + ': ' + str(t4-t3)
print 'total run for total= ' + str(total) + ': ' + str(t4-t0)

#print Lsub_list
#print Lsub_pfd
    
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

#print primes_list
#print Lsub_list
#print 2**4 * 3**2 * 5**1 * 7**1 * 13*1 
