with open('input.txt', 'r') as f:
    data = f.read()

def process_string(text):
    n_lbrace = 0
    layer = 0
    total_points = 0
    garbage_chars = 0
    in_garbage = False
    ignore_mode = False

    for char in text:
        if ignore_mode:
            ignore_mode = False
        else:
            if in_garbage:
                if char == '>':
                    in_garbage = False
                elif char == '!':
                    ignore_mode = True
                else:
                    garbage_chars += 1
            else:
                if char == '<':
                    in_garbage = True
                elif char == '{':
                    n_lbrace += 1
                    layer += 1

                elif char == '}':
                    total_points += layer
                    layer -= 1

    return total_points, garbage_chars

score, garbage_chars = process_string(data)
print(f"Final score: {score}")
print(f"Non-canceled garbage: {garbage_chars}")
