# NOTE: does not implement '3 doubles in a row' ==> Jail

import operator
import itertools
import fractions
from random import choice, randint
from time import time

t = time()

def generate_two_die_probabilities(highest_die_value):
    die = range(1, highest_die_value + 1)
    outcome_space_size = highest_die_value ** 2
   
    rolls = list(itertools.product(die, repeat = 2))
    return [sum(i) for i in rolls]



# number of times the player lands on a square
places_visited_count = dict((i, 0) for i in range(40))

highest_die_value = 4
die_possibilities = generate_two_die_probabilities(highest_die_value)

place = 0
turns = 0
community_chest_places = set([2, 17, 33])
chance_places = set([7, 22, 36])
while turns < 10 ** 6:

    # generate roll of the die here
    place += choice(die_possibilities)
    place = place % 40
    
    if place in community_chest_places:
        community_chest = [0, 10] + [-1] * 14
        community_chest_selection = community_chest[randint(0, 15)]
        
        if community_chest_selection == -1:
            pass
        else:
            place = community_chest_selection
        
        
    elif place in chance_places:
        chance = [0, 10, 11, 24, 39, 5, 100, 100,  101, 102] + [-1] * 6
        chance_selection = chance[randint(0, 15)]
        
        if chance_selection == -1:
            pass
        elif chance_selection < 40:
            place = chance_selection
        elif chance_selection == 100:
            # next railway station
            place = int(round(place * 1.0 / 10) * 10 + 5) % 40
        elif chance_selection == 101:
            # next utility
            if place == 22:
                place = 28
            else:
                place = 12
        else:
            place -= 3
                
    elif place == 30:
        place = 10
    
        
        
    places_visited_count[place] += 1    
    turns += 1
    
places_visited_count = sorted(places_visited_count.iteritems(), key=operator.itemgetter(1))
just_keys = [i[0] for i in places_visited_count]
just_keys.reverse()
print just_keys
print time() - t
    

        
    