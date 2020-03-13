#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # Go through list of weights
    for i in range(length):
        # Check to see if a hash exists
        index_1 = hash_table_retrieve(
            ht, limit - weights[i])
        # If there's a hash, return tuple of pair 
        if index_1 is not None:
            index_2 = (i, index_1)
            return index_2
        # Else, insert into hash table
        else: 
            hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
