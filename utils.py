import string
import os

counter_file = "data/entry_counter.txt"

def generate_entry_number():
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("1")

    with open(counter_file, "r") as f:
        count = int(f.read())

    letter_index = (count - 1) // 9999
    number_part = (count - 1) % 9999 + 1
    letter_part = string.ascii_uppercase[letter_index % 26]

    entry_number = f"{number_part:04}{letter_part}"

    with open(counter_file, "w") as f:
        f.write(str(count + 1))

    return entry_number
