'''
Created on Nov 29, 2015

1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).

How many different ways can P2 be made using any number of coins?

@author: Trader
'''
from numpy import prod

def comboListGen(chose_n_list):
    len_n_list = [x+1 for x in chose_n_list]
    num_combo = prod(len_n_list)
    len_n = len(len_n_list)
    base_n_list = []
    
    this_num = num_combo
    for i in xrange(len_n):
        this_num = this_num / len_n_list[i]
        base_n_list.append(this_num) 
    
    for i in xrange(num_combo):
        combo = []
        this_num=i
        for j in range(len_n):
            combo.append(this_num/base_n_list[j])
            this_num = this_num % base_n_list[j]
        yield combo

#consider all combinations of 'non-pennies'
#if the sum is less than 200, then it is a success

coin_amt = [2,5,10,20,50,100,200]
max_coin_num = []
for n in coin_amt:
    max_coin_num.append(200//n)

num_cases = 0
for combo in comboListGen(max_coin_num):
    this_sum = 0
    for i in xrange(len(coin_amt)):
        this_sum += coin_amt[i]*combo[i]
    
    if this_sum <= 200:
        num_cases += 1

print num_cases
    
    