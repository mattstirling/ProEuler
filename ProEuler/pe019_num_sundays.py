'''
Created on Nov 22, 2015

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

@author: Trader
'''
def is_leap_year(yyyy):
    
    if yyyy%4==0:
        if yyyy%100==0:
            if yyyy%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
        

def num_days_in_month (yyyy,mm):
    
    if mm==2:
        if is_leap_year(yyyy):
            return 29
        else:
            return 28
        
    dict_case = {
                  1: 31,
                  3: 31,
                  4: 30,
                  5: 31,
                  6: 30,
                  7: 31,
                  8: 31,
                  9: 30,
                  10: 31,
                  11: 30,
                  12: 31
                }
    return dict_case.get(mm,31)
    
    

def next_date(yyyy,mm,dd):
    if dd < 28:
        return (yyyy,mm,dd+1)
    else:
        
        if dd < num_days_in_month(yyyy,mm):
            return (yyyy,mm,dd+1)
        else:
            if mm < 12:
                return (yyyy,mm+1,1)
            else:
                return (yyyy+1,1,1)

        
year = 1900
month = 1
day = 1
weekday = 0 #0 is Monday, 6 is Sunday

count = 0

for i in range(40000):
    
    #count the Sunday on the first of the month
    if day==1 and i%7==6 and year>1900:
        print (year,month,day), i%7
        count+=1
    
    #iterate
    (year,month,day) = next_date(year,month,day)
    
    if (year,month,day)==(2000,12,31):
        print count
        break

print 365%7

for i in range(1900,2001,4):
    print i, is_leap_year(i)
