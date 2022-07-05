#!/usr/bin/python3
"""a script that adds all arguments to a Python list,
 and then save them to a file:"""


from os import path
from sys import argv
save_to_json_file = __import__('5-save_to_json').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
json_list = []

if path.exists(file):
    json_list = load_from_json_file(file)

for i in range(1, len(argv)):
    json_list.append(argv[i])

save_to_json_file(json_list, file)
