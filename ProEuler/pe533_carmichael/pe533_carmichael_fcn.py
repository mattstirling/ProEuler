'''
Created on Nov 10, 2015

from:
http://math-it.org/Mathematik/Zahlentheorie/Carmichael.html

@author: Trader
'''
from PE003_Largest_Prime_Factor import pfactordecomp
from PE003_Largest_Prime_Factor import primes

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

total=8
Lsub_list = []
for n in range(2,total+1):
    primes_list = list(primes(n+1))
    #print primes_list
    
    lambda_list = []
    for i in range(len(primes_list)):
        #add lambda(p**a) for n%lambda(p**a) = 0 
        a=1
        lambda_list.append([carmichael_fact(primes_list[i]**a)])
        while n%lambda_list[i][a-1]==0:
            a+=1
            lambda_list[i].append(carmichael_fact(primes_list[i]**a))
    #print lambda_list
    
    Lsub_list_next = 1
    for i in range(len(primes_list)):
        lam_len = len(lambda_list[i])
        #print i, primes_list[i],lam_len, lambda_list[i] 
        if lam_len>1:
            Lsub_list_next = Lsub_list_next * primes_list[i]**(lam_len-1)
    Lsub_list.append(Lsub_list_next)
    
    if n%10000==0:
        print 'done ' + str(n) + ', ~' + n/total 
        print max(Lsub_list)
         
#print Lsub_list
L_list = [Lsub_list[0]]
for i in range(1, len(Lsub_list)):
    L_list.append(max(Lsub_list[i],L_list[i-1]))
print Lsub_list
print L_list
print max(L_list)


