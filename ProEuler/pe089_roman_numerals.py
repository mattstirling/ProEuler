'''
Created on Nov 25, 2015

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

https://projecteuler.net/about=roman_numerals

@author: Trader
'''

def roman_2_int(str_roman):
    dict_case = {
                  'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000
                  }
    amt = 0
    b_subtractive = 0
    last_val = 0    #force rightmost value to be an addition
    #READ RIGHT TO LEFT
    for i in str_roman[::-1]:
        this_val = dict_case.get(i)
        
        #compare vs last value, could be subtractive
        if b_subtractive and this_val > last_val:
            b_subtractive = 0
        elif not b_subtractive and this_val < last_val:
            b_subtractive = 1
        
        #sum
        if not b_subtractive:
            amt += this_val
        else:
            amt -= this_val
        
        #iterate
        last_val = this_val
        
    return amt

def roman(n):
    
    dict_case = {
                0 : '',
                1 : 'I',
                2 : 'II',
                3 : 'III',
                4 : 'IV',
                5 : 'V',
                6 : 'VI',
                7 : 'VII',
                8 : 'VIII',
                9 : 'IX',
                10 : 'X',
                20 : 'XX',
                30 : 'XXX',
                40 : 'XL',
                50 : 'L',
                60 : 'LX',
                70 : 'LXX',
                80 : 'LXXX',
                90 : 'XC',
                100 : 'C',
                200 : 'CC',
                300 : 'CCC',
                400 : 'CD',
                500 : 'D',
                600 : 'DC',
                700 : 'DCC',
                800 : 'DCCC',
                900 : 'CM',
                }
    
    str_roman = dict_case.get(n,'not_simple')
    if not str_roman == 'not_simple':
        return str_roman
    elif n%1000 == 0:
        return 'M' * (n/1000) 
    else:
        #split in 1000s', 100's, 10's, 1's
        return roman(n//1000 * 1000) + roman( (n//100)%10 *100) + roman( (n//10)%10 *10) + roman(n%10)

def is_roman(str_roman):
    dict_case = {
                  'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000
                  }
    amt = 0
    b_subtractive = 0
    last_val = 0    #force rightmost value to be an addition
    #READ RIGHT TO LEFT
    for i in str_roman[::-1]:
        this_val = dict_case.get(i)
        
        #compare vs last value, could be subtractive
        if b_subtractive and this_val > last_val:
            b_subtractive = 0
        elif not b_subtractive and this_val < last_val:
            b_subtractive = 1
        
        #sum
        if not b_subtractive:
            amt += this_val
        else:
            amt -= this_val
        
        #iterate
        last_val = this_val
        
    return amt


#testing
'''
print roman_2_int('MMMMDCLXXII')
print roman_2_int('XXXXIX')
print roman_2_int('XLIIIIIIIII')
print roman_2_int('XLIX')
print roman_2_int('XLVIIII')
print roman(5)
print roman(5000)
print roman(49)
'''        

#read line from text file
#find the minimal form for the number
#difference len with minimal len
#add to total and iterate        
folder_in = 'C:/Temp/python/in/'
file_in = 'p089_roman.txt'

diff_tot = 0
with open(folder_in + file_in, 'r') as f:
    for line in f:
        str_roman = line.strip()
        this_len = len(str_roman)
        this_int = roman_2_int(str_roman)
        this_min_roman = roman(this_int)
        this_min_len = len(this_min_roman)
        print (str_roman,this_min_roman,this_int,this_len-this_min_len)
        diff_tot += (this_len-this_min_len)

print diff_tot

print roman_2_int('DLV')
print roman_2_int('MCXI')

