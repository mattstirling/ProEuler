'''
Created on Nov 22, 2015

https://projecteuler.net/problem=20

Find the sum of the digits in the number 100!

@author: Trader
'''
fact_100 = 1

for i in range(1,100+1):
    fact_100 = fact_100 * i

str_fact_100 = str(fact_100)
sum = 0

for i in str_fact_100:
    sum+=int(i)

print sum
    

