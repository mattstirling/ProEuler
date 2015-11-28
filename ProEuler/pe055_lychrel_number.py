'''
Created on Nov 23, 2015

@author: Trader
'''

b_run_main = 1

def reverse_num1(n):
    r = 0
    while n:
        r, n = r*10 + n % 10, n / 10
    return r

def reverse_num(n):
    return int(str(n)[::-1]) 
    
good_list = []
if b_run_main:
    for i in xrange(10,10000):
        this_num = i
        this_reverse_num = reverse_num(this_num)
        b_is_lyrchrel = True
        
        for j in xrange(50):
            this_num = this_num + this_reverse_num
            
            str_this_num = str(this_num)
            str_this_reverse_num = str_this_num[::-1]
            
            #check if palindrome
            if str_this_num == str_this_reverse_num:
                b_is_lyrchrel = False
                break
                   
            this_reverse_num = int(str_this_reverse_num)
        
        if b_is_lyrchrel:
            good_list.append(i)
            
    print good_list[:10]
    print len(good_list)