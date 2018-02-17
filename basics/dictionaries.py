student = {'name': 'tanzeem', 'age': 30}
print(student)
print(student.get('name'))
print(student.get('course'))
print(student.get('course', 'key not defined'))
print(student['age'])  # error if key not found to get around use get function instead

# adding new key
student['course'] = ['Math', 'Social']
print(student)

# updating the key
student['course'] = ['Math', 'Social Science']
print(student)

# updating multiple keys
student.update({'name': 'tanz', 'gender': 'male'})
print(student)

# remove
del student['age']
print(student)

gender = student.pop('gender')
print(gender)
print(student)

# looping
for key in student:
    print(key)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(f'{key} : {value}')

print(len(student)) # print count of keys

print(dir(student))
print(type(student))
print(help(dict.keys))
print(help(student.keys))


