import json

# Python object to be written to a JSON file
data = {
    "name" : "Ibrahim Hanafi",
    "age" : 23,
    "test" : "json"
}

# Write Python object to a JSON file
with open('output.json', 'w') as file:
    json.dump(data, file)

print("JSON data written to file 'output.json'")
