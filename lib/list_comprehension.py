
def return_evens(num_list):
    """Returns a list of even numbers from the input list"""
    return [x for x in num_list if x % 2 == 0]


def make_exclamation(sentence_list):
    """Returns a list of sentences with exclamation marks appended"""
    return [s + "!" for s in sentence_list]