import json

with open('input.json', 'r') as f:
    data = json.load(f)

def sum_numbers_tree(obj):
    if isinstance(obj, list):
        return sum([sum_numbers_tree(item) for item in obj])
    elif isinstance(obj, dict):
        return sum([sum_numbers_tree(item) for item in obj.values()])
    elif isinstance(obj, int):
        return int(obj)
    else:
        return 0

total = sum_numbers_tree(data)
print(f"A ::: Total numbers in the JSON: {total}")

def sum_numbers_nonred(obj):
    if isinstance(obj, list):
        return sum([sum_numbers_nonred(item) for item in obj])
    elif isinstance(obj, dict):
        if "red" in obj.values() or "red" in obj.keys():
            return 0
        else:
            return sum([sum_numbers_nonred(item) for item in obj.values()])
    elif isinstance(obj, int):
        return int(obj)
    else:
        return 0

total_b = sum_numbers_nonred(data)
print(f"B ::: Total numbers among nonred objects: {total_b}")
