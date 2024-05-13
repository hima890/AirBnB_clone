import json

# Data object
data = {
    "name" : "Ibrahim Hanafi",
    "age" : 23,
    "test" : "json"
}

# Convert python object into json format
json_data = json.dumps(data)

print("Serialized JSON data:")
print(json_data)