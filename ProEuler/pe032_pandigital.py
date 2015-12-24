'''
Created on Dec 12, 2015

_ _ _ _ _ _ _ _ _  _  _ 
1 2 3 4 5 6 7 8 9 10 11

@author: Trader
'''
from PE003_Largest_Prime_Factor import divisorGen
from math import factorial 

def no_duplicated_numbers(n):
    str_num  =str(n)
    this_num_list = []
    for j in str_num:
        if j in this_num_list:
            return False
        this_num_list.append(j)
    return True        

def no_zero_or_nine_numbers(n):
    str_num  =str(n)
    for j in str_num:
        if j =='0' or j=='9':
            return False
    return True   

        
def permuteListGen(num_list):
    len_list = len(num_list)
    div_list = []
    for i in xrange(len_list-1,0,-1):
        div_list.append(factorial(i))
    #print div_list
    
    
    for i in xrange(factorial(len_list)):
        this_list = num_list[:]
        this_permute = []
        this_index = i
        for j in xrange(len_list-1):
            #find the position to select
            #select the position
            #reduce the index by div_list[i] * select_position
            #remove the selected from the list
            
            select_position = this_index // div_list[j]
            this_index -= select_position * div_list[j]
            this_permute.append(this_list[select_position])
            del this_list[select_position]
            
        this_permute.append(this_list[0])
        yield this_permute

def chose_9_2():
    this_list = []
    for i in xrange(12,99):
        if no_zero_or_nine_numbers(i) and no_duplicated_numbers(i):
            this_list.append([i//10,i%10])
    
    #order all permutations
    i=0
    while i < len(this_list):
        if this_list[i][0] > this_list[i][1]:
            del this_list[i]
        else:
            i+=1
        
    return this_list
    
ch_9_2_list = list(chose_9_2())
'''
for i in chose_9_2():
    print i 
print sum(1 for x in chose_9_2())
'''

test_num_list = [[3,9,1,8,6,7,2,5,4],[3,9,1,8,6,7,2,5,4]]    
nums_list = [1,2,3,4,5,6,7,8,9]
#nums_list = [1,2,3,4]
result_list = []
for num_list in permuteListGen(nums_list):
#for num_list in test_num_list:
    for num_split in ch_9_2_list:
        #get num1
        #get num2
        #get num3
        #test if num1 * num2 = num3
        #if yes, store num 3 (and also num1,2,3 case)
        str_num1 = ''
        str_num2 = ''
        str_num3 = ''
        
        for i in xrange(len(num_list)):
            if i<num_split[0]:
                str_num1 += str(num_list[i])
            elif i < num_split[1]:
                str_num2 += str(num_list[i])
            else:
                str_num3 += str(num_list[i])
        
        num1 = int(str_num1)
        num2 = int(str_num2)
        num3 = int(str_num3)
        
        if num1*num2 == num3:
            result_list.append([num1,num2,num3])

unique_prod_list = []
for i in result_list:
    print i
    if not i[2] in unique_prod_list:
        unique_prod_list.append(i[2]) 

print sum(unique_prod_list)
    


#num = 7254
#print list(divisorGen(num))




    