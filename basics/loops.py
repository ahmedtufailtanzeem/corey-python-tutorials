for index in range(1, 11, 2):  # increment is specified as last parameter
    print(index)

for index in range(1, 11):
    if index == 7:
        break
    print(index)

for index in range(10):
    if index == 1:
        continue
    print(index)

x = 1
while x < 10:
    print(x)
    x += 5

while True:
    print(x)
    if x % 25 == 0:
        break
    x += 1

for index in range(1, 3):
    for character in 'ab':
        print(f'{index} : {character}')
