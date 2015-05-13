#!/usr/bin/python

THRESHOLD = 10L ** 6
length_memo = {1: 1}

def collatz_length(n):
    '''Recursively builds a dict of lenghts of
    Collatz sequences.
    '''
    if n not in length_memo:
        if n % 2 == 0:
            length_memo[n] = 1 + collatz_length(n / 2)
        else:
            length_memo[n] = 1 + collatz_length(3 * n + 1)
    return length_memo[n]


def longest_sequence(memo):
    '''Finds longest memoized Collatz length and
    returns the sequence starting number.
    '''
    max_v = max(memo.values())
    keys = [x for x,y in memo.items() if y == max_v]
    return keys


# Generates all Collatz sequence lengths < 10 ** 6
for i in range(1, THRESHOLD):
    collatz_length(i)

starting_nums = longest_sequence(length_memo)

for the_number in starting_nums:
    print "The number under %d that produces the longest chain is %s.\
 Chain length is %d." % (THRESHOLD, the_number, length_memo[the_number])
