import json
sample_json = '{"name": "John", "age": 31, "city": "New York"}'

# JSON to python value aka Dictionary
json_as_python_values = json.loads(sample_json)
print(json_as_python_values)
print(type(json_as_python_values))

# python value to JSON
dictionary_to_json_string = json.dumps(json_as_python_values)
print(type(dictionary_to_json_string))
print(dictionary_to_json_string)

undefined = 12
if undefined:
    print('value is undefined')
else:
    print('value is defined')
