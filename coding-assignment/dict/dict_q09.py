#Use get() to Access a Value Safely
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("name"))  # Access the value for the key "name"
print(my_dict.get("city", "Not Found"))  # Provide a default value if the key doesn't exist
