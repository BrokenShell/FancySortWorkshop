user_data = [
    {"first_name": "John", "last_name": "Smith", "age": 42},
    {"first_name": "Jane", "last_name": "Smith", "age": 38},
    {"first_name": "Jane", "last_name": "Smith", "age": 17},
    {"first_name": "Jimmy", "last_name": "Smith", "age": 12},
    {"first_name": "Oscar", "last_name": "Addams", "age": 38},
]

user_data.sort(key=lambda x: (x["last_name"], x["first_name"], -x["age"]))
print(user_data)
