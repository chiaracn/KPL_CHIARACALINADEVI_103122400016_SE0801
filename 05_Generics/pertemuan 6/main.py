import json
data = {
    "nama": "John Doe",
    "usia": 30,
}

json_str = json.dumps(data)
print(data["nama"]) # ini adalah objek/dictionary
print(json_str) # ini adalah string JSON
print(data == json.loads(json_str))
