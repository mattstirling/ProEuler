'''
Created on Nov 16, 2015

@author: Trader
'''
folder_in = 'C:/Temp/python/in/'
file_in = 'pe018_tree.txt'

tree=[]
count = 0
with open(folder_in + file_in, 'r') as f:
    for line in f:
        tree.append([])
        for str_num in line.split(' '):
            tree[count].append(int(str_num))
        count += 1



for row in tree:
    print row

this_max = []
last_max = tree[0]
print last_max

for i in xrange(1,len(tree)):
    for j in xrange(0,i+1):
        if j==0:
            this_max.append(tree[i][j]+last_max[j])
        elif j==i:
            this_max.append(tree[i][j]+last_max[j-1])
        else:    
            this_max.append(tree[i][j]+max(last_max[j-1],last_max[j]))
    print this_max
    last_max = this_max
    this_max = []

print last_max
print max(last_max)