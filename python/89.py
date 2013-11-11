import csv
import time

t = time.time()

def numeral_to_decimal(numeral, roman):
    value = 0
    i = 0
    while True:
        if i == len(numeral):
            break
        elif i + 1 == len(numeral):
            value += roman[numeral[i]]
            break
        elif roman[numeral[i]] < roman[numeral[i + 1]]: # numeral[i] is therefore a 'prefix' for numeral[i + 1], e.g. IX
            value += roman[numeral[i + 1]] - roman[numeral[i]]
            i += 2
        else:       
            value += roman[numeral[i]]
            i += 1
            
    return value

def decimal_to_standardised_numeral(value, roman):

    
    standardised_numeral = ''
    while value / 1000 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'M'])
        value -= 1000
        
    if value / 900 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'CM'])
        value -= 900
    elif value / 500 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'D'])
        value -= 500
    elif value / 400 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'CD'])
        value -= 400
    
    while value / 100 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'C'])
        value -= 100

    if value / 90 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'XC'])
        value -= 90
    elif value / 50 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'L'])
        value -= 50
    elif value / 40 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'XL'])
        value -= 40
        
    while value / 10 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'X'])
        value -= 10
        
    if value / 9 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'IX'])
        value -= 9
    elif value / 5 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'V'])
        value -= 5
    elif value / 4 > 0:
        standardised_numeral = ''.join([standardised_numeral, 'IV'])
        value -= 4
    
    while value > 0:
        standardised_numeral = ''.join([standardised_numeral, 'I'])
        value -= 1
    
    return standardised_numeral
    
    
file = open('TextFiles/roman.txt', 'r')

roman = {
            'M': 1000, 
            'D': 500, 
            'C': 100, 
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

tally = 0
for line in csv.reader(file):
    numeral = line[0]
    
    value = numeral_to_decimal(numeral, roman)
            
    standardised_numeral = decimal_to_standardised_numeral(value, roman)
    
    tally += len(numeral) - len(standardised_numeral)
    
print tally
print time.time() - t