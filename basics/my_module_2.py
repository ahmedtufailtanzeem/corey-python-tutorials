import sys
import my_module
import random
import os
from my_module import my_module_var as var

print(sys.path)
print(var)
courses = ['Math', 'CompScience', 'Physics']
print(my_module.get_index_for_element_in_sequence(courses, 'Math'))

print(help(random.choice))
print(random.choice(courses))

print(os.__file__)
