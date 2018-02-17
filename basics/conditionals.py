if False:
    print("Condition satisfied")
elif True:
    print("El if satisfied")
else:
    print("Condition not satisfied")

a = [1, 2, 3]
b = [1, 2, 3]

# list compare using a == b is true if order and element size is same
if a == b:
    print('a is equal to b')
else:
    print('a and b not equal')

print(a is b)
a = b
print(a is b)

# memory address
print(id(a))

# None
# {}
# []
# 0
# ()
# ''

condition = ''
if condition:
    print('condition met')
else:
    print("condition not met")

if not False:
    print("i used not")





