'''
Created on Nov 8, 2015

using variables and syntax as used here:
http://www.movable-type.co.uk/scripts/latlong.html

syntax doesn't match, but used here for some simpler tranformations:
http://mathworld.wolfram.com/SphericalCoordinates.html

@author: Trader
'''
import numpy as np

bWriteTestOutput = 1
bWriteCoords = 0
folder_out = 'C:/Temp/python/out/'
file_out = 'bot_first_steps.txt'


 
num_bot = [] 
bot_dist = []
impl_path_left = []
impl_path_dist = []

#n is the number of robots
for n in range(823,827):
    
    num_bot.append(n)
    
     #open a file for writing output
    if bWriteTestOutput:
        file_w = open(folder_out + 'n'+str(n)+'_'+file_out,'w')
        #header
        file_w.write('iteration')
        file_w.write(','+'bot1 path distance')
        file_w.write(','+'implied path distance left')
        file_w.write(','+'implied path distance total')
        file_w.write(','+'bot1 distance from pole is')
        file_w.write(','+'bot1 d_dist to pole')
        file_w.write(','+'bot1 v bot2')
        file_w.write(','+'f')
        file_w.write(','+'dist_per_step')
        file_w.write('\n')
    
    #step = .0001
    fixed_f=.0025
    allow_dist_error = .01/2
    max_steps = 200000000
    record_every = 500000
    
    #define the first point of bot #1
    #let x_1, y_1 be (0.999,0) ... this makes lambda_1 = 0
    x_1= 0.999
    y_1=0
    z_1 = np.sqrt(1-0.999**2)
    phi_1 = np.arccos(x_1)
    lambda_1 = np.arctan2(y_1,x_1)
    
    #determine the first point of bot #2, the closest bot to bot#1. This depends on n, the number of bots
    phi_2 = phi_1
    lambda_2 = 2*np.pi/n
    x_2 = np.cos(lambda_2)*np.cos(phi_2)
    y_2 = np.sin(lambda_2)*np.cos(phi_2)
    z_2 = np.sin(phi_2) 
    #print np.sqrt(x_2**2+y_2**2+z_2**2) #test that length should be 1
    #print np.tan(lambda_1) 
    #print np.cos(phi_1)
    
    #initialize dist from pole
    this_dist_from_pole = np.sqrt((x_1-0)**2 + (y_1-0)**2 + (z_1-1)**2)
    last_dist_from_pole = this_dist_from_pole
    
   
    last_dist_count = allow_dist_error * 10
    dist_count = 0
    for i in range(max_steps):
        
        #determine the distance between bot1 and bot 2
        distance = np.arccos(np.sin(phi_1)*np.sin(phi_2)+np.cos(phi_1)*np.cos(phi_2)*np.cos(lambda_1-lambda_2))
        
        #2nd distance to check work, should be identical to first distance
        #a_dist = (np.sin(np.sqrt((phi_2-phi_1)/2)))**2 + np.cos(phi_1)*np.cos(phi_2)*(np.sin((lambda_2-lambda_1)/2))**2
        #distance = 2*np.arctan2(np.sqrt(a_dist),np.sqrt(1-a_dist))
        #print distance2
        
        #print distance
        #print 0.999*2*np.pi/3 #the distance along the longitude should be slightly longer
    
        #get an intermediate point that is "1 step" away from bot1, in the direction of bot2
        
        #f = .001 #set f to be step/distance so that we travel a distance of "1 step" per iteration
        #f = min(step/distance,1)
        f=fixed_f
        dist_count += f*distance
        a = np.sin((1-f)*distance)/np.sin(distance)
        b= np.sin(f*distance)/np.sin(distance)
        x_next = a*np.cos(phi_1)*np.cos(lambda_1)+b*np.cos(phi_2)*np.cos(lambda_2)
        y_next = a*np.cos(phi_1)*np.sin(lambda_1)+b*np.cos(phi_2)*np.sin(lambda_2)
        z_next = a*np.sin(phi_1) + b*np.sin(phi_2)
        phi_next = np.arctan2(z_next,np.sqrt(x_next**2+y_next**2))
        lambda_next = np.arctan2(y_next,x_next)
        
        
        
        #Exit criteria for v1: once we are within one step of the pole, we are done.... exits too early
        #if this_dist_from_pole <= step*2:
        
        #Exit criteria for v2: once total distance stops getting more accurate at .01 precision
        this_dist_from_pole = np.sqrt((x_next-0)**2 + (y_next-0)**2 + (z_next-1)**2)
        impl_dist_left = this_dist_from_pole*f*distance/(last_dist_from_pole - this_dist_from_pole)
        
        if impl_dist_left < allow_dist_error:
            print 'done iterating.'
            #dist_count += this_dist_from_pole #this is redundant as we later round this away
            print ''
            print 'iteration '+str(i)
            print 'bot1 distance is ' + str(dist_count)
            print 'bot1 distance from pole is ' + str(this_dist_from_pole)
            print 'moved ' + str(last_dist_from_pole - this_dist_from_pole) + ' closer to pole in this step'
            print ''
            print 'f is:' +str(f)
            print 'bot1 v bot2,distance: ' + str(distance)
            print 'implied path distance left: ' + str(impl_dist_left)
            print 'implied path distance: ' + str(dist_count + impl_dist_left)
            
            file_w.write(str(i))
            file_w.write(','+str(dist_count))
            file_w.write(','+str(impl_dist_left))
            file_w.write(','+str(dist_count+impl_dist_left))
            file_w.write(','+str(this_dist_from_pole))
            file_w.write(','+str(last_dist_from_pole - this_dist_from_pole))
            file_w.write(','+str(distance))
            file_w.write(','+str(f))
            file_w.write(','+str(f*distance))
            file_w.write('\n')
            
            bot_dist.append(dist_count)
            impl_path_left.append(impl_dist_left)
            impl_path_dist.append(dist_count + impl_dist_left)

            
            break
        
            
            
        #now prepare for iterating for the next step
        
        #get the delta for lambda and phi
        d_phi = phi_next - phi_1
        d_lambda = lambda_next - lambda_1
    
        #iterate for point_2
        phi_2_next = phi_2 + d_phi
        lambda_2_next = lambda_2 + d_lambda
        
        #now test.... translate back into xyz. z should be the same for both, length should be 1
        if bWriteTestOutput and i%record_every==0:
            x_1= np.cos(lambda_1)*np.cos(phi_1)
            y_1= np.sin(lambda_1)*np.cos(phi_1)
            z_1 = np.sin(phi_1) 
    
            x_2= np.cos(lambda_2)*np.cos(phi_2)
            y_2= np.sin(lambda_2)*np.cos(phi_2)
            z_2 = np.sin(phi_2) 
            
            x_2_next = np.cos(lambda_2_next)*np.cos(phi_2_next)
            y_2_next = np.sin(lambda_2_next)*np.cos(phi_2_next)
            z_2_next = np.sin(phi_2_next) 
            
            print ''
            print 'iteration '+str(i)
            print 'bot1 distance is ' + str(dist_count)
            print 'bot1 distance from pole is ' + str(this_dist_from_pole)
            print 'moved ' + str(last_dist_from_pole - this_dist_from_pole) + ' closer to pole in this step'
            print ''
            print 'f is:' +str(f)
            print 'bot1 v bot2,distance: ' + str(distance)
            print 'implied path distance left: ' + str(impl_dist_left)
            print 'implied path distance: ' + str(dist_count + impl_dist_left)
                
            
            file_w.write(str(i))
            file_w.write(','+str(dist_count))
            file_w.write(','+str(impl_dist_left))
            file_w.write(','+str(dist_count+impl_dist_left))
            file_w.write(','+str(this_dist_from_pole))
            file_w.write(','+str(last_dist_from_pole - this_dist_from_pole))
            file_w.write(','+str(distance))
            file_w.write(','+str(f))
            file_w.write(','+str(f*distance))
            file_w.write('\n')
            
            if bWriteCoords:
                print 'bot1:  ',x_1,y_1,z_1,lambda_1, phi_1
                print 'bot1+: ',x_next,y_next,z_next,lambda_next,phi_next
                print 'bot2: ',x_2,y_2,z_2,lambda_2,phi_2
                print 'bot2+: ',x_2_next,y_2_next,z_2_next,lambda_2_next,phi_2_next
                print ''
                print 'bot1_z - bot2_z:',z_1-z_2
                print 'bot1+_z - bot2+_z:',z_next-z_2_next
                print ''
                print 'bot1_phi - bot2_phi:',phi_1-phi_2
                print 'bot1+_phi - bot2+_phi:',phi_next-phi_2_next
            
                file_w.write('bot1,' + str(x_1) + ','+str(y_1)+','+str(z_1)+','+str(lambda_1)+','+str(phi_1) + '\n')
                file_w.write('bot1+,' + str(x_next) + ','+str(y_next)+','+str(z_next)+','+str(lambda_next)+','+str(phi_next)+ '\n')
                file_w.write('bot2,' + str(x_2) + ','+str(y_2)+','+str(z_2)+','+str(lambda_2)+','+str(phi_2)+ '\n')
                file_w.write('bot2+,' + str(x_2_next) + ','+str(y_2_next)+','+str(z_2_next)+','+str(lambda_2_next)+','+str(phi_2_next)+ '\n')
        
        #iterate
        phi_1 = phi_next
        lambda_1 = lambda_next
        phi_2 = phi_2_next
        lambda_2 = lambda_2_next
        last_dist_from_pole = this_dist_from_pole
        last_dist_count = dist_count
        
    print 'bot1 distance is ' + str(dist_count)  
    print 'rounding to .01 precision: ' + str(round(dist_count,2))
    print 'and for all ' + str(n) + ' bots: ' + str(n*round(dist_count,2))


print bot_dist
print impl_path_left
print impl_path_dist

folder_out = 'C:/Temp/python/out/'
file_out = 'bot_output.txt'
file_w = open(folder_out + file_out,'w')
#header
file_w.write('bot_num, bot dist,impl path left,impl path dist'+'\n')
for i in range(len(num_bot)):
    file_w.write(str(num_bot[i])+',')
    file_w.write(str(bot_dist[i])+',')
    file_w.write(str(impl_path_left[i])+',')
    file_w.write(str(impl_path_dist[i])+'\n')
    
