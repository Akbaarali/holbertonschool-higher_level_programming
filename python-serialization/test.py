from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data, "data.json")
print("Saved")

loaded = load_and_deserialize("data.json")
print(loaded)
