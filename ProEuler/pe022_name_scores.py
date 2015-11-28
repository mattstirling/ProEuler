'''
Created on Nov 22, 2015

@author: Trader
'''

folder_in = 'C:/Temp/python/in/'
file_in = 'p022_names.txt'
with open(folder_in + file_in, 'r') as f:
    names = f.readline().split(",")
    f.close()

names.sort()
print len(names)

alpha_score = '_abcdefghijklmnopqrstuvwxyz'.upper()


print alpha_score.find('a')

score = []
count = 1
for name in names:
    this_score = 0
    for i in name.strip('"'):
        #print alpha_score.find(i), i
        this_score += alpha_score.find(i)
        
    score.append(this_score*count)
    count +=1

print sum(score)

