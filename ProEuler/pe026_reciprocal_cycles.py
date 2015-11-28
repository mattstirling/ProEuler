'''
Created on Nov 22, 2015

@author: Trader
'''
from PE003_Largest_Prime_Factor import factorGen
from PE003_Largest_Prime_Factor import primes


def pfactors_sub1000(n):
    for p in primes(1025):
        while n%p==0:
            yield p
            n=n//p
            if n==1: return
            if p>1000:
                yield n
                return

def pfactors(n):
    for p in primes(n):
        while n%p==0:
            yield p
            n=n//p
            if n==1: return

'''
p_list = list(primes(1000))
print len(p_list)

for i in p_list:
    for i in range(100):
'''     
p_mast_list = primes(1000)
p_list = []
i_list = []
for i in range(2,10000):
    this_list = list(pfactors_sub1000(10**i-1))
    print i, this_list
    for j in this_list:
        print (j,i)
        if j<1000 and j not in p_list:
            #print (j,i)
            p_list.append(j) 
            i_list.append(i)
 
print len(p_list)

print p_list
print i_list
 
 
'''
print 10**3/float(11)
print 10**4/float(37)
print 10**6/float(101)
print 10**7/float(271)
print 10**6/float(7)
print 10**9/float(239)
print 10**9/float(73)
print 10**9/float(79)
print 10**9/float(19)
'''