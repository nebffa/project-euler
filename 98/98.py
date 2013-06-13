# first time using git for project euler

'''
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36^2. 
What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96^2. 
We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, 
neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, 
find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file. '''


import csv
import math
import time

t = time.time()

file = open('words.txt', 'r')
words = [word for word in csv.reader(file).next()]


# aim: have a dictionary with mappings (dictionaries) as keys (e.g. {C: 1, A: 2, R: 9, E: 6})
# 		and values as a list of words that make a square number using this mapping
#		if the length of the list is greater than 1, then all words in the list are part of some square anagram word pair


# step 1: to see what possible mappings we can use - we can undertake symbol analysis on the square numbers
#       e.g. a 4-digit square number could be of type 1-1-1-1 (e.g. 4444), or type 1-2-1-2 (e.g. 4545), or type 1-2-3-2 (e.g. 4565), etc.
max_word_length = max([len(word) for word in words])
# max square of length max_word_length
highest_number_to_square = int(math.sqrt(10 ** (max_word_length - 1)))
squares = [i**2 for i in range(1, highest_number_to_square)]


squares_to_words = {}
squares.reverse()
# let's analyse the symbols of the square, using the results as keys in a dictionary - no values yet, they are the results of the words analysis
# we analyse the squares in descending order, because smaller squares will fall under larger mappings -
#       e.g. (probably not square numbers here) 1234's mapping would be a subslet of 12345678's map
for square in squares:
    current_symbol = 0
    # use a dictionary to keep track of which symbols already seen
    symbols = {}
    # use a list to replace every digit with a symbol
    letter_symbols = []
    for letter in str(square):
        if symbols.has_key(letter):
            letter_symbols.append(symbols[letter])
        else:
            letter_symbols.append(str(current_symbol))
            symbols[letter] = str(current_symbol)
            current_symbol += 1
    square_symbol = ''.join(letter_symbols)

    if squares_to_words.has_key(square_symbol):
        squares_to_words[square_symbol][0].append(square)
    else:
        squares_to_words[square_symbol] = [[square], []]


# now we analyse the symbols of the words and insert them into squares_to_words as values
for word in words:
    current_symbol = 0
    # use a dictionary to keep track of which symbols already seen
    symbols = {}
    # use a list to replace every digit with a symbol
    letter_symbols = []
    for letter in word:
        if symbols.has_key(letter):
            letter_symbols.append(symbols[letter])
        else:
            letter_symbols.append(str(current_symbol))
            symbols[letter] = str(current_symbol)
            current_symbol += 1

    word_symbol = ''.join(letter_symbols)
    if squares_to_words.has_key(word_symbol):
        squares_to_words[word_symbol][1].append(word)



# now that we have structurally analysed symbols and squares, and have found which ones match, we need to 
# determine what letter mappings are used to take a word to a square (e.g. {C: 1, A: 2, R: 9, E: 6} takes CARE to 1296 = 36^2)
mappings = {} # a dictionary with keys as mappings and values as words that form squares under these mappings
for key, values in squares_to_words.items():
    squares = values[0]
    words = values[1]

    # to reduce the work we need to do - the key can tell us which indices of a word we need to look at.
    # e.g. a key may be 001231122 - in this case we only need to look at the first occurrence of each number, i.e. indices 0, 2, 3, 4, rather than all 8 indices
    indices = []
    seen = []
    for index in range(0, len(key)):
        if key[index] not in seen:
            indices.append(index)
            seen.append(key[index])


    for square in squares:
        for word in words:
            # find the mapping
            mapping = {}
            square_str = str(square)
            for index in indices:
                mapping[word[index]] = square_str[index]

            new_key = tuple(sorted(mapping.items()))
            if mappings.has_key(new_key):
                mappings[new_key].append((square, word))
            else:
                mappings[new_key] = [(square, word)]


max_square = 0
for key, value in mappings.items():
    if len(value) > 1: # there exists a square word pair for this symbol arrangement 
        # we need to check if an anagram pair exists
        
        words = [i[1] for i in value]
        sorted_words = [sorted(word) for word in words]

        anagram_found = False
        for i in range(0, len(words) - 1):
            for j in range(1, len(words)):
                if sorted_words[i] == sorted_words[j]:
                    anagram_found = True
                    break
            if anagram_found:
                break


        # let's see if the square is our maximum yet
        if anagram_found:
            squares = [i[0] for i in value]
            for square in squares:
                if max_square < square:
                    max_square = square

print max_square
print time.time() - t