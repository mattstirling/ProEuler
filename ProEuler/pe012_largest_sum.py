'''
Created on Nov 5, 2015

@author: Trader
'''
folder_in = 'C:/Temp/python/in/'
file_in = 'pe012_50digit_num.txt'

nums=[]
sum=0
with open(folder_in + file_in, 'r') as f:
    for line in f:
        nums.append(str(line).strip())
        sum +=int(str(line).strip()) 

#print int(nums[1])+int(nums[2])
#print len(str(int(2**200 - 1)))
print sum
print str(sum)[:10]
          

