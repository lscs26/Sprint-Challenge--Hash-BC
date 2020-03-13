#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Put each ticket in the hash table by the source
    for ticket in tickets: 
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # get the first source of None
    nextDestination = hash_table_retrieve(hashtable, 'NONE')
    route[0] = nextDestination
    hash_table_remove(hashtable, 'NONE')

    # Iterate through the rest
    for i in range(1, length - 1):
        route[i] = hash_table_retrieve(hashtable, nextDestination)
        nextDestination = hash_table_retrieve(hashtable, nextDestination)

    return [i for i in route if i is not None]
