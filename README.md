# README

Checks if a given word is actually an anagram of the other.

## APPROACH

A good key turned out to be simply the sum of ascii codes of all letters of
the input word. Thus a word 'aa' maps out to 194 and so on. The most important
benefit of this approach is simply that all permutations of a word map out to
the same key.

## IDEA

Given an input string, its hashkey is computed according to the above method.
The dictionary.txt file is hashed to a python dict hash table. Now we only
test the input string against those entries of the dict, which have the same
hash key as the input string!
Also, instead of actually computing all the permutations and comparing against
all the words that mapped to each dictionary key, we simply sort the input word
and the words in the dictionary and check if those are equal. This actually
should reduce the computation time, and is equivalent to the longer method of
actually checking each permutation individually.