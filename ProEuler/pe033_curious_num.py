'''
Created on Dec 13, 2015

@author: Trader
'''
from math import factorial

def permuteListGen(item_list,num_items):
    len_list = len(item_list)
    permute_len = factorial(len_list)/factorial(len_list-num_items)
    print permute_len 
    
    div_list = []
    this_num = permute_len
    for i in xrange(len_list,len_list-num_items,-1):
        this_num = this_num / i
        div_list.append(this_num)
    print div_list
    
    
    for i in xrange(factorial(len_list)/factorial(len_list-num_items)):
        this_list = item_list[:]
        this_permute = []
        this_index = i
        for j in xrange(num_items):
            #find the position to select
            #select the position
            #reduce the index by div_list[i] * select_position
            #remove the selected from the list
            
            select_position = this_index // div_list[j]
            this_index -= select_position * div_list[j]
            this_permute.append(this_list[select_position])
            del this_list[select_position]
        
        yield this_permute

nums_list = [1,2,3,4,5,6,7,8,9]
for i in list(permuteListGen(nums_list,3)):
    print i

for i in permuteListGen(nums_list,3):
    b_pass = 0
    #4 cases
    if (10*i[0]+i[1])*i[2] == (10*i[0]+i[2])*i[1]:
        print (10*i[0]+i[1],10*i[0]+i[2])
    
    if (10*i[0]+i[1])*i[2] == (10*i[2]+i[0])*i[1]:
        print (10*i[0]+i[1],10*i[2]+i[0])

    if (10*i[0]+i[1])*i[2] == (10*i[1]+i[2])*i[0]:
        print (10*i[0]+i[1],10*i[1]+i[2])

    if (10*i[0]+i[1])*i[2] == (10*i[2]+i[1])*i[0]:
        print (10*i[0]+i[1],10*i[2]+i[1])
    


    
