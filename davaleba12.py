import json
import os

def create_file(folder_path, file_name):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        file.write("[]")
    return file_path

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = json.load(file)
    return content

def update_file(file_path, new_content):
    with open(file_path, 'w') as file:
        json.dump(new_content, file, indent=4)

def add_to_file(file_path, data_dict):
    content = read_file(file_path)
    if isinstance(content, list):
        content.append(data_dict)
    update_file(file_path, content)

chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

new_players = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]

folder_path = "./chess_data"
file_name = "chess_players.json"
file_path = create_file(folder_path, file_name)
update_file(file_path, chess_players)

for player in new_players:
    add_to_file(file_path, player)

final_content = read_file(file_path)
print(final_content)
