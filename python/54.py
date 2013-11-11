import csv
import time 
from collections import Counter as counter

t = time.time()

def royals_to_numbers(player):
    for i in range(0, 5):
        if (player[i])[0] == 'A':
            player[i] = '14' + (player[i])[1]
        elif (player[i])[0] == 'K':
            player[i] = '13' + (player[i])[1]
        elif (player[i])[0] == 'Q':
            player[i] = '12' + (player[i])[1]
        elif (player[i])[0] == 'J':
            player[i] = '11' + (player[i])[1]
        elif (player[i])[0] == 'T':
            player[i] = '10' + (player[i])[1]
    
    return player
            
def flush(player):
    if (player[0])[-1] == (player[1])[-1] == (player[2])[-1] == (player[3])[-1] == (player[4])[-1]:
        return True
    else:
        return False

def straight(player):
    values = [int(x[:-1]) for x in player]
    values.sort()   
    if values == range(values[0], values[0] + 5):
        return True
    else:
        return False
        
def sets(player):
    values = [int(k[:-1]) for k in player]
    values_counter = counter(values).items()
    values_counter.sort(key = lambda values: values[1])
    return values_counter
    
def hand(is_flush, is_straight, values_counter):
    if is_flush and is_straight:
        return (8, (values_counter[0])[0])
    elif (values_counter[-1])[1] == 4:
        return (7, (values_counter[-1])[0])
    elif (values_counter[-1])[1] == 3 and (values_counter[-2])[1] == 2:
        return (6, (values_counter[-1])[0])
    elif is_flush:
        values_counter.sort()
        values_counter = values_counter[::-1]
        return (5, (values_counter[0])[0],  (values_counter[1])[0],  (values_counter[2])[0],  (values_counter[3])[0],  (values_counter[4])[0])
    elif is_straight:
        return (4, (values_counter[-1])[0])
    elif (values_counter[-1])[1] == 3 and (values_counter[-2])[1] == 1:
        return (3, (values_counter[-1])[0])
    elif (values_counter[-1])[1] == 2 and (values_counter[-2])[1] == 2:
        return (2, (values_counter[-1])[0], (values_counter[-2])[0], (values_counter[-3])[0])
    elif (values_counter[-1])[1] == 2 and (values_counter[-2])[1] == 1:
        return (1, (values_counter[-1])[0], (values_counter[-2])[0], (values_counter[-3])[0], (values_counter[-4])[0])
    else:
        values_counter.sort()
        values_counter = values_counter[::-1]
        return (0, (values_counter[0])[0],  (values_counter[1])[0],  (values_counter[2])[0],  (values_counter[3])[0],  (values_counter[4])[0])
        
def compare(player1, player2):
    for i in range(0, len(player1)):
        if player1[i] > player2[i]:
            return True
        elif player1[i] < player2[i]:
            return False

            
wins = 0
end_file = 1
lines = 0
# read in text file
with open("poker.txt", 'rb') as f:
    import csv
    while end_file:
        try: 
            line = csv.reader(f, delimiter = ' ').next()
            player1 = line[0:5]
            player2 = line[5:10]
            player1 = royals_to_numbers(player1)
            is_flush = flush(player1)
            is_straight = straight(player1)  
            values_counter = sets(player1)
            player1_hand = hand(is_flush, is_straight, values_counter)
            player2 = royals_to_numbers(player2)
            is_flush = flush(player2)
            is_straight = straight(player2)
            values_counter = sets(player2)
            player2_hand = hand(is_flush, is_straight, values_counter)
            

            if compare(player1_hand, player2_hand) == True:
                wins += 1
    
        except:
            end_file = 0
            
print wins
print time.time() - t