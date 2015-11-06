'''
Created on Nov 5, 2015

@author: Trader
'''
folder_in = 'C:/Temp/python/in/'
file_in = 'pe011_grid.txt'

grid=[]
with open(folder_in + file_in, 'r') as f:
    for line in f:
        grid.append([int(num) for num in line.split(' ')])

max_prod = 0
#collect the product of all horizontal lines
for i in range(len(grid)):
    for j in range(len(grid[i])-3):
        print 
        this_prod = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]   
        if this_prod > max_prod:
            max_prod = this_prod

#collect the product of all vertical lines
for i in range(len(grid)-3):
    for j in range(len(grid[i])):
        print 
        this_prod = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]   
        if this_prod > max_prod:
            max_prod = this_prod

#collect the product of all rising diagonals
for i in range(3,len(grid)):
    for j in range(len(grid[i])-3):
        print 
        this_prod = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]   
        if this_prod > max_prod:
            max_prod = this_prod

#collect the product of all falling diagonals
for i in range(len(grid)-3):
    for j in range(len(grid[i])-3):
        print 
        this_prod = grid[i][j]*grid[i+1][j+1]*grid[i+2][j-2]*grid[i+3][j-3]   
        if this_prod > max_prod:
            max_prod = this_prod

print max_prod            
print 'done'
                                                           
                                                    

    
    
        