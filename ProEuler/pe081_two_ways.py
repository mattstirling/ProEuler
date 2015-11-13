'''
Created on Nov 12, 2015

@author: Trader
'''

folder_in = 'C:/Temp/python/in/'
file_in = 'p081_matrix.txt'
f = open(folder_in + file_in,'r')
last_line = [999999999 for i in xrange(80)]
last_line[0] = 0
for line in f:
    this_line = [int(i) for i in line.split(',')]
    
    #left-most zero is special
    this_line[0] = this_line[0] + last_line[0] 
    
    #all other points have 2 possible last steps
    for i in xrange(1,len(this_line)):
        this_line[i] = min(this_line[i-1],last_line[i]) + this_line[i]
    
    #iterate
    last_line = this_line

print this_line[79]
     
    
print 310707/80        
    
    #print last_line[0]
    #print this_line[0]
