import json 

# Deserialize json format
json_data = '{"name": "Ibrahim Hanafi", "age": 23, "test": "json"}'

# Deserialize JSON data into Python object
data = json.loads(json_data)

print("Deserialized Python object:")
print(data)