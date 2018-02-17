# lets learn about strings

my_message = 'Hello World'

multi_line_string = '''This is a multi line
string in python'''

print(my_message)
print(multi_line_string)

print(len(my_message))

# slicing
print(my_message[0:])
print(my_message[:11])
print(my_message[0:5])

# functions
print(my_message.lower())
print(my_message.count('ll'))
print(my_message.upper())
print(my_message.find('lll'))  # -1 If not found else index of first find
print(my_message.find('l'))
print(my_message.replace('World', 'Universe'))
print('Tanzeem' + " Ahmed")
name = 'tanzeem'
print('Welcome, {}'.format(my_message))
print(f'Welcome, {name}')

# Help
print(dir(int))  # shows all available methods and variables
print(help(str))
print(help(str.lower))

