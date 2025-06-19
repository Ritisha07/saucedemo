import json
import os

def load_login_data():
    file_path = os.path.join(os.path.dirname(__file__), '../data/login_data.json')
    with open(file_path, 'r') as file:
        return json.load(file)
def get_valid_login_data():
    data = load_login_data()
    return [(entry["username"], entry["password"]) for entry in data["valid"].values()]
