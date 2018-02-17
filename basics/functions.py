def hello_func(greeting, name='you'):
    return f'{greeting}, {name}'


print(hello_func('Yo!'))
print(hello_func('Yo!', name='tanzeem'))  # first is positional and second is key-value argument


# variable arguments

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


student_info('a', 'b', value=[1, 2, 3])

course = ['a', 'b']
values = {'name': 'tanzeem'}

student_info(course, values)  # will treat both as parameter arguments since it can't make out
student_info(*course, **values)  # will expand and send
