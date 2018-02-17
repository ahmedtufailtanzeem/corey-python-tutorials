gender_old = ['male', 'female']
gender_new = ['neutral']

print(gender_new)
print(len(gender_new))

# range and index
print(gender_old[1])
print(gender_old[0:])
print(gender_old[0:-1])

# get the last element with out worrying about the last index
print(gender_old[-1])

# Append
gender_old.append('new_gender')
print(gender_old)

gender_old.insert(0, 'index0')
print(gender_old)

gender_old.remove('new_gender')  # remove specified object
print(gender_old)
print(gender_old.pop())  # remove the last element

gender_old.append(gender_new)  # will add a list to existing list
print(gender_old)

gender_old.remove(gender_new)
print(gender_old)

gender_old.extend(gender_new)  # will add a list item existing list
print(gender_old)

scores = [10, 56, 8, 45]
print(scores)
scores.reverse()
print(scores)
scores.sort()
print(scores)
scores.sort(reverse=True)
print(scores)

# sort with out changing the list
print(sorted(gender_old))
print(min(scores))
print(max(scores))
print(sum(scores))
print(sum(scores))

for items in scores:
    print(items)

for index, items in enumerate(scores):
    print(index, items)

for index, items in enumerate(scores, start=2):
    print(index, items)

# check presence of element in list
print(45 in scores)
print(451 in scores)
print(scores.index(10))
# print(scores.index(101))  # ValueError if element not found

print("list to string conversion")
nums = ['1', '2', '3']
nums_str = ':'.join(nums)
print(nums)
print(type(nums_str.split(':')))

