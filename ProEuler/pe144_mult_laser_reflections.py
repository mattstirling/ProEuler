'''
Created on Nov 29, 2015

The light beam in this problem starts at the point (0.0,10.1) just outside the white cell, and the beam first impacts the mirror at (1.4,-9.6).
The section corresponding to -0.01 < x < 0.01 at the top is missing, allowing the light to enter and exit through the hole.
The slope m of the tangent line at any point (x,y) of the given ellipse is: m = -4x/y

@author: Trader
'''
import math

def dot_product(l1,l2):
    return l1[0]*l2[0]+l1[1]*l2[1]

def get_normal_coord(p2):
    #The slope m of the tangent line at any point (x,y) of the given ellipse is: m = -4x/y
    #normal line is then y/4x
    return [p2[0] - 4*p2[0],p1[1]-1*p1[1]]

def get_orthog_proj_coord(l1,l2):
    multiplier = float(dot_product(l1,l2)) / float(dot_product(l2,l2))
    return [multiplier*l2[0],multiplier*l2[1]]

def get_orthog_proj_point(p2,l1,l2):
    orthog_coord = get_orthog_proj_coord(l1,l2)
    return [p2[0] + orthog_coord[0],p2[1] + orthog_coord[1]]

def get_orthog_reflect_point(p1,p2,l1,l2):
    orthog_proj_point = get_orthog_proj_point(p2,l1,l2)
    proj_vect = [orthog_proj_point[0]-p1[0],orthog_proj_point[1]-p1[1]]
    return [p1[0] + 2*proj_vect[0],p1[1] + 2*proj_vect[1]]

def get_slope(p2,p4): 
    return float(p4[1]-p2[1]) / float(p4[0]-p2[0])

def get_intercept(p2,slope):
    return p2[1] - slope*p2[0]

def get_next_point(p2,m,intercept):
    # solution for quadratic equation
    # a*x**2 + b*x + c = 0
    a = 4 + m**2
    b = 2 * m * intercept
    c = intercept**2 - 100
    d = b**2-4*a*c # discriminant
    #print (a,b,c,d)
    
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    
    if abs(x1 - p2[0]) > abs(x2 - p2[0]):
        return [x1, m * x1 + intercept]  
    else:
        return [x2, m * x2 + intercept]

def get_dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2)
    
def get_next_point_2(p1,p2):
    p3 = get_normal_coord(p2)
    #print(p3)
    
    l1 = [p1[0]-p2[0],p1[1]-p2[1]]
    l2 = [p3[0]-p2[0],p3[1]-p2[1]]
    
    #print get_orthog_proj_coord(l1,l2)
    #print get_orthog_proj_point(p2,l1,l2)
    #print get_orthog_reflect_point(p1,p2,l1,l2)
    
    p4 = get_orthog_reflect_point(p1,p2,l1,l2)
    m = get_slope(p2,p4)
    b = get_intercept(p2,m)
    #print [m,b]
    return get_next_point(p2,m,b)

#initialize the first 2 points    
p1 = [0.0,10.1]
p2 = [1.4,-9.6]

#begin with distance calc'd for the first beam
cum_dist = get_dist(p1,p2)

#determine the next beam and add distance until the beam exits the repeater
for i in xrange(1):
    next_pt = get_next_point_2(p1,p2)
    cum_dist += get_dist(p2,next_pt)
    print (i,next_pt,cum_dist)
    
    if next_pt[0]>-0.01 and next_pt[0]<0.01 and next_pt[1]>0:
        print 'light beam exited'
        break
    else: 
        #iterate
        p1 = p2
        p2 = next_pt



