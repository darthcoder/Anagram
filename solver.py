from collections import defaultdict
import sys, pdb


def word_order(word):
    """This is the hash key
    """
    order = 0               # The actual key
    for letter in word:
        order = order + ord(letter) 
        # ord(letter) gives the ascii code of letter
    return order

def inDict(dat):
    """This is the conversion of the input into
    a dict type hashtable
    """
    diction = defaultdict(list)     # A special type - dict of lists
    oder = 0
    for element in dat:
        # pdb.set_trace()
        oder = word_order(element)
        diction[oder].append(element)   
        # A dict arranged by key, each element of the dict is a list of
        # strings.
            
    return diction

def compare(word1,word2):
    """Words are sorted and compared.
    """
    test_len(word1,word2)   # Test that length of the two words is equal
                            # This is sort of overkill.

    if sorted(word1) == sorted(word2):
        return True
    else:
        return False

def main():
    data = []
    dicti = defaultdict(list)
    odr = 0
    f = open('dictionary.txt','rw')
    # Opening the dictionary

    for line in f:
        parse = line.rstrip()   # Lines have escape characters which need to be removed!
        data.append(parse)      # The sanitized input is stored to a list

    dicti = inDict(data)        # The list is converted to a dict of lists
    inn  = sys.argv[1]          # The input word is read         
    test_sanitary(inn)          # This checks that the input is an alphabet.
    checkWord = inn.lower()     # There might be uppercase letters, they are made lowercase

    orderCheck = word_order(checkWord)
                                # this is the hashkey of the input word

### Now we do the actual comparison of the argument word with the words in 
### the dictionary.
    
    for word in dicti[orderCheck]:      ###Only comparing with same hash words
        if compare(checkWord,str(word)):
            print "The word "+ checkWord+ " is the same as " + word
        else:
            continue

    f.close()


### TEST 1
### The input should be a string, with only english alphabets!

def test_sanitary(sample):
    assert sample.isalpha()

### TEST 2
### The length of the input string should be the same as the strings it is being compared to!

def test_len(sample1, sample2):
    assert len(sample1) == len(sample2)

if __name__ == '__main__':
    main()

