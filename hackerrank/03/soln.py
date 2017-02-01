def ransom_note_lazy(mag, rn):
    mag_words    = mag.split(' ')
    ransom_words = rn.split(' ')
    
    # reuse
    
    # lazy, inefficient solution
    for word in ransom_words: # n * ...
        if not (word in mag_words): # O(m) # if word not in ...
            return False
            # fail for repeated words
            # TODO: write unit test
            
            # could search for index and remove
    return True
    # O(n * m)

def ransom_note_sort(mag, rn):
    mag_words    = mag.split(' ')
    ransom_words = rn.split(' ')

    # O(n * log(n))
    ransom_words.sort()
    # O(m * log(m))
    mag_words.sort()
    
    print(mag_words)
    print(ransom_words)
    
    # O(m)
    for i in list(range(0, len(mag_words))): # m * ...
    
        if ransom_words == []: # O(1)
            return True

        # avoid index out-of-range, so check ransom_words len
        # but will never get empty mag_words
        
        if ransom_words[-1] == mag_words[-1]: # O(1)
            ransom_words.pop() #O(1)
        mag_words.pop() # O(1)
        
        print(mag_words)
        print(ransom_words)

    return ransom_words == []
    # O(m*log(m) + n*log(n))

# TODO write O(n + m) with hashing..
# python dictionaries
'''
    # or use trie!!!

    # create hash for both O(m)
    mag_hash(mag_words)
    for each word in ransom: O(n)
        if mag_hash[word] O(1)
            remove word from mag_hash O(1)
        else
            return False
'''

def ransom_note_dict(mag, rn):
    mag_words    = mag.split(' ')
    ransom_words = rn.split(' ')
    
    # create and fill dictionary # O(m)
    mag_dict = dict()
    for word in mag_words: # m * ...
        count = 0
        if word in mag_dict:
            count = mag_dict[word] # O(1)
        mag_dict[word] = 1 + count # O(1)

    # O(n)
    for word in ransom_words: # n * ...
        if word in mag_words: # O(1)
            count = mag_dict[word]
            if count == 1:
                mag_dict.pop(word)
            else:
                mag_dict[word] = count - 1
        else:
            return False
    return True
    # O(m + n)

ransom_note = ransom_note_dict
