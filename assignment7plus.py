def find_index_of_nth_occurrence(sequence, element_to_find, occurrence):
    """ Returns the location of the n-th occurrence of an element within a sequence """
    needle = -1
    while occurrence > 0:
        needle = sequence.find(element_to_find, needle + 1)
        occurrence -= 1
    return needle


def remove_at(sequence, index_to_remove):
    """ Removes an element from a sequence at the specified index.

    Returns the updated sequence and the element that was removed, in that order.
    """
    removed_element = sequence[index_to_remove]
    updated_sequence = sequence[:index_to_remove] + sequence[index_to_remove+1:]
    return updated_sequence, removed_element


def insert_at(sequence, index, element):
    """ Inserts an element at the specified location in a sequence and returns the updated sequence. """
    return sequence[:index] + element + sequence[index:]


def move_one(from_pillar, to_pillar, state):
    removed_state, element = remove_at(state, find_index_of_nth_occurrence(state, '|', from_pillar) - 1)
    new_state = insert_at(removed_state, find_index_of_nth_occurrence(removed_state, '|', to_pillar), element)
    return new_state


# ... add your functions from the previous solution here at the top

def move_many(how_many, from_pillar, to_pillar, state):
    """ Moves the specified number of discs from one pillar to another and returns the updated state representation.

    Prints the state for every move made.
    """
    print(move_one(from_pillar, to_pillar, state))


# Keep the following lines as they are
number_of_discs = int(input("How many discs are on the left-most pillar? "))
initial_state = ""
for disc in range(number_of_discs, 0, -1):
    initial_state += str(disc)
initial_state += "|||"
print(initial_state)
move_many(how_many=number_of_discs, from_pillar=1, to_pillar=3, state=initial_state)
