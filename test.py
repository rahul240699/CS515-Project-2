import sys
import os
import subprocess
import difflib

process = subprocess.run(["cat test1.in | python3 adventure.py loop.map"], capture_output= True, shell= True, text=True)

output = process.stdout

with open("test_2_1.out", "r") as file:
    expected_output = file.read()

with open("test_2.out", "r") as f:
    my_output = f.read()


def compare_strings(string1, string2):
    d = difflib.Differ()
    diff = d.compare(string1.splitlines(), string2.splitlines())
    return '\n'.join(diff)

differences = compare_strings(expected_output, my_output)
print("Differences:\n", differences)
