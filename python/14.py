greatestSequenceLength = 0
Seed = 0
for i in range(1, 1000000):
    seedStore = i
    # find length of sequence
    sequenceLength = 1
    while i != 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = 3 * i + 1
        sequenceLength += 1

    if sequenceLength > greatestSequenceLength:
        greatestSequenceLength = sequenceLength
        seed = seedStore

print "the greatest sequence length = %d" % greatestSequenceLength
print "seed = %d" % seed