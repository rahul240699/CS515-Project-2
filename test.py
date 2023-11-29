import sys
import os
import subprocess
import difflib

process = subprocess.run(["cat test.in | python3 adventure.py loop.map"], capture_output= True, shell= True, text=True)

output = process.stdout

with open("test.out", "r") as file:
    expected_output = file.read()

def compare_strings(string1, string2):
    d = difflib.Differ()
    diff = d.compare(string1.splitlines(), string2.splitlines())
    return '\n'.join(diff)

differences = compare_strings(expected_output, output)
print("Differences:\n", differences)
