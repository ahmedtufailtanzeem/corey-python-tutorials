print('this is a sample module, that will be imported')

my_module_var = 'sample module'


def get_index_for_element_in_sequence(sequence, target):
    for index, value in enumerate(sequence):
        if value == target:
            return index

    return -1


def do_nothing():
    pass
